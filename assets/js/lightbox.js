// ByronStatics lightbox — click any product image to view full size
// Works for both hero images and thumbnails on product pages.
(function () {
  'use strict';

  // Build modal once
  const modal = document.createElement('div');
  modal.id = 'bs-lightbox';
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-modal', 'true');
  modal.innerHTML = `
    <style>
      #bs-lightbox {
        position: fixed; inset: 0; z-index: 9999;
        background: rgba(0, 0, 0, 0.85);
        display: none; align-items: center; justify-content: center;
        padding: 24px; cursor: zoom-out;
      }
      #bs-lightbox.open { display: flex; }
      #bs-lightbox img {
        max-width: 92vw; max-height: 92vh;
        object-fit: contain; border-radius: 12px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.5);
        background: #fff;
      }
      #bs-lightbox .bs-close {
        position: absolute; top: 16px; right: 20px;
        color: #fff; font-size: 36px; font-weight: 300;
        background: none; border: none; cursor: pointer;
        line-height: 1; padding: 4px 12px;
        opacity: 0.85; transition: opacity .2s;
      }
      #bs-lightbox .bs-close:hover { opacity: 1; }
      #bs-lightbox .bs-caption {
        position: absolute; bottom: 24px; left: 0; right: 0;
        text-align: center; color: #fff; font-size: 14px;
        opacity: 0.85; font-family: 'Inter', system-ui, sans-serif;
      }
    </style>
    <button class="bs-close" aria-label="Close">&times;</button>
    <img alt="">
    <div class="bs-caption"></div>
  `;
  document.body.appendChild(modal);

  const lbImg = modal.querySelector('img');
  const lbCap = modal.querySelector('.bs-caption');
  const lbClose = modal.querySelector('.bs-close');

  function open(src, alt) {
    lbImg.src = src;
    lbImg.alt = alt || '';
    lbCap.textContent = alt || '';
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function close() {
    modal.classList.remove('open');
    document.body.style.overflow = '';
    lbImg.src = '';
  }

  modal.addEventListener('click', function (e) {
    if (e.target === modal || e.target === lbClose) close();
  });
  lbClose.addEventListener('click', close);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modal.classList.contains('open')) close();
  });

  // Wire up all product page images on DOM ready
  function wire() {
    // Hero image
    const heroWrap = document.querySelector('.aspect-square.bg-white.rounded-2xl');
    if (heroWrap) {
      const heroImg = heroWrap.querySelector('img');
      if (heroImg) {
        heroImg.style.cursor = 'zoom-in';
        heroImg.addEventListener('click', function () {
          open(heroImg.src, heroImg.alt);
        });
      }
    }
    // Thumbnails
    const thumbs = document.querySelectorAll('.grid.grid-cols-3 img');
    thumbs.forEach(function (img) {
      img.style.cursor = 'zoom-in';
      img.addEventListener('click', function () {
        open(img.src, img.alt);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wire);
  } else {
    wire();
  }
})();
