<template>
    <HeaderComponent></HeaderComponent>
    <div class="container-lg widget-area" v-if="$store.state.userIsAuth">
        <widget-component class="pt-5 pb-5">
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
        </widget-component> 
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