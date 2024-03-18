<template>
    <HeaderComponent></HeaderComponent>
    <div class="container">
        <div v-for="message in messages" class="py-5">
            <div class="alert alert-danger" role="alert">
            {{ message }}
            </div>
        </div>
        <div class="py-5">
            <div class="d-flex flex-column gap-3">
                <div v-for="order in orders">
                    <order-item :order="order" @click="$router.push({name: 'show_order', params: {'id': order.id}})">
                    </order-item>
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
                orders: []
            }
        },
        methods: {
            loadOrders(){
                try {
                    const request_data = {
                        'user': this.$store.state.user.id
                    }
                      axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/order/get_orders/`,
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          method: 'post',
                            data: request_data
                        }
                      ).then((response) => {
                            this.messages = []
                            this.orders = response.data
                            console.log(response.data)
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