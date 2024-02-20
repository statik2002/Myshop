<template>
    <header-component></header-component>
    <div class="container">
        <div>
            CheckOut Page
        </div>
        <div class="pt-5">{{ $route.params.product }}</div>
        <div class="pt-5">{{ product }}</div>
    </div>
    <footer-component></footer-component>
</template>

<script>
    import HeaderComponent from '@/components/HeaderComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
    export default {
        components: {HeaderComponent, FooterComponent},
        data() {
            return {
                product: {}
            }
        },
        mounted() {
            const productIndex = this.$store.state.cart.findIndex((index) => index.id == this.$route.params.product);
            console.log(productIndex)
            this.product = this.$store.state.cart[productIndex]
        }
    }
</script>

<style scoped>

</style>