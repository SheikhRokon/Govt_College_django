// toggle menu
let isMenuOpen = 0;
const mobileBtn = document.querySelector("#menubtn");
const mobileMenu = document.querySelector("#mobilemenu");
mobileBtn.addEventListener("click", () => {
  mobileMenu.style.display = "block";
  isMenuOpen++;
  if (isMenuOpen % 2 == 0) {
    mobileMenu.style.display = "none";
  }
});

// slider
let currentSlide = 0;
const slides = document.querySelectorAll(".slide");

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.style.display = i === index ? "block" : "none";
  });
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % slides.length;
  showSlide(currentSlide);
}

showSlide(currentSlide);

setInterval(nextSlide, 4000);
