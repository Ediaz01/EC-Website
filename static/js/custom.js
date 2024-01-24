// To add the active class to the links in the navbar after clicking on then

// document.addEventListener("DOMContentLoaded", (event) => {
//   var navLinks = document.querySelectorAll(".navbar-nav .nav-link");
//   var windowPathname = window.location.pathname;

//   // Now you can work with your links
//   navLinks.forEach((link) => {
//     const navLinkPathname = new URL(link.href).pathname;

//     if (windowPathname === navLinkPathname) {
//       link.classList.add("active");
//     }
//   });
// });

// Mobile Menu - From first website
document.addEventListener("DOMContentLoaded", () => {
  const hamburgerButton = document.querySelector(".hamburger-button");
  const mobileMenu = document.querySelector(".mobile-menu");

  hamburgerButton.addEventListener("click", () =>
    mobileMenu.classList.toggle("active")
  );
});

window.addEventListener("resize", function () {
  var mobMenu = document.querySelector(".mobile-menu"); // Replace with your menu's ID
  var width = window.innerWidth;

  if (width >= 670) {
    // Same breakpoint as in CSS
    mobMenu.classList.remove("active");
    // or mobileMenu.style.display = "none"; // or 'flex', 'grid', etc. depending on your layout
  }
});

// Detect when the user scrolls down
window.onscroll = function () {
  var header = document.querySelector(".header");
  if (window.scrollY > 0) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
};
