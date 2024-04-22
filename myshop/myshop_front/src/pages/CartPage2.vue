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
            <div class="row">
            <div class="col-12">
                <div class="shopping-cart-wrap">
                <div class="cart-table table-responsive">
                    <table class="table">
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
                            <a class="button" href="shop.html">Продлжить покупки</a>
                            <a class="button" href="#/">Очистить корзину</a>
                            <div class="cart-coupon">
                                <h3>Пояснение к заказу</h3>
                                <label for="Textarea1" class="form-label visually-hidden">Пояснение к заказу</label>
                                <textarea class="form-control" id="Textarea1"></textarea>
                            </div>
                        </div>
                        <div class="coupon2">
                            <a class="button" href="#/">Купон</a>
                        </div>
                    </div>
                    </div>
                    <div class="col-md-12 col-lg-5 col-12">
                    <div class="cart-page-total">
                        <h3>Итого</h3>
                        <ul>
                        <li>Итого<span class="money"><b>{{ $store.getters.getCartTotal }} &#8381;</b></span></li>
                        </ul>
                        <a class="proceed-to-checkout-btn" href="checkout.html">Оплатить</a>
                    </div>
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
    export default {
        data() {
            return {
                cartIsLoad: true,
                products: []
            }
        },
        computed: {
            productsInCart() {
                if (this.$store.state.userIsAuth) {
                    return this.$store.state.user.cart.products;
                } else {
                    return this.$store.state.cart.products
                }
                
            },
        },
        methods: {
            removeProduct(product) {

            },
        },
        mounted() {
            this.products = this.$store.getters.productsInCart
        }
    }
</script>

<style scoped>

</style>