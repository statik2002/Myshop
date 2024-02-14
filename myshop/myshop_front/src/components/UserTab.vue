<template>
    <div class="d-flex">
        <div class="dropdown" v-if="Object.entries($store.state.user).length === 0">
            <a class="btn btn-link" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                <i class="bi bi-door-open" style="font-size: 1.5rem;"></i>
            </a>
            <ul class="dropdown-menu bg-dark" aria-labelledby="dropdownMenuLink">
                <li><a class="dropdown-item" href="#" @click="showRegistrationDialog">Registration</a></li>
                <li><a class="dropdown-item" href="#" @click="showLoginDialog">Login</a></li>
                <li><a class="dropdown-item" href="#">Rules</a></li>
            </ul>
        </div>
        <div class="dropdown" v-else>
            <a class="btn btn-link" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                <i class="bi bi-person-circle" style="font-size: 1.5rem;"></i>
            </a>
            <ul class="dropdown-menu bg-dark" aria-labelledby="dropdownMenuLink">
                <li><a class="dropdown-item" href="#">Cabinet</a></li>
                <li><a class="dropdown-item" href="#">Cart</a></li>
                <li><a class="dropdown-item" href="#">Delivery</a></li>
            </ul>
        </div>
        <modal-component v-model:show="loginModalVisible">
            <login-form v-model:show="loginModalVisible"></login-form>
        </modal-component>
        <modal-component v-model:show="registrationModalVisible">
            <registration-form v-model:show="registrationModalVisible"></registration-form>
        </modal-component>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                userIsAuthenticated: false,
                loginModalVisible: false,
                registrationModalVisible: false,
                phone: '',
                password: ''
            }
        },
        methods: {
            showLoginDialog() {
                this.loginModalVisible = true
            },
            showRegistrationDialog() {
                this.registrationModalVisible = true
            },
            inputPhone(event) {
                this.phone = event.target.value
            },
            inputPassword(event) {
                this.password = event.target.value
            },
            saveUserData() {
                this.$store.dispatch('loginUser', {'phone': this.phone, 'password': this.password})
                    .then(
                        console.log('login OK')
                    )
                this.loginModalVisible = false
            }
        },
    }
</script>

<style scoped>

</style>