<template>
    <div class="">
        <div class="btn" v-if="!$store.getters.isUserLogin">
            <a class="btn btn-link" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                <i class="bi bi-door-open" style="font-size: 1.5rem;"></i>
                <span>Войти</span>
            </a>
            <ul class="dropdown-menu bg-dark" aria-labelledby="dropdownMenuLink">
                <li><a class="dropdown-item" href="#" @click="showRegistrationDialog">Регистрация</a></li>
                <li><a class="dropdown-item" href="#" @click="showLoginDialog">Логин</a></li>
                <li><a class="dropdown-item" href="#">Правила</a></li>
            </ul>
        </div>
        <div class="btn" v-else>
            <a class="" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                <img :src="$store.state.user.avatar" alt="avatar" class="menu-avatar" v-if="$store.state.user.avatar">
                <img src="@/assets/avatar_blank.webp" alt="avatar" class="menu-avatar" v-else>
                <span>Кабинет</span>
            </a>
            <ul class="dropdown-menu bg-dark" aria-labelledby="dropdownMenuLink">
                <li><routerLink to="/cabinet" class="dropdown-item">Кабинет</routerLink></li>
                <li><router-link to="/cart" class="dropdown-item">Корзина</router-link></li>
                <li><router-link to="/orders" class="dropdown-item">Заказы</router-link></li>
                <li><router-link to="/likes" class="dropdown-item">Избранное</router-link></li>
                <li><a class="dropdown-item" href="#" @click="userLogout">Logout</a></li>
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
                password: '',
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
            changeUserAuthState() {
                this.userIsAuthenticated = value
            },
            userLogout() {
                this.$store.dispatch('saveUserCartToServer')
                this.$store.commit('logoutUser')
                this.$router.push('/')
            },
            userLogin(){
                return $store.getters.isUserLogin
            }
        },
        mounted() {
        }
    }
</script>

<style scoped>

</style>