<template>
    <div v-if="messages.length > 0">
        <div class="alert alert-danger" role="alert" v-for="message in messages">
            Ошибка в поле {{ message.field }} : {{ message.error }}
        </div>
    </div>
    <form @submit.prevent>
        <div class="d-flex flex-column">
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="phoneInput" class="col-sm-2 form-label">Номер телефона:</label>
                </div>
                <div class="col-sm-9">
                    <!--
                    <input 
                        v-bind:value="phone" 
                        @input="inputPhone" 
                        type="text" 
                        class="form-control" 
                        autocomplete="tel-area-code" 
                        id="phone" 
                        value="+7(___)___-__-__"
                        pattern="\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}"
                        placeholder="+7(___)___-__-__">
                    -->
                    <input 
                        type="tel"
                        @input="inputPhone"
                        class="form-control"
                        autocomplete="tel-national"
                        id="phoneInput"
                        value=""
                        v-mask="['(+7) ###-###-##-##']">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputPassword" class="col-sm-2 form-label">Пароль:</label>
                </div>
                <div class="col-sm-9">
                    <input v-bind:value="password" @input="inputPassword" type="password" autocomplete="new-password" class="form-control" id="inputPassword">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputPasswordConfirm" class="col-sm-2 form-label">Подтвердить пароль:</label>
                </div>
                <div class="col-sm-9">
                <input v-bind:value="confirmPassword" @input="inputPasswordConfirm" type="password" autocomplete="new-password" class="form-control" id="inputPasswordConfirm">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputFirstName" class="col-sm-2 form-label">Имя</label>
                </div>
                <div class="col-sm-9">
                    <input v-bind:value="firstName" @input="inputFirstName" type="text" autocomplete="given-name" class="form-control" id="inputFirstName">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputLastName" class="col-sm-2 form-label">Фамилия</label>
                </div>
                <div class="col-sm-9">
                    <input v-bind:value="lastName" @input="inputLastName" type="text" autocomplete="family-name" class="form-control" id="inputLastName">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputEmail" class="col-sm-2 form-label">Email:</label>
                </div>
                
                <div class="col-sm-9">
                    <input v-bind:value="email" @input="inputEmail" type="email" @keyup.enter="registerUser" autocomplete="email" class="form-control" id="inputEmail">
                </div>
            </div>
            <div class="row d-flex align-items-end mb-3">
                <button type="button" class="btn btn-success " @click="registerUser">Регистрация</button>
            </div>
        </div>
    </form>
</template>

<script>
    import axios from 'axios';
    import { mask } from 'vue-the-mask';
    export default {
    name: 'registration-form',
    directives: { mask },
    props: {
        show: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            phone: '',
            password: '',
            confirmPassword: '',
            email: '',
            firstName: '',
            lastName: '',
            messages: []
        };
    },
    methods: {
        inputPhone(event) {
            this.phone = event.target.value;
        },
        inputPassword(event) {
            this.password = event.target.value;
        },
        inputEmail(event) {
            this.email = event.target.value;
        },
        inputPasswordConfirm(event) {
            this.confirmPassword = event.target.value;
        },
        inputFirstName(event) {
            this.firstName = event.target.value;
        },
        inputLastName(event) {
            this.lastName = event.target.value;
        },
        registerUser() {
            this.messages = []
            if (this.phone.length < 12) {
                this.messages.push({'field': '"Номер телефона"', 'error': 'Неправильный номер телефона!'})
                return
            }
            if (this.password.length < 3){
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
            if (this.password === this.confirmPassword){
                axios({
                    method: 'post',
                    url: `${this.$store.state.apiUrl}/api/v1/customers/`,
                    headers: { 'Content-Type': 'application/json;charset=utf-8' },
                    data: JSON.stringify({
                        'phone_number': this.phone, 
                        'password': this.password, 
                        'email': this.email,
                        'first_name': this.firstName,
                        'last_name': this.lastName
                    })
                })
                .then((response) => {
                    this.$emit('update:show', false);
                    this.$router.push('email_activation');
                })
                .catch((error) => {
                    if (error.response) {
                        for (let index in error.response.data) {
                            this.messages.push({'field': index, 'error': error.response.data[index]});
                        }
                        this.message = error.response;
                    }
                });
            }
            else {
                this.messages.push({'field': 'Пароль', 'error': 'Пароли не совпадают!'})
            }
        }
    },
}
</script>

<style scoped>

</style>