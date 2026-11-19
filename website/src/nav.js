// The top bar shared by every page.

const PAGES = [
  { href: "sessions.html", label: "Sessions", files: ["sessions.html"] },
  { href: "./", label: "Capture", files: ["", "index.html"] },
  { href: "review.html", label: "Review", files: ["review.html"] },
];

export function navItems(path) {
  const file = String(path).split("/").pop();
  return PAGES.map(({ href, label, files }) => ({ href, label, current: files.includes(file) }));
}

export function userLabel(auth) {
  return auth ? `${auth.username} (${auth.role})` : null;
}

// el: the <nav> element. onLogout runs after the stored login is cleared.
export function renderNav(el, { path, auth, onLogout }) {
  const doc = el.ownerDocument;
  el.replaceChildren();
  const brand = doc.createElement("span");
  brand.className = "brand";
  brand.textContent = "PRATA";
  const list = doc.createElement("ul");
  for (const item of navItems(path)) {
    const li = doc.createElement("li");
    const a = doc.createElement("a");
    a.href = item.href;
    a.textContent = item.label;
    if (item.current) a.setAttribute("aria-current", "page");
    li.append(a);
    list.append(li);
  }
  const user = doc.createElement("span");
  user.className = "user";
  const label = userLabel(auth);
  if (label) {
    const who = doc.createElement("span");
    who.textContent = label;
    const out = doc.createElement("button");
    out.type = "button";
    out.className = "link";
    out.textContent = "Log out";
    out.addEventListener("click", () => onLogout?.());
    user.append(who, " · ", out);
  } else {
    const a = doc.createElement("a");
    a.href = "sessions.html";
    a.textContent = "Log in";
    user.append(a);
  }
  el.append(brand, list, user);
}
