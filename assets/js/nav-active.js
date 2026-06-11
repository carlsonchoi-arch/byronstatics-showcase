// ByronStatics nav — exclusive active state for Home vs Collection
// Only ONE of Home/Collection can be active at a time. Importantly,
// the logo link is EXCLUDED — only nav links are mutated.

(function () {
  'use strict';

  // Inline style for Collection active state (matches Home's wavy underline)
  const style = document.createElement('style');
  style.textContent = `
    .nav-collection.is-active {
      color: #E9C46A; /* mustard */
      text-decoration: underline;
      text-decoration-style: wavy;
      text-decoration-thickness: 2px;
      text-underline-offset: 4px;
    }
  `;
  document.head.appendChild(style);

  // Active class string for the Home nav link
  const ACTIVE_CLASSES = ['text-mustard', 'underline', 'decoration-wavy', 'decoration-2', 'underline-offset-4'];
  // Inactive class string (default state)
  const INACTIVE_CLASSES = ['hover:text-mustard', 'transition'];

  // Get ONLY the nav Home link, not the logo or footer links
  function getNavHomeLink() {
    // Specifically target the nav element's Home link
    const navs = document.querySelectorAll('header nav');
    for (const nav of navs) {
      const homeLink = nav.querySelector('a[href$="index.html"]');
      if (homeLink) return homeLink;
    }
    return null;
  }

  function getNavCollectionLinks() {
    return document.querySelectorAll('header nav .nav-collection');
  }

  function setHomeActive(homeLink, active) {
    if (!homeLink) return;
    ACTIVE_CLASSES.forEach(function (c) { homeLink.classList.toggle(c, active); });
    INACTIVE_CLASSES.forEach(function (c) { homeLink.classList.toggle(c, !active); });
  }

  function setCollectionActive(links, active) {
    links.forEach(function (link) {
      link.classList.toggle('is-active', active);
    });
  }

  function updateActive() {
    const hash = window.location.hash;
    const onIndexPage = window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || window.location.pathname.endsWith('/');
    const collectionIsActive = (hash === '#products') && onIndexPage;

    const homeLink = getNavHomeLink();
    const collectionLinks = getNavCollectionLinks();

    if (collectionIsActive) {
      setHomeActive(homeLink, false);
      setCollectionActive(collectionLinks, true);
    } else {
      setHomeActive(homeLink, true);
      setCollectionActive(collectionLinks, false);
    }
  }

  // When user clicks the Home nav link, navigate to index.html and reset hash
  document.addEventListener('click', function (e) {
    const link = e.target.closest('header nav a[href$="index.html"]');
    if (link) {
      // If we're on the index page, just clear the hash
      if (window.location.pathname.endsWith('index.html') || window.location.pathname.endsWith('/')) {
        if (window.location.hash) {
          e.preventDefault();
          history.pushState(null, '', 'index.html');
          updateActive();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      }
    }
  });

  // Update on hash change
  window.addEventListener('hashchange', updateActive);
  // Update when page becomes visible (back/forward navigation)
  window.addEventListener('pageshow', updateActive);

  // Initial check
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateActive);
  } else {
    updateActive();
  }
})();
