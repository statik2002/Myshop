<template>
    <div>
    <h4>Register</h4>
        <form @submit.prevent="register">
            <label for="firstName">First Name</label>
            <div>
                <input id="firstName" type="text" v-model="firstName" required autofocus>
            </div>
            <label for="lastName">Last Name</label>
            <div>
                <input id="lastName" type="text" v-model="lastName" required autofocus>
            </div>
            <label for="email">Email</label>
            <div>
                <input id="email" type="email" v-model="email" required autofocus>
            </div>
            <label for="phone">Phone</label>
            <div>
                <input id="phone" type="tel" v-model="phone" required>
            </div>
            <label for="password">Password</label>
            <div>
                <input id="password" type="password" v-model="password" required>
            </div>
            <label for="password-confirm">Confirm Password</label>
            <div>
                <input id="password-confirm" type="password" v-model="password_confirmation" required>
            </div>
            <div>
                <button type="submit">Register</button>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                phone: "",
                password: "",
                password_confirmation: "",
                is_admin: null,
                email: "",
                firstName: "",
                lastName: ""
            }
        },
        methods: {
            register() {
                const data = {
                    first_name: this.firstName,
                    last_name: this.lastName,
                    phone_number: this.phone,
                    email: this.email,
                    password: this.password,
                    password_confirmation: this.password_confirmation,
                    is_admin: this.is_admin
                }
                this.$store.dispatch('registerUser', data)
                    .then(
                        () => this.$router.push('/')
                    )
                    .catch(err => console.log(err))
            }
        }
    }
</script>

<style scoped>

</style>