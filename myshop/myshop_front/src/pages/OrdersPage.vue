<template>
    <HeaderComponent></HeaderComponent>
    <div class="container">
        <div v-for="message in messages" class="py-5">
            <div class="alert alert-danger" role="alert">
            {{ message }}
            </div>
        </div>
        <div class="py-5" v-if="isOrdersLoaded">
            <div class="d-flex flex-row gap-3" >
                <!--Processing orders-->
                <p>Заказы в пути</p>
                <div v-for="order in processingOrders" v-if="processingOrders.length > 0">
                    <!--
                    <order-item :order="order" @click="$router.push({name: 'show_order', params: {'id': order.id}})">
                    </order-item>
                    -->
                    <order-item :order="order">
                    </order-item>
                </div>
                <div v-else>
                    У вас нет заказов в пути
                </div>
            </div>
            <div class="d-flex flex-column gap-3" >
                <!--Ready orders-->
                <p>Выданные заказы</p>
                <div v-for="order in completeOrders" v-if="completeOrders.length > 0">
                    <order-item :order="order">
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
    <FooterComponent></FooterComponent>
</template>

<script>
    import axios from 'axios'
    import HeaderComponent from '@/components/HeaderComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
    export default {
        components: {HeaderComponent, FooterComponent},
        data() {
            return {
                messages: [],
                orders: [],
                isOrdersLoaded: false,
                processingOrders: [],
                completeOrders: []
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
            }
        },
        mounted() {
            
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