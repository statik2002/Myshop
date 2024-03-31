<template>
    <HeaderComponent></HeaderComponent>
    <div class="container py-5">
        <div v-for="order_product in order.order_products">
            <div class="card mb-3" >
                <div class="row g-0">
                    <div class="col-md-4">
                        <img :src=order_product.product.product_images[0].image :alt=order_product.product.product_images[0].alt class="img-fluid rounded-start">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title">{{ order_product.product.name }}</h5>
                            <div>Order id: {{ order.id }}</div>
                            <p class="card-text">Order date: {{ order.order_create }}</p>
                            <p class="card-text">Status: {{ order.order_status.status }}</p>
                            <p class="card-text">Total: {{ order.total_amount }} Rub</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <modal-component v-model:show="feedbackModalVisible">
        <feedback-form v-model:show="feedbackModalVisible" :product_id="order.order_products[0].product.id"></feedback-form>
    </modal-component>
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
                isLoad: false,
                feedbackModalVisible: false
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

            feedback() {
                this.feedbackModalVisible = true
            }
        },
        mounted() {
            this.orderId = this.$route.params.id
            this.getOrder()
        }
    }
</script>

<style scoped>

</style>