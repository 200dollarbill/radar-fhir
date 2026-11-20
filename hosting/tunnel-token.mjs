// Puts the prata-laptop tunnel's token into .env/prata.env, using your
// wrangler login. The token is never printed. Run: make tunnel-token
import { execFileSync } from "node:child_process";
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const TUNNEL = "prata-laptop";
const NAME = "CLOUDFLARE_TUNNEL_TOKEN";

// Replace the `export name=...` line, or add one; other lines stay as they are.
export function setEnvLine(text, name, value) {
  const line = `export ${name}=${value}`;
  const lines = text.split("\n");
  if (lines.at(-1) === "") lines.pop();
  const at = lines.findIndex((l) => l.startsWith(`export ${name}=`));
  if (at >= 0) lines[at] = line; else lines.push(line);
  return lines.join("\n") + "\n";
}

async function main() {
  const here = dirname(fileURLToPath(import.meta.url));
  const envFile = join(here, "..", ".env", "prata.env");
  if (!existsSync(envFile)) throw new Error(".env/prata.env does not exist: make it first (README.md, Start here)");

  let auth;
  try {
    auth = JSON.parse(execFileSync("npx", ["wrangler", "auth", "token", "--json"], { cwd: here, stdio: ["ignore", "pipe", "ignore"] }).toString());
  } catch {
    throw new Error("not logged in to Cloudflare: run `cd hosting && npx wrangler login` first");
  }
  const bearer = auth.token ?? auth.apiToken ?? auth.oauthToken;
  if (!bearer) throw new Error("wrangler gave no token (an API key login is not supported here)");

  const api = async (path) => {
    const res = await fetch(`https://api.cloudflare.com/client/v4${path}`, { headers: { Authorization: `Bearer ${bearer}` } });
    const body = await res.json();
    if (!body.success) throw new Error(`Cloudflare API answered HTTP ${res.status}: ${JSON.stringify(body.errors)}`);
    return body.result;
  };
  const accounts = await api("/accounts");
  const account = process.env.CLOUDFLARE_ACCOUNT_ID ?? (accounts.length === 1 ? accounts[0].id : null);
  if (!account) throw new Error(`${accounts.length} Cloudflare accounts: set CLOUDFLARE_ACCOUNT_ID to choose one`);
  const [tunnel] = await api(`/accounts/${account}/cfd_tunnel?name=${TUNNEL}&is_deleted=false`);
  if (!tunnel) throw new Error(`no tunnel named ${TUNNEL} in this account`);
  const token = await api(`/accounts/${account}/cfd_tunnel/${tunnel.id}/token`);

  writeFileSync(envFile, setEnvLine(readFileSync(envFile, "utf8"), NAME, token));
  console.log(`wrote ${NAME} for tunnel ${TUNNEL} (${tunnel.id}) to .env/prata.env`);
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  main().catch((e) => { console.error(e.message); process.exit(1); });
}
