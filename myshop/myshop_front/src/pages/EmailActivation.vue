<template>
    <HeaderComponent></HeaderComponent>
    <div class="container pt-5 pb-5">
        <h1>Email Activation</h1>
        <p>We send activation email. Please Activate you acount!</p>
        <button type="button" class="btn btn-success" @click="$router.push('/')">Ok</button>
    </div>
    <FooterComponent></FooterComponent>
</template>

<script>
    import HeaderComponent from '@/components/HeaderComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
    export default {
        components: {HeaderComponent, FooterComponent},

    }
</script>

<style scoped>

</style>