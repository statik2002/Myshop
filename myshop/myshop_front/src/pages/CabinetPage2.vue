<template>
    <header-component></header-component>
    <div class="wrapper">
        

        <!--== Start Preloader Content ==-->
        <div class="preloader-wrap" v-if="!isCabinetLoad">
            <div class="preloader">
                <span class="dot"></span>
                <div class="dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
                
            </div>
        </div>
        <!--== End Preloader Content ==-->

        <main class="">
            <div class="container-lg mt-5" v-if="$store.getters.isUserLogin">
                <div class="d-flex flex-column mb-2" style="font-size: 0.9em;">
                    <div class="row">
                        <!--Orders widget-->
                        <div class="col-xxl-4 col-xl-4 col-lg-4 col-md-6 col-sm-6 mb-3">
                            <div class="widget p-3 h-100">
                                <div class="d-flex flex-column justify-content-between h-100">
                                    <div class="">
                                        <div class="row">
                                        <div class="col-auto">
                                            <div class="circle">
                                            <div class="">
                                                <i class="bi bi-box-seam icon-at-circle"></i>
                                            </div>
                                            </div>
                                        </div>
                                        <div class="col align-self-center">
                                            <div class="h4">Активные заказы</div>
                                        </div>
                                        </div>
                                    </div>
                                <div class="d-flex justify-content-between">
                                    <a href="#" @click="showReadyOrders">{{ $HumanizieOrders(ready_orders.length) }}</a>
                                    <span>Ожидают получения</span>
                                </div>
                                <div class="d-flex justify-content-between">
                                    <a href="#" @click="showProcessingOrders">{{ $HumanizieOrders(processing_orders.length) }}</a>
                                    <span>В пути</span>
                                </div>
                                </div>
                            </div>
                        </div>
                        <!--User widget-->
                        <div class="col-xxl-4 col-xl-4 col-lg-4 col-md-6 col-sm-6 mb-3">
                            <div class="widget p-3 h-100">
                                <div class="d-flex flex-column justify-content-between h-100">
                                <div class="d-flex">
                                    <div class="col-auto">
                                        <div class="circle" @click="uploadAvatar">
                                            <div v-if="$store.state.user.avatar">
                                                <div class="cabinet-avatar"><img :src="$store.state.user.avatar" alt="avatar" class=""></div>
                                            </div>
                                            <div v-else class="cabinet-avatar"><img src="@/assets/avatar_blank.webp" alt="avatar" class=""></div>
                                        </div>
                                    </div>
                                    <div class="col align-self-center">
                                        <div class="ms-2">{{ $store.state.user.first_name }}</div>
                                        <div class="ms-2">{{ $store.state.user.last_name }}</div>
                                        <div class="ms-2">{{ $store.state.user.email }}</div>
                                        <div class="ms-2">{{ $store.state.user.address }}</div>
                                    </div>
                                    <div class="col-auto">
                                    <div class="ms-auto"><a href="#" @click="showUserEdit"><i class="bi bi-pencil"></i></a></div>
                                    </div>
                                </div>
                                <div class="row mt-2">
                                    <div class="col">
                                    <div class=""><span class="text-secondary">Телефон:</span>{{ $store.state.user.phone_number }}</div>
                                    </div>
                                    <div class="col-auto">
                                    <div class="ms-auto"><button class="btn-theme" @click="userLogout">Выйти</button></div>
                                    </div>
                                </div>
                                </div>
                            </div>
                        </div>
                        <!--Discount widget-->
                        <div class="col-xxl-4 col-xl-4 col-lg-4 col-md-6 col-sm-6 mb-3">
                            <div class="widget p-3 h-100">
                                <div class="d-flex flex-column justify-content-between h-100">
                                <div class="">
                                    <div class="row">
                                    <div class="col-auto">
                                        <div class="circle">
                                        <div class="text-at-circle">{{ $store.state.user.personal_discount }}%</div>
                                        </div>
                                    </div>
                                    <div class="col align-self-center">
                                        <div class="h4">Ваша сидка</div>
                                    </div>
                                    </div>
                                </div>
                                <div class="d-flex justify-content-between">
                                    <span class="text-secondary">Кпить на 2345 &#8381; для скидки 6%</span>
                                </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row pt-5">
                        <div class="col-12">
                            <h4 class="order-header">Готовые заказы к выдаче</h4>
                            <div class="table-responsive">
                                <table class="table table-hover">
                                    <thead>
                                        <tr>
                                            <th scope="col">№</th>
                                            <th scope="col">ID заказа</th>
                                            <th scope="col">Изображение</th>
                                            <th scope="col">Наименование</th>
                                            <th scope="col">Пункт выдачи</th>
                                            <th scope="col">Сумма заказа</th>
                                            <th scope="col">QR код</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="order, index in ready_orders">
                                            <th scope="row">{{index+1}}</th>
                                            <td>{{order.id}}</td>
                                            <td>
                                                <img v-if="order.order_products[0].product.product_images.length > 0" :src=order.order_products[0].product.product_images[0].image :alt=order.order_products[0].product.product_images[0].alt height="100px">
                                                <img v-else src="@/assets/no_image.png" alt="no image" height="100px">
                                            </td>
                                            <td>{{ order.order_products[0].product.name }}</td>
                                            <td>Маг. Мозаика</td>
                                            <td>{{ order.total_amount }} &#8381;</td>
                                            <td @click="showQRModal(order)"><qrcode-vue :value="order.uuid" :size="100"></qrcode-vue></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div class="row py-5">
                        <div class="col-12">
                            <h4 class="order-header">Заказы в пути</h4>
                            <div class="table-responsive">
                                <table class="table table-hover">
                                    <thead>
                                        <tr>
                                        <th scope="col">№</th>
                                        <th scope="col">ID заказа</th>
                                        <th scope="col">Статус заказа</th>
                                        <th scope="col">Изображение</th>
                                        <th scope="col">Наименование</th>
                                        <th scope="col">Пункт выдачи</th>
                                        <th scope="col">Сумма заказа</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="order, index in processing_orders">
                                            <th scope="row">{{index+1}}</th>
                                            <td>{{order.id}}</td>
                                            <td>{{ order.order_status.status }}</td>
                                            <td>
                                                <img v-if="order.order_products[0].product.product_images.length > 0" :src=order.order_products[0].product.product_images[0].image :alt=order.order_products[0].product.product_images[0].alt height="100px">
                                                <img v-else src="@/assets/no_image.png" alt="no image" height="100px">
                                            </td>
                                            <td>{{ order.order_products[0].product.name }}</td>
                                            <td>Маг. Мозаика</td>
                                            <td>{{ order.total_amount }} &#8381;</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div class="row py-5">
                        <div class="col-12">
                            <h4 class="order-header">Выданные заказы</h4>
                            <div class="table-responsive">
                                <table class="table table-hover">
                                    <thead>
                                        <tr>
                                        <th scope="col">№</th>
                                        <th scope="col">ID заказа</th>
                                        <th scope="col">Изображение</th>
                                        <th scope="col">Наименование</th>
                                        <th scope="col">Пункт выдачи</th>
                                        <th scope="col">Сумма заказа</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="order, index in orderHistory">
                                            <th scope="row">{{index+1}}</th>
                                            <td>{{order.id}}</td>
                                            <td>
                                                <img v-if="order.order_products[0].product.product_images.length > 0" :src=order.order_products[0].product.product_images[0].image :alt=order.order_products[0].product.product_images[0].alt height="100px">
                                                <img v-else src="@/assets/no_image.png" alt="no image" height="100px">
                                            </td>
                                            <td>{{ order.order_products[0].product.name }}</td>
                                            <td>Маг. Мозаика</td>
                                            <td>{{ order.total_amount }} &#8381;</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </div>
    <modal-component v-model:show="showUploadAvatar">
        <upload-avatar-form v-model:show="showUploadAvatar">
        </upload-avatar-form>
    </modal-component>
    <modal-component v-model:show="QRModal">
        <div class="d-flex flex-column gap-3">
            <h2>Заказ №: {{qr_order.id}}</h2>
            <qrcode-vue :value="qr_order.uuid" :size="400"></qrcode-vue>
        </div>
    </modal-component>
    <footer-component></footer-component>
