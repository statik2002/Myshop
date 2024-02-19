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
                    <div>Удалить все</div>
                    <div>Оформить все</div>
                </div>
                
            </div>
        </div>
        
    </div>
    <footer-component></footer-component>
</template>

<script>
    import HeaderComponent from '@/components/HeaderComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
    import CartCard from '@/components/ProductInCartComponent.vue'
    export default {
        components: {HeaderComponent, FooterComponent, CartCard},
        computed: {
            productsInCart() {
                return this.$store.getters['getCart'];
            },
            getProductsCount() {
                return this.$store.cartProductQuantity;
            }
        }
    }
</script>

<style scoped>

</style>