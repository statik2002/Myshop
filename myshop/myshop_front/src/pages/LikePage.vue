<template>
    <HeaderComponent></HeaderComponent>

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

            }
        },
        methods: {},

        mounted() {

        }
    }
</script>

<style scoped>

</style>