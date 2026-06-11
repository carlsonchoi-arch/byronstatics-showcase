// ByronStatics nav active state
// Toggles `is-nav-active` class on <a data-nav="..."> inside <header> based on URL.
// Source of truth: pathname + hash + data-nav attribute (NO inline active class).
//
// Active rule:
//   /, /index, /index.html                        → data-nav="home" (or "collection" if hash === "#products")
//   /about, /about.html, /about/                  → data-nav="story"
//   /contact, /contact.html, /contact/            → data-nav="sayhi"
//   /products/*                                   → no active link
//
// Cloudflare Pages serves .html files but URLs can appear without extension; match both.

(function () {
  function getActiveKey() {
    var path = window.location.pathname || '/';
    var hash = window.location.hash;

    // Strip trailing slash for comparison (but keep '/' as is).
    var normalized = path;
    if (normalized.length > 1 && normalized.charAt(normalized.length - 1) === '/') {
      normalized = normalized.slice(0, -1);
    }

    // about / The Story  (match /about, /about/, /about.html)
    if (normalized === '/about' || normalized.indexOf('/about.') !== -1) return 'story';

    // contact / Say Hi  (match /contact, /contact/, /contact.html)
    if (normalized === '/contact' || normalized.indexOf('/contact.') !== -1) return 'sayhi';

    // home / collection
    if (normalized === '' || normalized === '/' ||
        normalized === '/index' || normalized.indexOf('/index.') !== -1) {
      return hash === '#products' ? 'collection' : 'home';
    }

    // /products/* → no active
    return null;
  }

  function apply() {
    var activeKey = getActiveKey();
    var navLinks = document.querySelectorAll('header nav a[data-nav]');
    navLinks.forEach(function (link) {
      var key = link.getAttribute('data-nav');
      if (activeKey && key === activeKey) {
        link.classList.add('is-nav-active');
      } else {
        link.classList.remove('is-nav-active');
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', apply);
  } else {
    apply();
  }
  window.addEventListener('hashchange', apply);
  window.addEventListener('popstate', apply);
})();
