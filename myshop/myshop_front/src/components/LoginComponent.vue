<template>
    <div>
        <form class="login" @submit.prevent="login">
            <h1>Sign in</h1>
            <label>Email</label>
            <input required v-model="email" type="email" placeholder="Name"/>
            <label>Password</label>
            <input required v-model="password" type="password" placeholder="Password"/>
            <hr/>
            <button type="submit" @click="login">Login</button>
        </form>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                phone: "",
                password: ""
            }
        },
        methods: {
            login() {
                this.$store.dispatch('loginUser', {'phone': phone, 'password': password})
                    .then(
                        console.log('login OK')
                    )
                    .catch(
                        console.log('login Error')
                    )
            }
        }
    }
</script>

<style scoped>

</style>