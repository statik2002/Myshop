<template>
    <header-component></header-component>
    <!--== Start Preloader Content ==-->
    <div class="preloader-wrap" v-if="!cartIsLoad">
        <div class="preloader">
            <span class="dot"></span>
            <div class="dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
            
        </div>
    </div>
    <!--== End Preloader Content ==-->

    <main class="main-content">
        <!--== Start Page Header Area Wrapper ==-->
        <div class="page-header-area">
        <div class="container">
            <div class="row">
            <div class="col-12 text-center">
                <div class="page-header-content">
                <h4 class="title mt-0">Ваша корзина</h4>
                </div>
            </div>
            </div>
        </div>
        </div>
        <!--== End Page Header Area Wrapper ==-->

        <!--== Start Product Area Wrapper ==-->
        <section class="product-area shopping-cart-area">
            <div class="container d-none d-md-block">
                <div class="row">
                    <div class="col-12">
                        <div class="shopping-cart-wrap">
                            <div class="cart-table">
                                <table class="table table-sm">
                                    <thead>
                                        <tr>
                                        <th class="indecor-product-remove">Удалить</th>
                                        <th class="indecor-product-thumbnail">Изображение</th>
                                        <th class="indecor-product-name">Товар</th>
                                        <th class="indecor-product-price">Цена</th>
                                        <th class="indecor-product-quantity">Количество</th>
                                        <th class="indecor-product-subtotal">Всего</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="cart_product in products">
                                            <td class="indecor-product-remove">
                                                <a href="#/"><i class="bi bi-trash3" @click="$store.commit('deleteProductFromCart', cart_product.id)"></i></a>
                                            </td>
                                            <td class="indecor-product-thumbnail">
                                                <a href="#/" v-if="cart_product.product.product_images.length > 0"><img :src=cart_product.product.product_images[0].image :alt=cart_product.product.product_images[0].alt></a>
                                                <a href="#/" v-else><img src="@/assets/no_image.png" alt="no image"></a>
                                            </td>
                                            <td class="indecor-product-name">
                                                <h4 class="title"><a href="#" @click="$router.push({ name: 'product2', params: { id: cart_product.id } })">{{ cart_product.product.name }}</a></h4>
                                            </td>
                                            <td class="indecor-product-price"><span class="price">{{ cart_product.fixed_price }} &#8381;</span></td>
                                            <td class="indecor-product-quantity">
                                                <div class="pro-qty">
                                                    <div class="inc qty-btn" @click="add(cart_product)">+</div>
                                                        <input type="text" title="Quantity" :value="cart_product.quantity | 0" @input="inputQuantity(cart_product, $event)">
                                                    <div class= "dec qty-btn" @click="sub(cart_product)">-</div>
                                                </div>
                                            </td>
                                            <td class="product-subtotal"><span class="price">{{ getTotal(cart_product) }}</span></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="row">
                                <div class="col-md-12 col-lg-7 col-12">
                                    <div class="coupon-all">
                                        <div class="coupon">
                                            <div class="d-flex gap-2">
                                                <button class="button" @click="$router.push('/newfront')">Продлжить покупки</button>
                                                <button class="button" @click="clearCart">Очистить корзину</button>
                                            </div>
                                        </div>
                                        <!--
                                        <div class="coupon2">
                                            <a class="button" href="#/">Купон</a>
                                        </div>
                                        -->
                                    </div>
                                </div>
                                <!--
                                <div class="col-md-12 col-lg-7 col-12">
                                    <div class="coupon-all">
                                        <div class="coupon">
                                            <div class="cart-coupon">
                                                <h3>Пояснение к заказу</h3>
                                                <label for="Textarea1" class="form-label visually-hidden">Пояснение к заказу</label>
                                                <textarea class="form-control" id="Textarea1"></textarea>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                -->
                                <div class="col-md-12 col-lg-5 col-12">
                                    <div class="cart-page-total">
                                        <h3>Итого</h3>
                                        <ul>
                                        <li>Итого<span class="money"><b>{{ $store.getters.getCartTotal }} &#8381;</b></span></li>
                                        </ul>
                                        <div v-if="$store.getters.isUserLogin">
                                            <button v-if="$store.getters.isUserLogin" class="proceed-to-checkout-btn" @click="sendOrder">Заказать</button>
                                        </div>
                                        <div v-else class="pt-3">
                                            <h5 class="text-center">Что бы сделать заказ необходимо зарегистрироваться или войти в свой аккаунт.</h5>
                                            <div class="d-flex flex-row gap-3">
                                                <a href="#offcanvasLoginView" data-bs-toggle="modal" role="button" aria-controls="offcanvasLoginView" class="proceed-to-checkout-btn">Войти</a>
                                                <button class="proceed-to-checkout-btn" @click="$router.push('register_user')">Регистрация</button>
                                            </div>
                                            
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="container-fluid d-block d-md-none">
                <div class="shopping-cart-wrap">
                    <div class="row py-2" v-for="product in products">
                        <div class="col">
                            <div class="row">
                                <div class="col text-center">{{ product.product.name }}</div>
                            </div>
                            <div class="row">
                                <div class="col-5">
                                    <img v-if="product.product.product_images.length > 0" :src=product.product.product_images[0].image :alt=product.product.product_images[0].alt>
                                    <img v-else src="@/assets/no_image.png" alt="No image">
                                </div>
                                <div class="col-2 align-self-center">{{ product.fixed_price }} &#8381;</div>
                                <div class="col-2 align-self-center">
                                    <div class="small-product-quantity">
                                        <div class="pro-qty">
                                            <div class="inc qty-btn" @click="add(product)">+</div>
                                                <input type="text" title="Quantity" :value="product.quantity | 0" @input="inputQuantity(product, $event)">
                                            <div class= "dec qty-btn" @click="sub(product)">-</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-3 align-self-center">{{ product.fixed_price * product.quantity }} &#8381;</div>
                            </div>
                        </div>
                    </div>
                    <div class="row pt-3">
                        <div class="col">
                            <div class="cart-page-total">
                                <h3>Итого</h3>
                                <ul>
                                    <li>Итого<span class="money"><b>{{ $store.getters.getCartTotal }} &#8381;</b></span></li>
                                </ul>
                                <div v-if="$store.getters.isUserLogin">
                                    <button v-if="$store.getters.isUserLogin" class="proceed-to-checkout-btn" @click="sendOrder">Заказать</button>
                                </div>
                                <div v-else class="pt-3">
                                    <h5 class="text-center">Что бы сделать заказ необходимо зарегистрироваться или войти в свой аккаунт.</h5>
                                    <a href="#offcanvasLoginView" data-bs-toggle="modal" role="button" aria-controls="offcanvasLoginView" class="proceed-to-checkout-btn">Войти</a>
                                    <button class="proceed-to-checkout-btn" @click="$router.push('register_user')">Регистрация</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!--== End Product Area Wrapper ==-->
    </main>

    <footer-component></footer-component>
