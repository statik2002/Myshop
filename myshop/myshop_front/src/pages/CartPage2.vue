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
        <div class="container">
            <div class="row d-none d-md-block">
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
                                    <tr v-for="product in products">
                                        <cart-product-2 :cart_product="product"></cart-product-2>
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
                                    <button class="proceed-to-checkout-btn" @click="sendOrder">Заказать</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="container-fluid d-block d-md-none">
            <div class="row">
                <table class="table">
                    <thead>
                        <tr>
                        <th scope="col"></th>
                        <th scope="col"></th>
                        <th scope="col">Товар</th>
                        <th scope="col">Цена</th>
                        <th scope="col">Коли-во</th>
                        <th scope="col">Всего</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="product in products">
                            <cart-product-2 :cart_product="product"></cart-product-2>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        </section>
        <!--== End Product Area Wrapper ==-->
    </main>

    <footer-component></footer-component>
</template>

<script>
    import router from '@/router/router';
import axios from 'axios';
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
            removeProduct(product) {

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