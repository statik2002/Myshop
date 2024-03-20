<template>
    <div class="widget">
        <div class="row p-3" v-if="order.order_products.length > 0">
            <div class="col-1"><i class="bi bi-dot"></i> {{ order.id }}</div>
            <div class="col-1" v-if="order.order_status.id==4"><span class="badge bg-danger"><i class="bi bi-sign-stop"></i></span></div>
            <div class="col-1" v-if="order.order_status.id==1"><span class="badge bg-warning"><i class="bi bi-pin-angle"></i></span></div>
            <div class="col-1" v-if="order.order_status.id==2"><span class="badge bg-info"><i class="bi bi-gear"></i></span></div>
            <div class="col-1" v-if="order.order_status.id==3"><span class="badge bg-info"><i class="bi bi-box2-heart"></i></span></div>
            <div class="col-1" v-if="order.order_status.id==5"><span class="badge bg-success"><i class="bi bi-patch-check"></i></span></div>
            <div class="col-1" v-if="order.order_status.id==6"><span class="badge bg-secondary"><i class="bi bi-file-earmark-zip"></i></span></div>
            <div class="col-2" ><i class="bi bi-clock"></i> {{ formatDate(order.order_create) }}</div>
            <div class="col-2">Товаров: {{ order.order_products.length }} Шт.</div>
            <div class="col-2" v-if="order.order_products[0].product.product_images.length > 0">
                <img :src=order.order_products[0].product.product_images[0].image :alt=order.order_products[0].product.product_images[0].alt width="50">
            </div>
            <div class="col-2" v-else>No Image</div>
            <div class="col-2"><i class="bi bi-patch-check"></i> {{ order.order_status.status }}</div>
            <div class="col-2"><i class="bi bi-wallet2"></i> {{ order.total_amount }} Руб.</div>
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