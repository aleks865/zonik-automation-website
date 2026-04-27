function openLightbox(image) {
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightbox-img");

  lightbox.style.display = "flex";
  lightboxImg.src = image.src;
  lightboxImg.alt = image.alt;
}

function closeLightbox() {
  const lightbox = document.getElementById("lightbox");
  lightbox.style.display = "none";
}

const revealElements = document.querySelectorAll(".reveal");

function revealOnScroll() {
  const windowHeight = window.innerHeight;

  revealElements.forEach((element) => {
    const elementTop = element.getBoundingClientRect().top;

    if (elementTop < windowHeight - 80) {
      element.classList.add("active");
    }
  });
}

window.addEventListener("scroll", revealOnScroll);
window.addEventListener("load", revealOnScroll);

const menuToggle = document.querySelector(".menu-toggle");
const nav = document.querySelector("nav");
const navLinks = document.querySelectorAll("nav a");
const sections = document.querySelectorAll("section[id]");

if (menuToggle) {
  menuToggle.addEventListener("click", () => {
    nav.classList.toggle("open");
  });
}

navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    nav.classList.remove("open");
  });
});

function setActiveLink() {
  let currentSection = "";

  sections.forEach((section) => {
    const sectionTop = section.offsetTop - 140;
    const sectionHeight = section.offsetHeight;

    if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
      currentSection = section.getAttribute("id");
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove("active");

    if (link.getAttribute("href") === `#${currentSection}`) {
      link.classList.add("active");
    }
  });
}

window.addEventListener("scroll", setActiveLink);
window.addEventListener("load", setActiveLink);

const contactForm = document.getElementById("contact-form");
const formMessage = document.getElementById("form-message");

if (contactForm && formMessage) {
  const emailInput = document.getElementById("email");
  const messageInput = document.getElementById("message");

  contactForm.addEventListener("submit", (event) => {
    event.preventDefault();

    formMessage.textContent = "";
    formMessage.style.color = "#dc2626";

    const emailValue = emailInput.value.trim();
    const messageValue = messageInput.value.trim();

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

    if (emailValue === "") {
      formMessage.textContent = "Wpisz adres e-mail.";
      emailInput.focus();
      return;
    }

    if (!emailPattern.test(emailValue)) {
      formMessage.textContent = "Wpisz poprawny adres e-mail.";
      emailInput.focus();
      return;
    }

    if (messageValue === "") {
      formMessage.textContent = "Opisz zakres prac lub treść zapytania.";
      messageInput.focus();
      return;
    }

    formMessage.style.color = "#2563eb";
    formMessage.textContent = "Dziękujemy za wiadomość. Formularz został poprawnie wypełniony.";
    contactForm.reset();
  });
}

const testimonialsSwiper = new Swiper(".testimonials-slider", {
  loop: true,
  spaceBetween: 24,
  grabCursor: true,
  simulateTouch: true,
  allowTouchMove: true,
  touchRatio: 1.2,
  shortSwipes: true,
  longSwipes: true,
  mousewheel: {
    forceToAxis: true,
  },
  keyboard: {
    enabled: true,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    1024: {
      slidesPerView: 2,
    }
  }
});

const portfolioSwiper = new Swiper(".portfolio-slider", {
  loop: true,
  spaceBetween: 56,
  grabCursor: true,
  simulateTouch: true,
  allowTouchMove: true,
  touchRatio: 1.2,
  shortSwipes: true,
  longSwipes: true,
  mousewheel: {
    forceToAxis: true,
  },
  keyboard: {
    enabled: true,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1200: {
      slidesPerView: 3,
    }
  }
});
const blogSwiper = new Swiper(".blog-slider", {
  loop: true,
  spaceBetween: 24,
  grabCursor: true,
  simulateTouch: true,
  allowTouchMove: true,
  touchRatio: 1.2,
  shortSwipes: true,
  longSwipes: true,
  mousewheel: {
    forceToAxis: true,
  },
  keyboard: {
    enabled: true,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1200: {
      slidesPerView: 3,
    }
  }
});
document.addEventListener("DOMContentLoaded", function(){

const scrollTopBtn = document.getElementById("scrollTopBtn");

window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    scrollTopBtn.style.display = "flex";
  } else {
    scrollTopBtn.style.display = "none";
  }
});

scrollTopBtn.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});

});