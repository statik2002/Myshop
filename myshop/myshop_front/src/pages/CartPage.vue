<template>
    <header-component></header-component>
    <div class="container-lg pt-5">
        <div class="d-flex flex-column gap-3" v-if="!$store.state.userIsAuth">
            <div>Необходимо зарегистрироваться или войти в аккаунт что бы оформить заказ</div>
            <cart-card v-for="cartItem in $store.getters.productsInCart"
                :cart_product="cartItem">
            </cart-card>
            <div class="row p-3 cart-product widget">
                <div class="d-flex justify-content-between">
                    <div>
                        Кол-во товаров: <b>{{ $store.getters.getCartProductsCount }}</b>
                    </div>
                    <div>
                        Общая сумма: <b>{{ $store.getters.getCartTotal }} &#8381;</b>
                    </div>
                </div>
            </div>
        </div>
        <div class="d-flex flex-column gap-3" v-else>
            <cart-card v-for="cartItem in $store.getters.productsInCart"
                :cart_product="cartItem">
            </cart-card>
            <div class="row p-3 cart-product widget">
                <div class="d-flex justify-content-between">
                    <div>
                        Кол-во товаров: <b>{{ $store.getters.getCartProductsCount }}</b>
                    </div>
                    <div>
                        Общая сумма: <b>{{ $store.getters.getCartTotal }} &#8381;</b>
                    </div>
                </div>
            </div>
            <div class="row p-3 cart-product widget">
                <div class="d-flex justify-content-between">
                    <div><button type="button" class="btn btn-secondary" @click="clearCart">Удалить все</button></div>
                    <div v-if="$store.state.userIsAuth"><button type="button" class="btn btn-success" @click="orderAll">Оформить все</button></div>
                    <div v-else><button type="button" class="btn btn-success" @click="">Регистрация/Логин</button></div>
                </div>
                
            </div>
        </div>
        <modal-component v-model:show="orderModalVisible">
            <div class="container">
                <div class="d-flex flex-column gap-2">
                    <div>Ваш заказ</div>
                    <div v-for="item in $store.state.cart">
                        <div>{{ item.name }} - {{ item.quantity }} Шт. = {{ item.quantity * item.price }} Руб.</div>
                    </div>
                    <div>На сумму: {{ $store.getters.getCartTotal }} Руб.</div>
                    <div><button type="button" class="btn btn-success" @click="sendOrder">Оформить</button></div>
                </div>
            </div>
        </modal-component>
    </div>
    <footer-component></footer-component>
</template>

<script>
    import axios from 'axios'
    import HeaderComponent from '@/components/HeaderComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
    import CartCard from '@/components/ProductInCartComponent.vue'
    import ModalComponent from '@/components/UI/ModalComponent.vue'
    export default {
        components: {HeaderComponent, FooterComponent, CartCard, ModalComponent},
        data() {
            return {
                orderModalVisible: false,
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
            getProductsCount() {
                return this.$store.state.user.cart.cartProductQuantity;
            }
        },
        methods: {
            orderAll() {
                this.orderModalVisible = true
            },
            
            async sendOrder() {
                //console.log(this.$store.state.user.access)
                let order_products = []
                for (const key in this.$store.state.user.cart.products){
                    order_products.push({
                        'product': this.$store.state.user.cart.products[key].id,
                        'quantity': this.$store.state.user.cart.products[key].quantity,
                        'fixed_price': this.$store.state.user.cart.products[key].fixed_price,
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
                          url: `${this.$store.state.apiUrl}/api/v1/order/`,
                          method: 'post',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          data: order
                        }
                      ).then((response) => {
                            //console.log(response)
                            //this.$store.commit('clearCart')
                            this.$store.commit('deleteProductsFromCart', order_products)
                            this.orderModalVisible = false
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },

            clearCart() {
                this.$store.commit('clearCart')
            }
        }
    }
</script>

<style scoped>

</style>