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
let daysElement = document.querySelector(".day");
let hourElement = document.querySelector(".hour");
let minutElement = document.querySelector(".minut");
let secondElement = document.querySelector(".second");

function getTimeDifference(endTime) {
  const now = new Date().getTime();
  const diff = endTime - now;
  const totalSeconds = Math.floor(diff / 1000);
  const seconds = totalSeconds % 60;
  const totalMinutes = Math.floor(totalSeconds / 60);
  const minutes = totalMinutes % 60;
  const totalHours = Math.floor(totalMinutes / 60);
  const hours = totalHours % 24;
  const totalDays = Math.floor(totalHours / 24);

  return { days: totalDays, hours, minutes, seconds };
}

function startTimer() {
  let endTime = localStorage.getItem("timerEndTime");

  if (!endTime) {
    endTime = new Date().getTime() + 3 * 24 * 60 * 60 * 1000;
    localStorage.setItem("timerEndTime", endTime);
  } else {
    endTime = parseInt(endTime, 10);
  }

  setInterval(() => {
    const { days, hours, minutes, seconds } = getTimeDifference(endTime);

    daysElement.innerText = days < 10 ? "0" + days + ":" : days + ":";
    hourElement.innerText = hours < 10 ? "0" + hours + ":" : hours + ":";
    minutElement.innerText = minutes < 10 ? "0" + minutes + ":" : minutes + ":";
    secondElement.innerText = seconds < 10 ? "0" + seconds : seconds;

    if (days <= 0 && hours <= 0 && minutes <= 0 && seconds <= 0) {
      endTime = new Date().getTime() + 3 * 24 * 60 * 60 * 1000;
      localStorage.setItem("timerEndTime", endTime);
    }
  }, 1000);
}

startTimer();
