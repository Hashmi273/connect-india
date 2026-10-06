// ==========================================================================
// CONNECT INDIA — EXACT EVENTBEDS INTERACTION ENGINE
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {

    // --- 1. PIN INTERACTION & PHONE SCREEN CYCLER ---
    const pins = document.querySelectorAll('.eb-pin-item');
    const feedCards = document.querySelectorAll('.feed-card');

    pins.forEach(pin => {
        pin.addEventListener('click', () => {
            const ch = pin.dataset.ch;
            
            // Highlight pin
            pins.forEach(p => p.classList.remove('active'));
            pin.classList.add('active');

            // Switch phone feed card
            feedCards.forEach(c => {
                c.classList.remove('active');
                if (c.dataset.feed === ch) {
                    c.classList.add('active');
                }
            });
        });
    });

    // Auto cycle feed cards in center phone every 3 seconds
    let currentFeedIdx = 0;
    if (feedCards.length > 0) {
        setInterval(() => {
            currentFeedIdx = (currentFeedIdx + 1) % feedCards.length;
            feedCards.forEach((c, idx) => {
                c.classList.toggle('active', idx === currentFeedIdx);
            });
        }, 3200);
    }

    // --- 2. TOP NAV SCROLL SHADOW & BACK TO TOP ---
    const topNav = document.getElementById('topNav');
    const ebScrollTop = document.getElementById('ebScrollTop');

    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        
        if (scrollY > 50) {
            topNav.style.boxShadow = '0 4px 20px rgba(0,0,0,0.06)';
            topNav.style.background = 'rgba(255, 255, 255, 0.98)';
        } else {
            topNav.style.boxShadow = 'none';
            topNav.style.background = 'rgba(245, 247, 250, 0.9)';
        }

        if (scrollY > 600) {
            ebScrollTop.classList.add('visible');
        } else {
            ebScrollTop.classList.remove('visible');
        }
    });

    if (ebScrollTop) {
        ebScrollTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // --- 3. LEAD FORM DISPATCH ---
    const leadForm = document.getElementById('leadForm');
    if (leadForm) {
        leadForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = leadForm.querySelector('button[type="submit"] .btn-text-main');
            const originalText = btn.textContent;

            btn.textContent = 'Allocating Sandbox...';

            setTimeout(() => {
                btn.textContent = '✓ Access Request Sent!';
                leadForm.reset();
                setTimeout(() => {
                    btn.textContent = originalText;
                }, 3000);
            }, 1200);
        });
    }

});
