<template>
    <HeaderComponent></HeaderComponent>
    <div class="container-lg widget-area" v-if="$store.state.userIsAuth">
        <div class="d-flex flex-column mb-2" style="font-size: 0.9em;">
            <div class="row pt-5">
                <!--Active orders-->
                <widget-component>
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
                                <span>В процессе</span>
                            </div>
                            </div>
                        </div>
                    </div>
                </widget-component>
                <!--User wodget-->
                <widget-component>
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
                                <div class="ms-auto"><a href="#" @click="userLogout">Выйти</a></div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                </widget-component>
                <!--Discount widget-->
                <widget-component>
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
                </widget-component>
            </div>
            <div class="row mt-3">
                <!--Payment-->
                <widget-component>
                    <div class="col-lg-3 col-md-6 mb-3">
                        <div class="widget p-3 h-100">
                            <div class="d-flex flex-column align-items-start gap-2 h-100">
                            <div class="fw-bold">Ваша карта</div>
                            <div class="d-flex gap-2">
                                <div class=""><i class="bi bi-credit-card"></i></div>
                                <div class="">**** **** **** 7777</div>
                            </div>
                            <div class="mt-auto">
                                <a href="#">Добавить карту</a>
                            </div>
                            </div>
                        </div>
                        </div>
                </widget-component>
                <!--Address widget-->
                <widget-component>
                    <div class="col-lg-3 col-md-6 mb-3">
                        <div class="widget p-3 h-100">
                            <div class="d-flex flex-column align-items-start gap-2 h-100">
                                <div class="fw-bold">Ваша адрес:</div>
                                <div>
                                    <div class="d-flex gap-2">
                                        <div class=""><i class="bi bi-house"></i></div>
                                        <div>
                                            <div class="">Братск</div>
                                            <div>Ленина д. 32 кв. 134</div>
                                        </div>
                                    </div>
                                </div>
                                <div class="mt-auto">
                                    <a href="#">Изменить адрес</a>
                                </div>     
                            </div>                     
                        </div>
                    </div>
                </widget-component>
                <!--Pick point widget-->
                <widget-component>
                    <div class="col-lg-3 col-md-6 mb-3">
                        <div class="widget p-3 h-100">
                            <div class="d-flex flex-column align-items-start gap-2 h-100">
                                <div class="fw-bold">Ваш пункт выдачи</div>
                                <div v-if="$store.state.user.pickpoint" class="d-flex flex-column gap-2">
                                    <div>
                                        <i class="bi bi-shop"></i>
                                        {{ $store.state.user.pickpoint.name }}
                                    </div>
                                    <div>
                                        <i class="bi bi-geo-alt"></i>
                                        {{ $store.state.user.pickpoint.address }}
                                    </div>
                                    <div>
                                        <i class="bi bi-telephone"></i>
                                        {{ $store.state.user.pickpoint.phone ? $store.state.user.pickpoint.phone : '' }}
                                    </div>
                                </div>
                                <div v-else>Нет выбранных пунктов выдачи</div>
                                <div class="mt-auto">
                                    <a href="#">Изменить пункт выдачи</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </widget-component>
                <!--Likes widget-->
                <widget-component>
                    <div class="col-lg-3 col-md-6 mb-3">
                        <div class="widget p-3 h-100">
                            <div class="d-flex flex-column align-items-start gap-2 h-100">
                                <div class="fw-bold">Ваши любимые товары</div>
                                <div class="" style="font-size: 0.8em;" v-for="item in likedProducts">
                                    <a href="#" class="d-flex gap-2">
                                        <router-link :to="{name: 'product', params: {id: item.id}}">{{ item.name }}</router-link>
                                    </a>
                                </div>
                                <div class="mt-auto">
                                    <router-link to="/likes">Все любимые товары</router-link>
                                </div>
                            </div>
                        </div>
                    </div>
                </widget-component>
            </div>
            <div class="row mt-3">
                <!--Last orders-->
                <widget-component>
                    <div class="col-lg-6 col-md-12 mb-3">
                        <div class="widget p-3 h-100">
                            <div class="d-flex flex-column align-items-start gap-2 h-100">
                            <div class="fw-bold">Ваши последние заказы</div>
                            <div v-for="order in processing_orders.slice(0,3)" class="d-flex justify-content-start">
                                <div class="">{{ $FormatDate(order.order_create) }}</div>
                                <div class="ms-5">Товаров: {{ order.order_products.length }}</div>
                                <div class="ms-5">На сумму: {{ order.total_amount }} &#8381;</div>
                            </div>
                            <div class="mt-auto">
                                <router-link to="/orders">История заказов</router-link>
                            </div>
                            </div>
                            
                        </div>
                    </div>
                </widget-component>
                <!--Some widget-->
                <widget-component>
                    <div class="col-lg-6 col-md-12 mb-3">
                        <div class="widget p-3 w-100">
                            <div class="d-flex flex-column align-items-start gap-2 h-100">
                            <div class="fw-bold">Избранное</div>
                            <div>
                                <a href="#" class="d-flex gap-2">
                                <div class=""><i class="bi bi-paint-bucket"></i></div>
                                <div class="">Краска Текс 1,5кг</div>
                                </a>
                                <a href="#" class="d-flex gap-2">
                                <i class="bi bi-brush"></i>
                                Кисть мялярная 23см
                                </a>
                                <a href="#" class="d-flex gap-2">
                                <i class="bi bi-hammer"></i>
                                Молоток слесарный 250гр.
                                </a>
                            </div>
                            <div class="mt-auto">
                                <a href="#">Все избранные товары</a>
                            </div>
                            </div>
                        </div>
                    </div>
                </widget-component>
            </div>
        </div>
    </div>
    <div class="container-lg widget-area" v-else>
        User in not login!
    </div>
    <modal-component v-model:show="showReadyOrdersModal">
        <div class="d-flex flex-column gap-2">
            <div v-for="order in ready_orders" v-if="ready_orders.length > 0">
                <order-item :order="order" @click="$router.push({name: 'show_order', params: {'id': order.id}})"></order-item>
            </div>
            <div v-else>
                Готовых к выдаче заказов нет
            </div>
        </div>
    </modal-component>
    <modal-component v-model:show="showProcessingOrdersModal">
        <div class="d-flex flex-column gap-2">
            <div v-for="order in processing_orders" v-if="processing_orders.length > 0">
                <order-item :order="order" @click="$router.push({name: 'show_order', params: {'id': order.id}})"></order-item>
            </div>
            <div v-else>
                Заказов в обработке нет
            </div>
        </div>
    </modal-component>
    <modal-component v-model:show="showUserEditModal">
        <div class="d-flex flex-column gap-2">
            <user-edit v-model:show="showUserEditModal"></user-edit>
        </div>
    </modal-component>
    <modal-component v-model:show="showUploadAvatar">
        <upload-avatar-form v-model:show="showUploadAvatar">
        </upload-avatar-form>
    </modal-component>
    <FooterComponent></FooterComponent>
