<template>
    <HeaderComponent></HeaderComponent>
    <div class="container py-3">
        <div class="d-flex flex-column gap-2" v-if="isLoad">
            <div>ID: {{ order.id }}</div>
            <div>Date: {{ order.order_create }}</div>
            <div>Status: {{ order.order_status.status }}</div>
            <div>Total: {{ order.total_amount }} Руб.</div>
            <div v-if="order.order_status.id==5"><QrcodeVue :value=order.uuid></QrcodeVue></div>
            <div v-for="order_product in order.order_products">
                <div class="d-flex flex-row gap-2 border">
                    <div v-if="order_product.product.product_images.length > 0">
                        <img :src=order_product.product.product_images[0].image :alt=order_product.product.product_images[0].alt :width="100">
                    </div>
                    <div>{{ order_product.product.name }}</div>
                    <div>{{ order_product.fixed_price }} Руб. </div>
                    <div>{{ order_product.quantity }} Шт.</div>
                </div>
                
            </div>
        </div>
    </div>
    <FooterComponent></FooterComponent>
</template>

<script>
    import axios from 'axios'
    import QrcodeVue from 'qrcode.vue'
    import HeaderComponent from '@/components/HeaderComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
    export default {
        components: { HeaderComponent, FooterComponent, QrcodeVue },
        data() {
            return {
                orderId: 0,
                order: {},
                isLoad: false
            }
        },
        methods: {
            getOrder() {
                const request_data = {
                    'user': this.$store.state.user.id
                }
                try {
                      axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/order/${this.orderId}/`,
                          method: 'get',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          data: request_data
                        }
                      ).then((response) => {
                            //this.orders = response.data
                            this.order = response.data
                            this.isLoad = true
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },
            formatDate(date){
                date = new Date(date)
                let year = new Intl.DateTimeFormat('ru', { year: 'numeric' }).format(date);
                let month = new Intl.DateTimeFormat('ru', { month: 'short' }).format(date);
                let day = new Intl.DateTimeFormat('ru', { day: '2-digit' }).format(date);
                let hour = new Intl.DateTimeFormat('ru', { hour: '2-digit' }).format(date);
                let minute = new Intl.DateTimeFormat('ru', { minute: '2-digit' }).format(date);
                return `${day} ${month} ${year} ${hour}:${minute}`
            },
        },
        mounted() {
            this.orderId = this.$route.params.id
            this.getOrder()
        }
    }
</script>

<style scoped>

</style>