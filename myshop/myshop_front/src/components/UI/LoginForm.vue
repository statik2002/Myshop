<template>
    <form @submit.prevent>
        <div class="d-flex flex-column">
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="phone" class="col-sm-2 form-label">Phone number:</label>
                </div>
                <div class="col-sm-9">
                    <input v-bind:value="phone" @input="inputPhone" type="text" class="form-control" autocomplete="tel-area-code" id="phone" value="+79999999999">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputPassword" class="col-sm-2 form-label">Password:</label>
                </div>
                
                <div class="col-sm-9">
                <input v-bind:value="password" @input="inputPassword" type="password" autocomplete="new-password" class="form-control" id="inputPassword">
                </div>
            </div>
            <div class="row d-flex align-items-end">
                <button type="button" class="btn btn-success " @click="loginUser">Login</button>
            </div>
        </div>
    </form>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'login-form',
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
                console.log( JSON.stringify({'phone_number': this.phone, 'password': this.password}))
                axios(
                    {
                        method: 'post',
                        url: 'http://127.0.0.1:8000/api/token/',
                        headers: {'Content-Type': 'application/json;charset=utf-8'},
                        data: JSON.stringify({'phone_number': this.phone, 'password': this.password})
                    }
                )
                .then((response) => {
                    console.log(response)
                    //commit('setUser', {'access_token': response.data.access})
                    this.$store.dispatch('setUser', {'access_token': response.data.access})
                    this.$emit('update:show', false)
                })
                .catch((error) => {
                    console.log(error)
                })
            }
        }
    }
</script>

<style scoped>

</style>