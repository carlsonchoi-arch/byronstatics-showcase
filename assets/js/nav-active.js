// ByronStatics nav — exclusive active state for Home vs Collection
// Only ONE of Home/Collection can be active at a time:
//   - On home page (no hash): Home is active
//   - After clicking Collection (hash = #products): Collection is active, Home goes inactive

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

  function updateActive() {
    const hash = window.location.hash;
    const homeLinks = document.querySelectorAll('a[href$="index.html"]');
    const collectionLinks = document.querySelectorAll('.nav-collection');
    // active = (hash === '#products')
    const collectionIsActive = (hash === '#products');

    // Reset all Home links to inactive class
    homeLinks.forEach(function (link) {
      // Remove the Home-active classes
      link.classList.remove(
        'text-mustard',
        'underline',
        'decoration-wavy',
        'decoration-2',
        'underline-offset-4'
      );
      // Add the inactive (default) class
      if (!link.classList.contains('hover:text-mustard')) {
        link.classList.add('hover:text-mustard', 'transition');
      }
    });

    // If Collection is active, set it; otherwise set Home
    if (collectionIsActive) {
      // Collection is active, Home already reset to inactive above
      collectionLinks.forEach(function (link) {
        link.classList.add('is-active');
        // Add a click listener so clicking it makes Home inactive immediately
      });
    } else {
      // Home should be active
      homeLinks.forEach(function (link) {
        link.classList.add(
          'text-mustard',
          'underline',
          'decoration-wavy',
          'decoration-2',
          'underline-offset-4'
        );
      });
      collectionLinks.forEach(function (link) {
        link.classList.remove('is-active');
      });
    }
  }

  // Click handlers: when Collection is clicked, prevent Home from staying active
  document.addEventListener('click', function (e) {
    const link = e.target.closest('.nav-collection');
    if (link) {
      // Defer to allow hash change to fire first
      setTimeout(updateActive, 10);
    }
  });

  // Update on hash change
  window.addEventListener('hashchange', updateActive);
  // Initial check
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateActive);
  } else {
    updateActive();
  }
})();
