// Loaded as a classic script before each page's module. If the page script fails to
// load, the usual cause is an outdated file in the browser cache next to a new one
// (2026-11-18: an old serial.js without serialSend stopped the Capture page). Chrome
// may keep such a file without asking the server for up to a day, and ignores
// Clear-Site-Data on http://127.0.0.1. So: re-download every file this page used,
// straight from the server (cache: "reload" also replaces the cached copy), then
// reload. At most MAX_TRIES per tab; after that, say what to do.
(function () {
  var MAX_TRIES = 2;
  var KEY = "prata-repair-tries";
  var repairing = false;

  function tries() {
    try { return Number(sessionStorage.getItem(KEY) || 0); } catch (e) { return MAX_TRIES; }
  }

  function show(text) {
    var el = document.getElementById("load-error");
    if (!el) return;
    el.hidden = false;
    el.textContent = text;
  }

  window.addEventListener("error", function (e) {
    if (window.prataLoaded || repairing) return;
    var n = tries();
    if (n >= MAX_TRIES) {
      show("This page failed to load (" + (e.message || "a file could not be fetched") +
        "). Reload it with Ctrl+Shift+R. If that does not help, restart the server.");
      return;
    }
    repairing = true;
    try { sessionStorage.setItem(KEY, String(n + 1)); } catch (err) { /* storage blocked */ }
    show("Updating outdated files in the browser cache, then reloading…");
    var site = location.origin + location.pathname.replace(/[^/]*$/, "");
    var urls = performance.getEntriesByType("resource")
      .map(function (r) { return r.name; })
      .filter(function (u) { return u.indexOf(site) === 0; });
    urls.push(location.href);
    Promise.all(urls.map(function (u) {
      return fetch(u, { cache: "reload" }).catch(function () {});
    })).then(function () { location.reload(); });
  }, true);

  window.addEventListener("load", function () {
    if (window.prataLoaded) {
      try { sessionStorage.removeItem(KEY); } catch (e) { /* ignore */ }
    }
  });
})();
