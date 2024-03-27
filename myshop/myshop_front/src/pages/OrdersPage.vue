<template>
    <HeaderComponent></HeaderComponent>
    <div class="container">
        <div v-for="message in messages" class="py-5">
            <div class="alert alert-danger" role="alert">
            {{ message }}
            </div>
        </div>
        <div class="py-5">
            <div class="d-flex flex-column gap-3" v-if="isOrdersLoaded">
                <div v-for="order in orders" v-if="orders.length > 0">
                    <order-item :order="order" @click="$router.push({name: 'show_order', params: {'id': order.id}})">
                    </order-item>
                </div>
                <div v-else>
                    Вы не делали заказов
                </div>
            </div>
            <div v-else class="d-flex justify-content-center align-items-center" style="min-height: 80vh;">
                <div class="spinner-grow" style="width: 5rem; height: 5rem;" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
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
                isOrdersLoaded: false
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