</template>

<script>
    import axios from 'axios'
    import QrcodeVue from 'qrcode.vue'
    export default {
        components: {QrcodeVue},
        data() {
            return {
                isCabinetLoad: true,
                ready_orders: [],
                processing_orders: [],
                orderHistory: [],
                showUploadAvatar: false,
                QRModal: false,
                qr_order: null
            }
        },
        methods: {
            async getUserOrders() {
                try {
                      axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/order/get_ready_orders/`,
                          method: 'get',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          timeout: 1000
                        }
                      ).then((response) => {
                            if (response.status == 401){
                                //Врзможно устаревший token или неверный

                            }
                            this.ready_orders = response.data
                            //console.log(response.data)
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },
            async getProcessingOrders() {
                try {
                      axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/order/get_proccessing_orders/`,
                          method: 'get',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          timeout: 1000
                        }
                      ).then((response) => {
                            this.processing_orders = response.data
                            //console.log(response.data)
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },
            async getOrderHistory() {
                try {
                      axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/order/get_history_orders/`,
                          method: 'get',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          timeout: 1000
                        }
                      ).then((response) => {
                            this.orderHistory = response.data
                            //console.log(response.data)
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },
            userLogout() {
                this.$store.commit('logoutUser')
                this.$router.push('newfront')
            },
            uploadAvatar() {
                this.showUploadAvatar = true
            },
            showQRModal(order){
                this.qr_order = order
                this.QRModal = true
            }
        },
        mounted() {
            this.getUserOrders()
            this.getProcessingOrders()
        }
    }
</script>

<style scoped>

</style>