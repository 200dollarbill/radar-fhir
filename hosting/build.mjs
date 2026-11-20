// Builds the Worker's static assets: website/ is copied to public/capture/
// (the address the pages already use), plus Cloudflare's _headers and
// _redirects files. Run: node build.mjs
import { cp, rm, writeFile } from "node:fs/promises";
import { join, relative, dirname, sep } from "node:path";
import { fileURLToPath } from "node:url";

export const HEADERS = `/*
  Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline'
  Permissions-Policy: serial=(self)
  X-Frame-Options: DENY
  Referrer-Policy: no-referrer
  Strict-Transport-Security: max-age=31536000
  X-Content-Type-Options: nosniff
`;

export const REDIRECTS = "/ /capture/sessions.html 302\n";

// Top-level website entries that are not part of the site.
const LEFT_OUT = new Set(["tests", "eval", "package.json", "node_modules"]);

export async function build({ websiteDir, outDir }) {
  await rm(outDir, { recursive: true, force: true });
  await cp(websiteDir, join(outDir, "capture"), {
    recursive: true,
    filter: (src) => {
      const top = relative(websiteDir, src).split(sep)[0];
      return !LEFT_OUT.has(top);
    },
  });
  await writeFile(join(outDir, "_headers"), HEADERS);
  await writeFile(join(outDir, "_redirects"), REDIRECTS);
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const here = dirname(fileURLToPath(import.meta.url));
  await build({ websiteDir: join(here, "..", "website"), outDir: join(here, "public") });
  console.log("built hosting/public");
}
