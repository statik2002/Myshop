<template>
    <!--
    <div class="widget">
        <div class="row p-3" v-if="order.order_products.length > 0">
            <div class="col-1"><i class="bi bi-sort-numeric-up-alt"></i> {{ order.id }}</div>
            <div class="col-2" v-if="order.order_products[0].product.product_images.length > 0">
                <img :src=order.order_products[0].product.product_images[0].image :alt=order.order_products[0].product.product_images[0].alt width="80">
            </div>
            <div class="col-2" v-else>No Image</div>
            <div class="col-3" ><i class="bi bi-clock"></i> {{ formatDate(order.order_create) }}</div>
            <div class="col-2">Товаров: {{ order.order_products.length }} Шт.</div>
            <div class="col-2" v-if="order.order_status.id==4"><i class="bi bi-sign-stop"></i> {{ order.order_status.status }}</div>
            <div class="col-2" v-if="order.order_status.id==1"><i class="bi bi-pin-angle"></i> {{ order.order_status.status }}</div>
            <div class="col-2" v-if="order.order_status.id==2"><i class="bi bi-gear"></i> {{ order.order_status.status }}</div>
            <div class="col-2" v-if="order.order_status.id==3"><i class="bi bi-box2-heart"></i> {{ order.order_status.status }}</div>
            <div class="col-2" v-if="order.order_status.id==5"><i class="bi bi-patch-check"></i> {{ order.order_status.status }}</div>
            <div class="col-2" v-if="order.order_status.id==6"><i class="bi bi-file-earmark-zip"></i> {{ order.order_status.status }}</div>
            <div class="col-2"><i class="bi bi-wallet2"></i> {{ order.total_amount }} Руб.</div>
        </div>
    </div>
    -->
    <div class="card mb-3">
        <div class="row g-0">
            <div class="col-md-4" v-if="order.order_products[0].product.product_images.length > 0">
                <img class="img-fluid rounded-start" :src=order.order_products[0].product.product_images[0].image :alt=order.order_products[0].product.product_images[0].alt>
            </div>
            <div class="col-2" v-else>No Image</div>
            <div class="col-md-8">
                <div class="card-body">
                    <h5 class="card-title">{{ order.order_products[0].product.name }}</h5>
                    <p class="card-text">Order id: {{ order.id }}</p>
                    <p class="card-text">Товаров: {{ Number(order.order_products[0].quantity) }} Шт.</p>
                    <p class="card-text" v-if="order.order_status.id==4"><i class="bi bi-sign-stop"></i> {{ order.order_status.status }}</p>
                    <p class="card-text" v-if="order.order_status.id==1"><i class="bi bi-pin-angle"></i> {{ order.order_status.status }}</p>
                    <p class="card-text" v-if="order.order_status.id==2"><i class="bi bi-gear"></i> {{ order.order_status.status }}</p>
                    <p class="card-text" v-if="order.order_status.id==3"><i class="bi bi-box2-heart"></i> {{ order.order_status.status }}</p>
                    <p class="card-text" v-if="order.order_status.id==5"><i class="bi bi-patch-check"></i> {{ order.order_status.status }}</p>
                    <p class="card-text" v-if="order.order_status.id==6"><i class="bi bi-file-earmark-zip"></i> {{ order.order_status.status }}</p>
                    <p class="card-text"><i class="bi bi-wallet2"></i> {{ order.total_amount }} Руб.</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'order-item',
        props: {
            order: {
                type: Object,
                required: true
            }
        },
        methods: {
            formatDate(date){
                date = new Date(date)
                let year = new Intl.DateTimeFormat('ru', { year: 'numeric' }).format(date);
                let month = new Intl.DateTimeFormat('ru', { month: 'short' }).format(date);
                let day = new Intl.DateTimeFormat('ru', { day: '2-digit' }).format(date);
                let hour = new Intl.DateTimeFormat('ru', { hour: '2-digit' }).format(date);
                let minute = new Intl.DateTimeFormat('ru', { minute: '2-digit' }).format(date);
                return `${day} ${month} ${year} ${hour}:${minute}`
            }
        }
    }
</script>

<style scoped>

</style>