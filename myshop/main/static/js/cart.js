class Product {

    constructor(price, quantity, id) {
        this.price = price;
        this.quantity = quantity;
        this.id = id;
    }

    price = "";
    quantity = "";
    id = "";
}

class Cart {

    products = [];
    total_products = 0;
    total_income = 0;

    showTotalProducts(selectorClass) {
        document.querySelector(selectorClass).innerHTML = this.total_products;
    }

    showTotalIncome(selectorClass) {
        document.querySelector(selectorClass).innerHTML = this.total_income.toLocaleString('ru-RU', {style: 'currency', currency: "RUB"});
    }
}

let productsInCart = document.querySelector('#productList');
let cart = new Cart();

for (let product of productsInCart.children) {
    let description = product.querySelector('.product-description');
    let quantity = product.querySelector('.quantity');
    const price = product.querySelector('.price');
    const id = product.id;
    const listedProduct = new Product(price.value, quantity.value, id);
    cart.products.push(listedProduct);
    cart.total_products += Number(quantity.value);
    cart.total_income += quantity.value * price.value;
};

cart.showTotalProducts('.cart-total-products');
cart.showTotalIncome('.cart-total-value');


productsInCart.onclick = function(event) {
    let target = event.target;
    let parent = target.parentElement;
    let quantity = parent.parentElement.querySelector('.quantity');
    let total = parent.parentElement.parentElement.parentElement.querySelector('.total');
    let price = parent.parentElement.parentElement.parentElement.querySelector('.price');
    if (parent.className === "minus-button") {
        (quantity.value >= 2) ? quantity.value-- : 1;
        total.value = (price.value * quantity.value).toLocaleString('ru-RU', {style: 'currency', currency: "RUB"});
        cart.total_products -= 1;
        cart.total_income -= Number(price.value);
    } else if (parent.className === "plus-button") {
        (quantity.value <= 999) ? quantity.value++ : 999;
        total.value = (price.value * quantity.value).toLocaleString('ru-RU', {style: 'currency', currency: "RUB"});
        cart.total_products += 1;
        cart.total_income += Number(price.value);
    }
    cart.showTotalProducts('.cart-total-products');
    cart.showTotalIncome('.cart-total-value');
};