import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { runInNewContext } from "node:vm";

const extensionUrl = new URL("../extensions/microsoft-foundry/extension.mjs", import.meta.url);
const source = readFileSync(extensionUrl, "utf8");
const marker = "// Security boundary: opening the canvas must never install or update global";
const markerOffset = source.indexOf(marker);
const licenseOffset = source.indexOf("/*! Bundled license information:", markerOffset);

assert.ok(markerOffset > 0, "security override must exist");
assert.ok(licenseOffset > markerOffset, "security override must precede bundled license trailer");
assert.ok(markerOffset > source.indexOf("main.tar.gz"), "override must run after legacy bundle initialization");

const securityBlock = source.slice(markerOffset, licenseOffset);
assert.match(securityBlock, /qX="";/);
assert.match(securityBlock, /Automatic global skill installation is disabled/);
assert.match(securityBlock, /CQ=async\(\)=>\{\};/);

const context = {
  qX: "https://mutable.example/main.tar.gz",
  YX: async () => {
    throw new Error("legacy installer executed");
  },
  nQ: async () => {
    throw new Error("legacy updater executed");
  },
  I$: async () => {
    throw new Error("legacy updater executed");
  },
  CQ: async () => {
    throw new Error("legacy canvas callback executed");
  },
};

runInNewContext(securityBlock, context);
assert.equal(context.qX, "", "mutable archive URL must be disabled");
assert.deepEqual(
  JSON.parse(JSON.stringify(await context.I$())),
  {
    ok: true,
    status: "plugin-managed",
    action: "none",
    changed: false,
    ready: true,
    summary: "Foundry Skills are managed by the installed plugin.",
  },
);
await context.CQ({ log: () => assert.fail("canvas open must not trigger update logging") });

console.log("PASS canvas open performs no automatic skill install/update");
