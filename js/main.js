// open / close cart

let cart = document.querySelector(".cart");
function openCart() {
  cart.classList.add("active");
}
function closeCart() {
  cart.classList.remove("active");
}

// open & close menu

let menu = document.querySelector(".links ul");
function openMenu() {
  menu.classList.add("active");
}
function closeMenu() {
  menu.classList.remove("active");
}

// add item img

let bigImg = document.getElementById("big_img");

function changItemImg(img, name) {
  bigImg.src = img;
}

// add items in cart

var allProductsJson;

var items_in_cart = document.querySelector(".items_in_cart");

let productCart = [];

function addToCart(id, btn) {
  productCart.push(allProductsJson[id]);
  btn.classList.add("active");

  console.log(productCart);
  getCartItems();
}

let count_item = document.querySelector(".count_item");
let price_cart_head = document.querySelector(".price_cart_head");
let item_in_cart = document.querySelector(".item_in_cart");
let price_cart_total = document.querySelector(".price_cart_total");

function getCartItems() {
  let totalPrice = 0;
  let items_c = "";
  for (let i = 0; i < productCart.length; i++) {
    items_c += `
                <div class="item_cart">
                <img src="${productCart[i].img}" alt="">
                <div class="content">
                    <h4>${productCart[i].name}</h4>
                    <p class="price_cart">$${productCart[i].price}</p>
                </div>
                <button onclick="removeFromCart(${i})" class="delet_item"><i class="fa-solid fa-dumpster"></i></button>
            </div>
        `;

    totalPrice += productCart[i].price;
  }
  items_in_cart.innerHTML = items_c;

  price_cart_head.innerHTML = `$${totalPrice}`;

  count_item.innerHTML = productCart.length;

  item_in_cart.innerHTML = `(${productCart.length}  Item in cart)`;
  price_cart_total.innerHTML = "$" + totalPrice;
}

function removeFromCart(index) {
  productCart.splice(index, 1);
  getCartItems();
  let addToCartBtns = document.querySelectorAll(".fa-cart-plus");
  for (let i = 0; i < addToCartBtns.length; i++) {
    addToCartBtns[i].classList.remove("active");

    productCart.forEach((product) => {
      if (product.id == i) {
        addToCartBtns[i].classList.add("active");
      }
    });
  }
}

let back_to_top = document.querySelector(".back_to_top");

back_to_top.addEventListener("click", function () {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});

function darktoggle() {
  document.body.classList.toggle("dark");
}

