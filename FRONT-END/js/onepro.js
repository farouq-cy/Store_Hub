"use strict";

// Start One Product Page
let dec = document.querySelector(
  ".imgAndDetailes .container .detailes .buyLove .dec"
);
let inc = document.querySelector(
  ".imgAndDetailes .container .detailes .buyLove .inc"
);
let Num = document.getElementById("Num");

dec.addEventListener("click", () => {
    if(Num.innerHTML == '0') Num.innerHTML = '0';
    else Num.innerHTML--;
});
inc.addEventListener("click", () => {
    Num.innerHTML++;
});
