<template>
    <div v-if="messages.length > 0">
        <div class="alert alert-danger" role="alert" v-for="message in messages">
            {{ message }}
        </div>
    </div>
    <form @submit.prevent>
        <div class="d-flex flex-column">
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="phone" class="col-sm-2 form-label">Номер телефона:</label>
                </div>
                <div class="col-sm-9">
                    <!--
                    <input v-bind:value="phone" @input="inputPhone" type="text" class="form-control" autocomplete="tel-area-code" id="phone" value="+79999999999">
                    -->
                    <input 
                        type="tel"
                        v-bind:value="phone"
                        @input="inputPhone"
                        class="form-control"
                        autocomplete="tel-area-code"
                        id="phone"
                        value=""
                        v-mask="['(+7) ###-###-##-##']"
                        @keyup.enter="loginUser">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputPassword" class="col-sm-2 form-label">Пароль:</label>
                </div>
                
                <div class="col-sm-9">
                <input v-bind:value="password" @input="inputPassword" @keyup.enter="loginUser" type="password" autocomplete="new-password" class="form-control" id="inputPassword">
                </div>
            </div>
            <div class="row d-flex align-items-end">
                <button type="button" class="btn btn-success " @click="loginUser" >Войти</button>
            </div>
        </div>
    </form>
</template>

<script>
    import axios from 'axios';
    import { mask } from 'vue-the-mask';
    export default {
        name: 'login-form',
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
                messages: []
            }
        },
        methods: {
            inputPhone(event) {
                this.phone = event.target.value
            },
            inputPassword(event) {
                this.password = event.target.value
            },
            loginUser() {
                this.messages = []
                if (this.phone.length<12) {
                    this.messages.push('Phone number wrong!')
                    return
                }
                if (this.password.length<3) {
                    this.messages.push('Password wrong!')
                    return
                }
                axios(
                    {
                        method: 'post',
                        url: 'http://127.0.0.1:8000/api/v1/token/login/',
                        headers: {'Content-Type': 'application/json;charset=utf-8'},
                        data: JSON.stringify({'phone_number': this.phone, 'password': this.password})
                    }
                )
                .then((response) => {
                    const token = response.data.access
                    axios(
                        {
                            method: 'get',
                            url: `http://127.0.0.1:8000/api/v1/customers/${response.data.user_id}/`,
                            headers: {'Content-Type': 'application/json;charset=utf-8', "Authorization" : `Bearer ${token}`},
                        }
                    )
                    .then((response) => {
                        console.log(response.data)
                        //this.$store.commit('setUser2', response.data)
                        this.$store.commit('setUser', response.data)
                        //useStorage('user', JSON.stringify({'access_token': response.data.access}))
                        this.$emit('update:show', false)
                    })
                    .catch((error) => {
                        console.log(error)
                    })
                })
                .catch((error) => {
                    if (error.response.data.error) {
                        this.messages.push(error.response.data.error)
                    }
                })
            }
        },
    }
</script>

<style scoped>

</style>