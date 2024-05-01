<template>
    <header-component></header-component>
    <div class="container py-5">
        <div class="login-wrap">
            <div class="account-form-wrap">
                <div class="login-form">
                    <div class="content">
                        <h4 class="title">Регистрация</h4>
                        <p>Введите ваши учетные данные.</p>
                    </div>
                    <div class="content">
                        <div class="d-flex flex-column" v-for="message in messages">
                            <div>В поле "{{ message.field }}" ошибка "{{ message.error }}"</div>
                        </div>
                    </div>
                    <form @submit.prevent>
                        <div class="row">
                            <div class="col-12">
                                <div class="form-group">
                                    <input v-model="phone" class="form-control" type="text" placeholder="+7 999 999 99 99" autocomplete="username" v-mask="['(+7) ###-###-##-##']">
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-group">
                                    <input v-model="password1" class="form-control" type="password" placeholder="пароль" autocomplete="current-password">
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-group">
                                    <input v-model="password2" class="form-control" type="password" placeholder=" повторите пароль" autocomplete="current-password">
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-group">
                                    <input v-model="firstName" class="form-control" type="text" placeholder="Имя" autocomplete="given-name">
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-group">
                                    <input v-model="lastName" class="form-control" type="text" placeholder="Фамилия" autocomplete="family-name">
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="form-group">
                                    <input v-model="email" class="form-control" type="email" placeholder="Email" autocomplete="email">
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="d-flex justify-content-center">
                                    <div class="login-form-group">
                                        <button class="btn-sign" type="submit" @click="registerUser">Зарегистрироваться</button>
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <footer-component></footer-component>
</template>

<script>
    import axios from 'axios'
    import { mask } from 'vue-the-mask';
    export default {
        directives: { mask },
        data() {
            return {
                phone: '',
                password1: '',
                password2: '',
                firstName: '',
                lastName: '',
                email: '',
                messages: []
            }
        },
        methods: {
            registerUser() {
                this.messages = []
                if (this.phone.length < 12) {
                    this.messages.push({'field': '"Номер телефона"', 'error': 'Неправильный номер телефона!'})
                    return
                }
                if (this.password1.length < 3){
                    this.messages.push({'field': 'Пароль', 'error': 'Пароль не соответствует требованиям!'})
                    return
                }
                if (this.email.length < 8) {
                    this.messages.push({'field': 'Email', 'error': 'Не правильный email!'})
                    return
                }
                if (this.firstName.length < 2) {
                    this.messages.push({'field': 'Имя', 'error': 'Введите ваше имя!'})
                    return
                }
                if (this.lastName.length < 2) {
                    this.messages.push({'field': 'Фамилия', 'error': 'Введите вашу фамилию!'})
                    return
                }
                if (this.password1 === this.password2){
                    axios({
                        method: 'post',
                        url: `${this.$store.state.apiUrl}/api/v1/customers/`,
                        headers: { 'Content-Type': 'application/json;charset=utf-8' },
                        data: JSON.stringify({
                            'phone_number': this.phone, 
                            'password': this.password1, 
                            'email': this.email,
                            'first_name': this.firstName,
                            'last_name': this.lastName
                        })
                    })
                    .then((response) => {
                        this.$router.push('email_activation');
                    })
                    .catch((error) => {
                        if (error.response) {
                            for (let index in error.response.data) {
                                this.messages.push({ 'field': index, 'error': error.response.data[index] });
                            }
                            this.message = error.response;
                        }
                    });
                }
                else {
                    this.messages.push({'field': 'Пароль', 'error': 'Пароли не совпадают!'})
                }
            }
        }
    }
</script>

<style scoped>

</style>