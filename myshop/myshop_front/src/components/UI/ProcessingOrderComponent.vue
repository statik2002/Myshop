<template>
    <div class="card text-bg-dark" style="width: 15vw">
        <img
            v-if="order.order_products[0].product.product_images.length > 0" 
            :src=order.order_products[0].product.product_images[0].image 
            class="card-img" 
            :alt=order.order_products[0].product.product_images.alt
            >
        <img
            v-else 
            src="@/assets/no_image.png"
            class="card-img" 
            alt="no image"
            >
        <div class="card-img-overlay">
            <router-link :to="{name: 'show_order', params: {id: order.id}}" class="stretched-link">
            <div class="d-flex flex-column h-100">
                <div class="alert alert-light p-1" role="alert">{{ $FormatDate(order.order_create) }}</div>
                <div class="mt-auto"><h5><span class="badge text-bg-success rounded-pill">{{order.order_status.status}}</span></h5></div>
            </div>
            </router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'processing-order',
        props: {
            order: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
            }
        },
        methods: {
        },
        mounted(){
            switch(this.order.order_status.status) {
                case 'Выдан': this.cardClass = 'card mb-3 bg-primary'; break;
            }
        }
    }
</script>

<style scoped>

</style>