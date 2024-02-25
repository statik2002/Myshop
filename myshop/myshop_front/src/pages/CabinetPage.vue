<template>
    <HeaderComponent></HeaderComponent>
    <div class="container-lg widget-area" v-if="$store.state.userIsAuth">
        <div class="d-flex flex-column mb-2" style="font-size: 0.9em;">
            <div class="row pt-5">
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
                                    <div class="h4">Заказы</div>
                                </div>
                                </div>
                            </div>
                            <div class="d-flex justify-content-between">
                                <span class="text-secondary">Ближайшие</span>
                                <span>Не ожидается</span>
                            </div>
                            </div>
                        </div>
                        </div>
                </widget-component>
                <widget-component>
                    <div class="col-xxl-4 col-xl-4 col-lg-4 col-md-6 col-sm-6 mb-3">
                        <div class="widget p-3 h-100">
                            <div class="d-flex flex-column justify-content-between h-100">
                            <div class="d-flex">
                                <div class="col-auto">
                                <div class="circle">
                                    <div v-if="$store.state.user.avatar">
                                        <div class="cabinet-avatar"><img :src="$store.state.user.avatar" alt="avatar" class=""></div>
                                    </div>
                                    <div v-else class="cabinet-avatar"><img src="@/assets/avatar_blank.webp" alt="avatar" class=""></div>
                                </div>
                                </div>
                                <div class="col align-self-center">
                                <div class="ms-2">{{ $store.state.user.first_name }}</div>
                                <div class="ms-2">{{ $store.state.user.last_name }}</div>
                                </div>
                                <div class="col-auto">
                                <div class="ms-auto"><a href="#"><i class="bi bi-bell text-success"></i></a></div>
                                </div>
                            </div>
                            <div class="row mt-2">
                                <div class="col">
                                <div class=""><span class="text-secondary">Телефон:</span>{{ $store.state.user.phone_number }}</div>
                                </div>
                                <div class="col-auto">
                                <div class="ms-auto"><a href="#">Выйти</a></div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                </widget-component>
                <widget-component>
                    <div class="col-xxl-4 col-xl-4 col-lg-4 col-md-6 col-sm-6 mb-3">
                        <div class="widget p-3 h-100">
                            <div class="d-flex flex-column justify-content-between h-100">
                            <div class="">
                                <div class="row">
                                <div class="col-auto">
                                    <div class="circle">
                                    <div class="text-at-circle">5%</div>
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
                <widget-component>
                    <div class="col-lg-3 col-md-6 mb-3">
                        <div class="widget p-3 h-100">
                            <div class="d-flex flex-column align-items-start gap-2 h-100">
                                <div class="fw-bold">Ваш пункт выдачи</div>
                                <div class="d-flex gap-2">
                                    <i class="bi bi-shop"></i>
                                    ул. Ленина д. 1
                                </div>
                                <div class="mt-auto">
                                    <a href="#">Изменить пункт выдачи</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </widget-component>
                <widget-component>
                    <div class="col-lg-3 col-md-6 mb-3">
                        <div class="widget p-3 h-100">
                            <div class="d-flex flex-column align-items-start gap-2 h-100">
                                <div class="fw-bold">Ваши любимые товары</div>
                                <div class="" style="font-size: 0.8em;">
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
                                    <a href="#">Все любимые товары</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </widget-component>
            </div>
            <div class="row mt-3">
                <widget-component>
                    <div class="col-lg-6 col-md-12 mb-3">
                        <div class="widget p-3 h-100">
                            <div class="d-flex flex-column align-items-start gap-2 h-100">
                            <div class="fw-bold">Ваши  последние покупки</div>
                            <div class="d-flex justify-content-start">
                                <div class="">21.10.2023</div>
                                <div class="ms-5">Товаров: 5</div>
                                <div class="ms-5">На сумму: 2321 &#8381;</div>
                            </div>
                            <div class="d-flex justify-content-start">
                                <div class="">11.11.2023</div>
                                <div class="ms-5">Товаров: 1</div>
                                <div class="ms-5">На сумму: 245 &#8381;</div>
                            </div>
                            <div class="mt-auto">
                                <a href="#">История покупок</a>
                            </div>
                            </div>
                            
                        </div>
                    </div>
                </widget-component>
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
    <FooterComponent></FooterComponent>
</template>

<script>
    import HeaderComponent from '@/components/HeaderComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
    export default {
        components: { HeaderComponent, FooterComponent },
    }
</script>

<style scoped>

</style>