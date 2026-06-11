// ByronStatics nav — data-driven active state
// Each nav link has data-nav="home|collection|story|sayhi"
// JS determines which is active based on the current page.

(function () {
  'use strict';

  // Style for the active state (mustard + wavy underline, matches original design)
  const style = document.createElement('style');
  style.textContent = `
    .is-nav-active {
      color: #E9C46A !important; /* mustard */
      text-decoration: underline !important;
      text-decoration-style: wavy !important;
      text-decoration-thickness: 2px !important;
      text-underline-offset: 4px !important;
    }
  `;
  document.head.appendChild(style);

  // Map pathname → which data-nav value should be active
  function getActiveKey() {
    const path = window.location.pathname;
    if (path.endsWith('about.html')) return 'story';
    if (path.endsWith('contact.html')) return 'sayhi';
    // index.html or root
    if (path.endsWith('index.html') || path.endsWith('/') || path === '') {
      // On index, if hash is #products, Collection is active; otherwise Home
      if (window.location.hash === '#products') return 'collection';
      return 'home';
    }
    // products/* or any other path
    return null;
  }

  function updateActive() {
    const activeKey = getActiveKey();
    // Only operate on links inside the header nav
    const navLinks = document.querySelectorAll('header nav a[data-nav]');
    navLinks.forEach(function (link) {
      const key = link.getAttribute('data-nav');
      if (key === activeKey) {
        link.classList.add('is-nav-active');
      } else {
        link.classList.remove('is-nav-active');
      }
    });
  }

  // When user clicks the Home nav link while on index.html with #products hash,
  // clear the hash so the active state goes from Collection back to Home
  document.addEventListener('click', function (e) {
    const link = e.target.closest('header nav a[data-nav]');
    if (!link) return;
    const key = link.getAttribute('data-nav');
    const path = window.location.pathname;
    const isIndex = path.endsWith('index.html') || path.endsWith('/');
    
    if (key === 'home' && isIndex && window.location.hash) {
      e.preventDefault();
      history.pushState(null, '', 'index.html');
      updateActive();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (key === 'collection' && isIndex) {
      // Let the hash change naturally, then update
      setTimeout(updateActive, 10);
    }
  });

  window.addEventListener('hashchange', updateActive);
  window.addEventListener('pageshow', updateActive);
  window.addEventListener('popstate', updateActive);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateActive);
  } else {
    updateActive();
  }
})();