</template>

<script>
    import axios from 'axios';
    import Decimal from 'decimal.js'
    export default {
        data() {
            return {
                cartIsLoad: true,
                products: []
            }
        },
        computed: {
            productsInCart() {
                if (this.$store.getters.isUserLogin) {
                    return this.$store.state.user.cart.products;
                } else {
                    return this.$store.state.cart.products
                }
                
            },
        },
        methods: {
            add(cart_product) {
                this.$store.commit('addOne', cart_product.id)
            },
            sub(cart_product) {
                this.$store.commit('subOne', cart_product.id)
            },
            getTotal(cart_product) {
                const price = new Decimal(cart_product.product.price)
                const discount = new Decimal(cart_product.product.discount)
                const quantity = new Decimal(cart_product.quantity)
                return ((price - price * discount/100) * quantity).toFixed(2)
            },
            inputQuantity(cart_product, event){
                if(event.target.value < 1){
                    event.target.value = 1
                    this.$store.commit('setProductInCartQuantity', {id: cart_product.id , value: 1})
                } else {
                    this.$store.commit('setProductInCartQuantity', {id: cart_product.id, value: event.target.value})
                }
            },
            clearCart() {
                this.products = []
                this.$store.commit('clearCart')
            },
            async sendOrder() {
                //console.log(this.$store.state.user.access)
                let order_products = []
                for (const key in this.products){
                    order_products.push({
                        'product': this.products[key].id,
                        'quantity': this.products[key].quantity,
                        'fixed_price': this.products[key].fixed_price,
                    })
                }
                //console.log(JSON.stringify(order_products))
                const order = {
                    'order_products': order_products
                }
                //console.log(JSON.stringify(order))

                try {
                      axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/order/`,
                          method: 'post',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          data: order
                        }
                      ).then((response) => {
                            //console.log(response)
                            //this.$store.commit('clearCart')
                            this.products = []
                            this.$store.commit('deleteProductsFromCart', order_products)
                            this.$router.go()
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },
            
        },
        mounted() {
            this.products = this.$store.getters.productsInCart
        }
    }
</script>

<style scoped>

</style>