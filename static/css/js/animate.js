// index animation carousel

$(document).ready(function() {
    function resetCaptions() {
        $(".carousel-caption p, .carousel-caption h1, .carousel-caption a").css({
            opacity: 0,
            position: "relative",
            top: "5px",
            left: "-5px",
            transform: "scale(0.9)",
            transition: "none"
        });
    }

    function animateCaption($caption) {
        const $p = $caption.find("p");
        const $h1 = $caption.find("h1");
        const $a = $caption.find("a");

        $p.animate({ opacity: 1, top: "10px" }, 600);

        $h1.delay(600).animate({ opacity: 1, left: "-20px" }, 800);

        $a.delay(1400).queue(function(next) {
            $(this).css({
                opacity: 1,
                transform: "scale(1)",
                transition: "transform 0.7s ease-in-out"
            });
            next();
        });
    }

    function animateCurrentSlide() {
        resetCaptions();
        const $activeCaption = $(".carousel-item.active .carousel-caption");
        animateCaption($activeCaption);
    }

    animateCurrentSlide();

    $('#mainCarousel').on('slid.bs.carousel', function() {
        animateCurrentSlide();
    });
});




document.addEventListener("DOMContentLoaded", function() {
    const filterLinks = document.querySelectorAll(".nav-link[data-filter]");
    const products = document.querySelectorAll("[data-category]");

    filterLinks.forEach(link => {
        link.addEventListener("click", function(e) {
            e.preventDefault();
            filterLinks.forEach(l => l.classList.remove("active"));
            this.classList.add("active");

            const filterValue = this.getAttribute("data-filter");

            products.forEach(product => {
                const category = product.getAttribute("data-category");
                if (filterValue === "all" || category === filterValue) {
                    product.style.display = "block";
                } else {
                    product.style.display = "none";
                }
            });
        });
    });
});





const navLinks = document.querySelectorAll(".nav-link");
const productItems = document.querySelectorAll("[data-category]");

navLinks.forEach(link => {
    link.addEventListener("click", function(e) {
        e.preventDefault();

        // Toggle active class
        navLinks.forEach(link => link.classList.remove("active"));
        this.classList.add("active");

        const filter = this.getAttribute("data-filter");

        productItems.forEach(item => {
            const category = item.getAttribute("data-category");
            if (filter === "all" || category === filter) {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        });
    });
});



document.addEventListener("DOMContentLoaded", function() {
    const isLoggedIn = localStorage.getItem("isLoggedIn");

    if (isLoggedIn === "true") {
        document.querySelectorAll(".after-login").forEach(el => el.style.display = "inline-block");
        document.querySelectorAll(".before-login").forEach(el => el.style.display = "none");
    } else {
        document.querySelectorAll(".after-login").forEach(el => el.style.display = "none");
        document.querySelectorAll(".before-login").forEach(el => el.style.display = "inline-block");
    }
});



document.addEventListener('DOMContentLoaded', function() {
    const loginLinkLi = document.getElementById('login-link-li');
    const registerLinkLi = document.getElementById('register-link-li');
    const profileDropdownLi = document.getElementById('profile-dropdown-li');
    const logoutLinkLi = document.getElementById('logout-link-li');

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }

    const usernameCookie = getCookie('user');

    if (usernameCookie) {
        // User is logged in
        loginLinkLi.classList.add('d-none'); // Hide Login
        registerLinkLi.classList.add('d-none'); // Hide Register
        profileDropdownLi.classList.remove('d-none'); // Show Profile
        logoutLinkLi.classList.remove('d-none'); // Show Logout
    } else {
        // User is not logged in
        loginLinkLi.classList.remove('d-none'); // Show Login
        registerLinkLi.classList.remove('d-none'); // Show Register
        profileDropdownLi.classList.add('d-none'); // Hide Profile
        logoutLinkLi.classList.add('d-none'); // Hide Logout
    }

    // --- Product filtering logic (keep existing) ---
    const filterLinks = document.querySelectorAll('.nav-link[data-filter]');
    const productList = document.getElementById('product-list');

    filterLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            filterLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');

            const filter = this.dataset.filter;
            const products = productList.children;

            for (let i = 0; i < products.length; i++) {
                const product = products[i];
                const category = product.dataset.category;

                if (filter === 'all' || filter === category) {
                    product.style.display = 'block';
                } else {
                    product.style.display = 'none';
                }
            }
        });
    });

    // "Load More" button logic (keep existing)
    const loadMoreButton = document.querySelector('.load-more-btn');
    if (loadMoreButton) {
        loadMoreButton.addEventListener('click', function() {
            alert('More products would be loaded here in a real application!');
            this.style.display = 'none'; // Just hide for demonstration
        });
    }
});