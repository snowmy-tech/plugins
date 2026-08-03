# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Secure storage for Launch with AWS OAuth credentials.

On macOS, secrets are stored in the user's login Keychain. Other platforms
must provide an explicit credential helper through
``LAUNCH_WITH_AWS_CREDENTIAL_HELPER``. The helper is invoked with one of
``get``, ``store``, or ``delete`` followed by the client id. ``store`` reads
the JSON secret payload from stdin and ``get`` writes it to stdout.
"""

import json
import os
import shlex
import subprocess
import sys
from typing import Optional


ENV_CREDENTIAL_HELPER = "LAUNCH_WITH_AWS_CREDENTIAL_HELPER"
KEYCHAIN_SERVICE = "com.amazon.launch-with-aws.oauth-session"


class CredentialStoreError(RuntimeError):
    """Raised when the configured OS credential store cannot be used."""


def _helper_command() -> Optional[list[str]]:
    value = os.environ.get(ENV_CREDENTIAL_HELPER, "").strip()
    if not value:
        return None
    command = shlex.split(value)
    if not command:
        raise CredentialStoreError(f"{ENV_CREDENTIAL_HELPER} is empty.")
    return command


def _backend_command(operation: str, account: str) -> tuple[list[str], bool]:
    helper = _helper_command()
    if helper:
        return [*helper, operation, account], False
    if sys.platform == "darwin":
        base = ["/usr/bin/security"]
        if operation == "store":
            # Keeping -w last makes security read the password from stdin,
            # rather than exposing it in the process argument list.
            return [*base, "add-generic-password", "-U", "-s", KEYCHAIN_SERVICE, "-a", account, "-w"], True
        if operation == "get":
            return [*base, "find-generic-password", "-s", KEYCHAIN_SERVICE, "-a", account, "-w"], True
        if operation == "delete":
            return [*base, "delete-generic-password", "-s", KEYCHAIN_SERVICE, "-a", account], True
    raise CredentialStoreError(
        "No secure OAuth credential store is configured. On non-macOS systems, "
        f"set {ENV_CREDENTIAL_HELPER} to an OS-keyring or managed-secret helper."
    )


def _run(operation: str, account: str, payload: Optional[str] = None) -> subprocess.CompletedProcess[str]:
    command, is_keychain = _backend_command(operation, account)
    if operation == "store" and is_keychain:
        return _store_keychain(command, payload or "")
    result = subprocess.run(
        command,
        input=(payload + "\n") if payload is not None else None,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode == 0:
        return result
    # macOS security returns 44 when an item was not found. Credential helpers
    # use the conventional exit code 1 for a missing item.
    if operation in ("get", "delete") and result.returncode == (44 if is_keychain else 1):
        return result
    detail = (result.stderr or "").strip()
    suffix = f" ({detail})" if detail else ""
    raise CredentialStoreError(f"Secure credential {operation} failed{suffix}.")


def _store_keychain(command: list[str], payload: str) -> subprocess.CompletedProcess[str]:
    """Store via Security.framework while passing secret data only on stdin."""
    account = command[-2]
    swift = """import Foundation
import Security
let account = CommandLine.arguments.last!
let secret = FileHandle.standardInput.readDataToEndOfFile()
let query: [String: Any] = [kSecClass as String: kSecClassGenericPassword,
 kSecAttrService as String: \"com.amazon.launch-with-aws.oauth-session\",
 kSecAttrAccount as String: account]
let status = SecItemCopyMatching(query as CFDictionary, nil)
let result: OSStatus
if status == errSecSuccess {
 result = SecItemUpdate(query as CFDictionary, [kSecValueData as String: secret] as CFDictionary)
} else {
 var item = query
 item[kSecValueData as String] = secret
 result = SecItemAdd(item as CFDictionary, nil)
}
exit(result == errSecSuccess ? 0 : 1)
"""
    result = subprocess.run(
        ["/usr/bin/swift", "-e", swift, account],
        input=payload.encode("utf-8"),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise CredentialStoreError("Secure credential store failed.")
    return subprocess.CompletedProcess(command, result.returncode, "", "")


def store_session_secrets(client_id: str, secrets: dict[str, str]) -> None:
    required = ("client_secret", "access_token", "refresh_token")
    if not client_id or any(not secrets.get(name) for name in required):
        raise CredentialStoreError("Refusing to store an incomplete OAuth credential set.")
    payload = json.dumps({name: secrets[name] for name in required}, separators=(",", ":"))
    _run("store", client_id, payload)


def load_session_secrets(client_id: str) -> Optional[dict[str, str]]:
    if not client_id:
        return None
    result = _run("get", client_id)
    if result.returncode != 0:
        return None
    try:
        payload = json.loads(result.stdout)
    except (TypeError, json.JSONDecodeError) as err:
        raise CredentialStoreError("Secure credential store returned invalid JSON.") from err
    required = ("client_secret", "access_token", "refresh_token")
    if any(not isinstance(payload.get(name), str) or not payload[name] for name in required):
        raise CredentialStoreError("Secure credential store returned an incomplete OAuth credential set.")
    return {name: payload[name] for name in required}


def delete_session_secrets(client_id: str) -> None:
    if client_id:
        _run("delete", client_id)
