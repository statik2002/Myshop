<template>
    <HeaderComponent></HeaderComponent>
    <div class="container py-5">
        <div v-for="order_product in order.order_products">
            <div class="card p-2" >
                <div class="row">
                    <div class="col-md-3">
                        <img
                            v-if="order_product.product.product_images.length > 0"
                            :src=order_product.product.product_images[0].image
                            :alt=order_product.product.product_images[0].alt
                            class="img-fluid rounded-start"
                        >
                        <img
                            v-else
                            src="@/assets/no_image.png"
                            alt="no image"
                            class="img-fluid rounded-start"
                        >
                    </div>
                    <div class="col-md-6">
                        <div class="card-body">
                            <h5 class="card-title">{{ order_product.product.name }}</h5>
                            <div>ID заказа: {{ order.id }}</div>
                            <p class="card-text">Дата заказа: {{ $FormatDate(order.order_create) }}</p>
                            <p class="card-text">Статус заказа: {{ order.order_status.status }}</p>
                            <p class="card-text">Сумма заказа: {{ order.total_amount }} &#8381;</p>
                            <button v-if="order.order_status.status=='Выдан'" class="btn btn-success" @click="feedback">Feedback</button>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div v-if="order.order_status.status=='Готов к выдаче'">
                            <qrcode-vue :value="order.uuid" class="img-fluid" :size="200" level="H" />
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
                feedbackModalVisible: false,
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