import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).parents[1] / "skills" / "launch-with-aws" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import auth
import credential_store
from launch_config import StoredSession


def session() -> StoredSession:
    return StoredSession(
        client_id="client-id",
        client_secret="client-secret-value",
        client_expires_at=4_000_000_000,
        authorize_endpoint="https://oidc.us-east-1.amazonaws.com/authorize",
        token_endpoint="https://oidc.us-east-1.amazonaws.com/token",
        scopes=["launch:access"],
        access_token="access-token-value",
        refresh_token="refresh-token-value",
        token_expires_at=4_000_000_000,
    )


class CredentialStorageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.session_dir_patch = patch.object(auth, "SESSION_DIR", self.temp_dir.name)
        self.session_dir_patch.start()
        self.addCleanup(self.session_dir_patch.stop)

    def test_metadata_serialization_excludes_all_secret_values(self) -> None:
        text = session().to_metadata_json()
        payload = json.loads(text)
        self.assertEqual(payload["credential_store"], "os-keyring")
        for name in ("client_secret", "access_token", "refresh_token"):
            self.assertNotIn(name, payload)
        for value in ("client-secret-value", "access-token-value", "refresh-token-value"):
            self.assertNotIn(value, text)

    def test_save_and_load_use_secure_store_and_safe_metadata(self) -> None:
        value = session()
        secrets = {
            "client_secret": value.client_secret,
            "access_token": value.access_token,
            "refresh_token": value.refresh_token,
        }
        with patch.object(auth, "store_session_secrets") as store, patch.object(
            auth, "load_session_secrets", return_value=secrets
        ):
            auth.save_session(value)
            loaded = auth.load_session()
        store.assert_called_once_with(value.client_id, secrets)
        self.assertEqual(loaded, value)
        disk_text = Path(auth._session_file()).read_text()
        self.assertNotIn("client-secret-value", disk_text)
        self.assertNotIn("access-token-value", disk_text)
        self.assertNotIn("refresh-token-value", disk_text)

    def test_legacy_plaintext_is_scrubbed_when_keychain_write_fails(self) -> None:
        path = Path(auth._session_file())
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value := session().__dict__))
        error = credential_store.CredentialStoreError("keychain unavailable")
        with patch.object(auth, "store_session_secrets", side_effect=error):
            with self.assertRaisesRegex(credential_store.CredentialStoreError, "keychain unavailable"):
                auth.load_session()
        disk_text = path.read_text()
        for name in ("client_secret", "access_token", "refresh_token"):
            self.assertNotIn(name, json.loads(disk_text))
        for secret_value in (value["client_secret"], value["access_token"], value["refresh_token"]):
            self.assertNotIn(secret_value, disk_text)

    def test_logout_removes_secure_item_and_metadata(self) -> None:
        path = Path(auth._session_file())
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(session().to_metadata_json())
        with patch.object(auth, "delete_session_secrets") as delete:
            auth.clear_session()
        delete.assert_called_once_with("client-id")
        self.assertFalse(path.exists())

    def test_keychain_store_sends_secret_on_stdin_not_argv(self) -> None:
        completed = __import__("subprocess").CompletedProcess([], 0, "", "")
        with patch.object(credential_store.sys, "platform", "darwin"), patch.object(
            credential_store, "_store_keychain", return_value=completed
        ) as store:
            credential_store.store_session_secrets(
                "client-id",
                {
                    "client_secret": "client-secret-value",
                    "access_token": "access-token-value",
                    "refresh_token": "refresh-token-value",
                },
            )
        command, stdin_payload = store.call_args.args
        self.assertNotIn("client-secret-value", command)
        self.assertNotIn("access-token-value", command)
        self.assertNotIn("refresh-token-value", command)
        self.assertIn("client-secret-value", stdin_payload)


if __name__ == "__main__":
    unittest.main()
