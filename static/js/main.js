// Navbar scroll effect
window.addEventListener('scroll', function() {
    const navbar = document.getElementById('mainNavbar');
    if (window.scrollY > 50) {
        navbar.classList.add('navbar-scrolled');
    } else {
        navbar.classList.remove('navbar-scrolled');
    }
});

// Carousel animation handling (only if mainCarousel exists)
window.onload = function() {
    const activeCaption = document.querySelector(".carousel-item.active .animated-caption");
    if (activeCaption) {
        activeCaption.classList.add("show");
    }

    const carousel = document.getElementById("mainCarousel");
    if (carousel) {
        carousel.addEventListener("slide.bs.carousel", function() {
            document.querySelectorAll(".animated-caption").forEach(caption => {
                caption.classList.remove("show");
            });
        });

        carousel.addEventListener("slid.bs.carousel", function() {
            const current = document.querySelector(".carousel-item.active .animated-caption");
            if (current) {
                current.classList.add("show");
            }
        });
    }
};