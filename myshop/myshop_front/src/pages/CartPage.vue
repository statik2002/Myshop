<template>
    <header-component></header-component>
    <div class="container-lg pt-5">
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
                    <div><button type="button" class="btn btn-secondary">Удалить все</button></div>
                    <div><button type="button" class="btn btn-success" @click="orderAll">Оформить все</button></div>
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
                    <div><button type="button" class="btn btn-success ">Оформить</button></div>
                </div>
            </div>
        </modal-component>
    </div>
    <footer-component></footer-component>
</template>

<script>
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
            }
        }
    }
</script>

<style scoped>

</style>