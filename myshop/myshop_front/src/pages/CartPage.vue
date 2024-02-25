<template>
    <header-component></header-component>
    <div class="container-lg pt-5">
        <div class="mb-5" v-if="!$store.state.userIsAuth">Необходимо зарегистрироваться или войти в аккаунт что бы оформить заказ</div>
        <div class="d-flex flex-column gap-3">
            <cart-card v-for="cartItem in productsInCart"
                :name='cartItem.name'
                :description='cartItem.description'
                :id='cartItem.id'
                :product_images='cartItem.product_images'
                :available='cartItem.available'
                :slug='cartItem.slug'
                :rating='cartItem.rating'
                :show_count='cartItem.show_count'
                :create_date='cartItem.create_date'
                :price='cartItem.price'
                :discount='cartItem.price'
                :code_1c='cartItem.code_1c'
                :quantity='cartItem.quantity'
                :catalog='cartItem.catalog'
                :tags="cartItem.tags">
            </cart-card>
            <div class="row p-3 cart-product widget">
                <div class="d-flex justify-content-between">
                    <div>
                        Кол-во товаров: <b>{{ $store.getters.getTotalProductQuantity }}</b>
                    </div>
                    <div>
                        Общая сумма: <b>{{ $store.getters.getTotalProductsAmount }} &#8381;</b>
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
                    <div>На сумму: {{ $store.getters.getTotalProductsAmount }} Руб.</div>
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
                orderModalVisible: false
            }
        },
        computed: {
            productsInCart() {
                return this.$store.getters['getCart'];
            },
            getProductsCount() {
                return this.$store.cartProductQuantity;
            }
        },
        methods: {
            orderAll() {
                this.orderModalVisible = true
            },
            
            async sendOrder() {
                //console.log(this.$store.state.user.access)
                let order_products = []
                for (const key in this.$store.state.cart){
                    order_products.push({
                        'product': this.$store.state.cart[key].id,
                        'quantity': this.$store.state.cart[key].quantity,
                        'fixed_price': this.$store.state.cart[key].price,
                    })
                }
                //console.log(order_products)
                //console.log(JSON.stringify(order_products))
                const order = {
                    'user': this.$store.state.user.id,
                    'products_in_order': order_products
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
                            this.$store.commit('clearCart')
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