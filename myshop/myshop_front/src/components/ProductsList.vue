<template>
    <div class="container-xl pt-3">
        <div class="row g-1">
            <TransitionGroup name="products">
                <div v-for="product in products" :key="product" class="col-xxl-2 col-xl-2 col-lg-2 col-md-3 col-sm-6">
                    <product-card :product="product"/>
                </div>
            </TransitionGroup>
        </div>
    </div>
</template>

<script>
    import ProductCard from '@/components/ProductCard.vue'
    export default {
        components: {ProductCard},
        name: 'products-list',
        props: {
            products: {
                type: Array,
                required: true
            }
        }
    }
</script>

<style scoped>
.products-enter-active,
.products-leave-active {
  transition: all 0.5s ease;
}
.products-enter-from,
.products-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>