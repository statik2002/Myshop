<template>
    <div class="wrapper">
        <header-component></header-component>
        <div class="container pt-5 pb-5">
            <h1>Активация почты</h1>
            <p>
                Мы отправили письмо с кодом активации на указанный вами e-mail. Для полноценного использования интернет магазином, необходимо активировать 
                аккаунт перейдя по ссылке которое будет в письме.
            </p>
            <button type="button" class="btn btn-success" @click="$router.push('/')">Ok</button>
        </div>
        <footer-component></footer-component>
    </div>
</template>

<script>

    export default {


    }
</script>

<style scoped>

</style>