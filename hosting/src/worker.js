// PRATA's public front door. Static pages are served by Workers static assets
// without running this code. Everything else (API calls, and any address that
// is not a page) runs here: API calls under /auth/, /api/ and /fhir-r4/ are
// forwarded to the server on the owner's laptop through the Workers VPC
// binding LAPTOP; anything else gets 404 and never reaches the laptop.

export function outcome(status, code, text, headers = {}) {
  const body = { resourceType: "OperationOutcome", issue: [{ severity: "error", code, details: { text } }] };
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/fhir+json", "X-Content-Type-Options": "nosniff", ...headers },
  });
}

const API = /^\/(auth|api|fhir-r4)\//;
const ADMIN = /^\/fhir-r4\/v1\/admin(\/|$)/;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // The server routes on the percent-decoded path, so every check here uses
    // it too (otherwise /fhir-r4/v1/admin%2Faccounts would slip past).
    let path;
    try {
      path = decodeURIComponent(url.pathname);
    } catch {
      return outcome(400, "invalid", "Malformed address.");
    }

    // Account management stays on the laptop's command line.
    if (ADMIN.test(path)) {
      return outcome(403, "forbidden", "Account management is only available on the PRATA laptop.");
    }
    if (!API.test(path)) {
      return outcome(404, "not-found", "Not found.");
    }

    if (request.method === "POST" && path === "/auth/token") {
      const key = request.headers.get("CF-Connecting-IP") ?? "unknown";
      const { success } = await env.LOGIN_LIMIT.limit({ key });
      if (!success) {
        return outcome(429, "throttled", "Too many login attempts. Try again in a minute.", { "Retry-After": "60" });
      }
    }

    // Same method, path, query, headers and (streamed) body; the site uses no
    // cookies. X-PRATA-Public tells the server this came from the internet, so
    // it refuses account management even if a path trick got past this file.
    const forward = new Request("http://127.0.0.1" + url.pathname + url.search, request);
    forward.headers.delete("cookie");
    forward.headers.set("X-PRATA-Public", "1");

    let res;
    try {
      res = await env.LAPTOP.fetch(forward);
    } catch {
      return outcome(503, "transient", "PRATA server is offline (laptop off or tunnel down).", { "Retry-After": "30" });
    }
    const out = new Response(res.body, res);
    out.headers.set("X-Content-Type-Options", "nosniff");
    return out;
  },
};
