// ByronStatics nav — active state highlighting for in-page links
// When user clicks "Collection" (href="#products") or navigates to
// index.html#products from another page, highlight that nav link.

(function () {
  'use strict';

  // Add a small <style> block for the active state (matches the home link style)
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
    const collectionLinks = document.querySelectorAll('.nav-collection');
    collectionLinks.forEach(function (link) {
      // Active if hash is #products OR if we are on index.html and hash matches
      const isActive = hash === '#products';
      if (isActive) {
        link.classList.add('is-active');
      } else {
        link.classList.remove('is-active');
      }
    });
  }

  // Update on hash change
  window.addEventListener('hashchange', updateActive);
  // Initial check (handles page load with #products)
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateActive);
  } else {
    updateActive();
  }
})();
