<template>
    <div class="card mb-3 ">
        <div class="row g-0">
            <div class="col-md-3" v-if="order.order_products[0].product.product_images.length > 0">
                <img 
                    class="img-fluid rounded-start" 
                    :src=order.order_products[0].product.product_images[0].image 
                    :alt=order.order_products[0].product.product_images[0].alt>
            </div>
            <div class="col-2" v-else>No Image</div>
            <div class="col-md-9">
                <div class="card-body">
                    <div class="d-flex flex-column ">
                        <h5 class="card-title">{{ order.order_products[0].product.name }}</h5>
                        <div class="d-flex flex-row gap-2">
                            <p class="card-text">Order id: {{ order.id }}</p>
                            <p class="card-text">Товаров: {{ Number(order.order_products[0].quantity) }} Шт.</p>
                            <p class="card-text" v-if="order.order_status.id==4"><i class="bi bi-sign-stop"></i> {{ order.order_status.status }}</p>
                            <p class="card-text" v-if="order.order_status.id==1"><i class="bi bi-pin-angle"></i> {{ order.order_status.status }}</p>
                            <p class="card-text" v-if="order.order_status.id==2"><i class="bi bi-gear"></i> {{ order.order_status.status }}</p>
                            <p class="card-text" v-if="order.order_status.id==3"><i class="bi bi-box2-heart"></i> {{ order.order_status.status }}</p>
                            <p class="card-text" v-if="order.order_status.id==5"><i class="bi bi-patch-check"></i> {{ order.order_status.status }}</p>
                            <p class="card-text" v-if="order.order_status.id==6"><i class="bi bi-file-earmark-zip"></i> {{ order.order_status.status }}</p>
                        </div>
                        <p class="card-text"><i class="bi bi-wallet2"></i> {{ order.total_amount }} Руб.</p>
                    </div>
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
        data() {
            return {
                cardClass: ''
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