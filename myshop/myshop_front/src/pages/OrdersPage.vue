<template>
    <HeaderComponent></HeaderComponent>
    <div class="container">
        <div v-for="message in messages" class="py-5">
            <div class="alert alert-danger" role="alert">
                {{ message }}
            </div>
        </div>
        <div class="d-flex flex-column py-5" v-if="isOrdersLoaded">
            <div class="" v-if="processingOrders.length > 0">
                <p>Заказы в пути</p>
                <carousel :items-to-show="5" :wrapAround=carouselWrap>
                    <slide v-for="slide in processingOrders" :key="slide">
                        <processing-order :order="slide">
                        </processing-order>
                    </slide>
                    <template #addons>
                        <navigation />
                        <pagination />
                    </template>
                </carousel>
            </div>
            <div class="d-flex flex-column gap-3" >
                <!--Ready orders-->
                <p>Выданные заказы</p>
                <div v-for="order in completeOrders" v-if="completeOrders.length > 0">
                    <order-item :order="order" @click="setRating(order)">
                    </order-item>
                </div>
                <div v-else>
                    У вас нет выданых заказов
                </div>
            </div>
        </div>
        <div v-else class="d-flex justify-content-center align-items-center" style="min-height: 80vh;">
            <div class="spinner-grow" style="width: 5rem; height: 5rem;" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
    </div>
    <modal-component v-model:show="feedbackModalVisible">
        <feedback-form v-model:show="feedbackModalVisible" :product_id="selectedOrderProduct"></feedback-form>
    </modal-component>
    <FooterComponent></FooterComponent>
</template>

<script>
    import axios from 'axios'
    import HeaderComponent from '@/components/HeaderComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
    import 'vue3-carousel/dist/carousel.css'
    import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

    export default {
        components: {HeaderComponent, FooterComponent, Carousel, Slide, Pagination, Navigation},
        data() {
            return {
                messages: [],
                orders: [],
                isOrdersLoaded: false,
                processingOrders: [],
                completeOrders: [],
                carouselItemsToShow: 5,
                carouselWrap: true,
                feedbackModalVisible: false,
                selectedOrderProduct: 0
            }
        },
        methods: {
            loadOrders(){
                try {
                      axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/order/get_orders/`,
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          method: 'get',
                        }
                      ).then((response) => {
                            this.messages = []
                            this.orders = response.data
                            this.isOrdersLoaded = true
                            for(const order of this.orders) {
                                if (order.order_status.status=="Выдан"){
                                    this.completeOrders.push(order)
                                } else {
                                    this.processingOrders.push(order)
                                }
                            }
                            //console.log(response.data)
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            }, 
            setRating(order) {
                this.selectedOrderProduct = order.order_products[0].product.id
                this.feedbackModalVisible = true
            }
        },
        mounted() {
            
            if (this.processingOrders.length < 5) {
                this.carouselWrap = false
            }

            if (this.$store.state.user.access)
            {
                this.loadOrders()
            } else {
                this.messages.push('Not login!')
            }
        }
    }
</script>

<style scoped>

</style>