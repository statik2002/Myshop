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
                    <label for="phone" class="col-sm-2 form-label">Phone number:</label>
                </div>
                <div class="col-sm-9">
                    <input 
                        type="tel"
                        @input="inputPhone"
                        class="form-control"
                        autocomplete="tel-area-code"
                        id="phone"
                        :value=phoneNumber
                        v-mask="['(+7) ###-###-##-##']">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputFirstName" class="col-sm-2 form-label">First name:</label>
                </div>
                <div class="col-sm-9">
                <input v-bind:value="firstName" @input="inputFirstName" type="text" autocomplete="first name" class="form-control" id="inputFirstName">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputLastName" class="col-sm-2 form-label">Last name:</label>
                </div>
                <div class="col-sm-9">
                <input v-bind:value="lastName" @input="inputLastName" type="text" autocomplete="last-name" class="form-control" id="inputLastName">
                </div>
            </div>
            <div class="row d-flex align-items-end">
                <button type="button" class="btn btn-success " @click="saveUser">Save</button>
            </div>
        </div>
    </form>
</template>

<script>
    import { mask } from 'vue-the-mask';
    import axios from 'axios';
    export default {
        name: 'user-edit',
        directives: { mask },
        props: {
            show: {
                type: Boolean,
                default: false
            }
        },
        data() {
            return {
                messages: [],
                firstName: '',
                lastName: '',
                phoneNumber: ''
            }
        },
        methods: {
            inputPhone(event) {
                this.phoneNumber = event.target.value;
            },
            inputFirstName(event) {
                this.firstName = event.target.value;
            },
            inputLastName(event) {
                this.lastName = event.target.value;
            },
            saveUser() {
                axios({
                    method: 'post',
                    url: 'http://127.0.0.1:8000/api/v1/customers/customer_update/',
                    headers: { 'Content-Type': 'application/json;charset=utf-8' },
                    data: JSON.stringify({
                        'customer_id': this.$store.state.user.id, 
                        'phone_number': this.phoneNumber, 
                        'firstName': this.firstName, 
                        'lastName': this.lastName,
                        'email': this.$store.state.email
                    })
                })
                .then((response) => {
                    if (response.data.response == 'ok') {
                        this.$store.commit('updateUser', {'first_name': this.firstName, 'last_name': this.lastName})
                        this.$emit('update:show', false);
                    }
                    
                    console.log(response)
                })
                .catch((error) => {
                    if (error.response) {
                        for (let index in error.response.data) {
                            this.messages.push({ 'field': index, 'error': error.response.data[index] });
                        }
                        this.message = error.response;
                        console.log(error)
                    }
                });
                this.$emit('update:show', false);
            }
        },
        mounted() {
            this.firstName = this.$store.state.user.first_name
            this.lastName = this.$store.state.user.last_name
            this.phoneNumber = this.$store.state.user.phone_number
        }
    }
</script>

<style scoped>

</style>