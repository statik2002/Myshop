<template>
    <header-component></header-component>
    <div class="container-lg pt-5">
        <cart-card v-for="cartItem in productsInCart"
            :name='cartItem.name'
            :description='cartItem.description'
            :id='cartItem.id'
            :product_images='cartItem.product_iamges'
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
            }
        }
    }
</script>

<style scoped>

</style>