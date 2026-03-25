/**
 * Mobile Performance and UI Optimization
 * Handles responsive navigation and optimizes image loading 
 * to reduce bandwidth and improve site speed on mobile devices.
 */

document.addEventListener("DOMContentLoaded", () => {
    
    // Smooth mobile menu toggle
    const menuToggle = document.querySelector('.mobile-menu-btn');
    const navLayout = document.querySelector('.nav-layout');

    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            navLayout.classList.toggle('is-active');
            menuToggle.setAttribute('aria-expanded', navLayout.classList.contains('is-active'));
        });
    }

    // Lazy load heavy assets to improve initial load time
    const performanceImages = document.querySelectorAll('.lazy-image');
    
    const assetObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy-image');
                observer.unobserve(img);
            }
        });
    });

    performanceImages.forEach(img => assetObserver.observe(img));
});