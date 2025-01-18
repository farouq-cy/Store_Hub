"use strict";
const body = document.querySelector("body");
const toggle = document.querySelector("#toggle");
const sunIcon = document.querySelector(".toggle .bxs-sun");
const moonIcon = document.querySelector(".toggle .bx-moon");

toggle.addEventListener("change", () => {
  body.classList.toggle("dark");
  sunIcon.className =
    sunIcon.className == "bx bxs-sun" ? "bx bx-sun" : "bx bxs-sun";
  moonIcon.className =
    moonIcon.className == "bx bxs-moon" ? "bx bx-moon" : "bx bxs-moon";
  if (body.classList.contains("dark")) {
    localStorage.setItem("DarkToogle", "Dark");
  } else {
    localStorage.removeItem("DarkToogle");
  }
});
document.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("DarkToogle")) {
    body.classList.add("dark");
    sunIcon.className =
      sunIcon.className == "bx bxs-sun" ? "bx bx-sun" : "bx bxs-sun";
    moonIcon.className =
      moonIcon.className == "bx bxs-moon" ? "bx bx-moon" : "bx bxs-moon";
  }
});

// Start Swiper
const swiper = new Swiper(".swiper", {
  loop: true,

  pagination: {
    el: ".swiper-pagination",
    dynamicBullests: true,
    clickable: true,
  },
  autoplay: {
    delay: 1500,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  scrollbar: {
    el: ".swiper-scrollbar",
  },
});
// End Swiper

let days = document.querySelector(".day");
let hour = document.querySelector(".hour");
let minut = document.querySelector(".minut");
let second = document.querySelector(".second");

function updateClock() {
  let dayValue = parseInt(days.innerText);
  let hourValue = parseInt(hour.innerText);
  let minutValue = parseInt(minut.innerText);
  let secondValue = parseInt(second.innerText);

  secondValue--;

  if (secondValue < 0) {
    secondValue = 59;
    minutValue--;
  }

  if (minutValue < 0) {
    minutValue = 59;
    hourValue--;
  }

  if (hourValue < 0) {
    hourValue = 23;
    dayValue--;
  }

  if (dayValue < 0) {
    dayValue = 2;
  }

  days.innerText = dayValue < 10 ? "0" + dayValue + ":" : dayValue + ":";
  hour.innerText = hourValue < 10 ? "0" + hourValue + ":" : hourValue + ":";
  minut.innerText = minutValue < 10 ? "0" + minutValue + ":" : minutValue + ":";
  second.innerText = secondValue < 10 ? "0" + secondValue : secondValue;
}

setInterval(updateClock, 1000);