</template>

<script>
    import axios from 'axios'
    import HeaderComponent from '@/components/HeaderComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
    export default {
        components: { HeaderComponent, FooterComponent },
        data() {
            return {
                ready_orders: [],
                processing_orders: [],
                likedProducts: [],
                showReadyOrdersModal: false,
                showProcessingOrdersModal: false,
                showUserEditModal: false,
                showUploadAvatar: false,
            }
        },
        methods: {
            async refreshToken() {
                try {
                      axios(
                        {
                          url: `${this.$store.state.apiUrl}/api/v1/order/get_ready_orders/`,
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

            async getUserOrders() {
                try {
                      axios(
                        {
                          url: `${this.$store.state.apiUrl}/api/v1/order/get_ready_orders/`,
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
                          url: `${this.$store.state.apiUrl}/api/v1/order/get_proccessing_orders/`,
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

            async get_likes_products(num) {
                const likedProducts = this.$store.state.user.likes.slice(0, num)
                try {
                      axios(
                        {
                          url: `${this.$store.state.apiUrl}/api/v1/like/get_sliced_liked_products/`,
                          method: 'post',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          data: likedProducts,
                          timeout: 1000
                        }
                      ).then((response) => {
                            this.likedProducts=response.data
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },

            showReadyOrders() {
                this.showReadyOrdersModal = true
            },

            showProcessingOrders() {
                this.showProcessingOrdersModal = true
            },

            showUserEdit() {
                this.showUserEditModal = true
            },

            userLogout() {
                this.$store.commit('logoutUser')
                this.$router.push('/')
            },

            uploadAvatar() {
                this.showUploadAvatar = true
            },
        },
        mounted() {
            this.getUserOrders()
            this.getProcessingOrders()
            this.get_likes_products(3)
        }
    }
</script>

<style scoped>

</style>