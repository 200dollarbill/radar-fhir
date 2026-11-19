// PRATA's public front door. Static pages are served by Workers static assets
// and never reach this code; only /auth/*, /api/* and /fhir-r4/* do
// (wrangler.jsonc run_worker_first). Those are forwarded to the server on the
// owner's laptop through the Workers VPC binding LAPTOP.

export function outcome(status, code, text, headers = {}) {
  const body = { resourceType: "OperationOutcome", issue: [{ severity: "error", code, details: { text } }] };
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/fhir+json", "X-Content-Type-Options": "nosniff", ...headers },
  });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Account management stays on the laptop's command line.
    if (url.pathname.startsWith("/fhir-r4/v1/admin/")) {
      return outcome(403, "forbidden", "Account management is only available on the PRATA laptop.");
    }

    if (request.method === "POST" && url.pathname === "/auth/token") {
      const key = request.headers.get("CF-Connecting-IP") ?? "unknown";
      const { success } = await env.LOGIN_LIMIT.limit({ key });
      if (!success) {
        return outcome(429, "throttled", "Too many login attempts. Try again in a minute.", { "Retry-After": "60" });
      }
    }

    // Same method, path, query, headers and (streamed) body; the site uses no cookies.
    const forward = new Request("http://127.0.0.1" + url.pathname + url.search, request);
    forward.headers.delete("cookie");

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
