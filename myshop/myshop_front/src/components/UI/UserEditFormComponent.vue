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
                    <label for="phone" class="col-sm-2 form-label">Номер телефона:</label>
                </div>
                <div class="col-sm-9">
                    <input 
                        type="tel"
                        @input="inputPhone"
                        class="form-control"
                        autocomplete="tel-national"
                        id="phone"
                        :value=phoneNumber
                        v-mask="['(+7) ###-###-##-##']">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputFirstName" class="col-sm-2 form-label">Имя:</label>
                </div>
                <div class="col-sm-9">
                <input v-bind:value="firstName" @input="inputFirstName" type="text" autocomplete="given-name" class="form-control" id="inputFirstName">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputLastName" class="col-sm-2 form-label">Фамилия:</label>
                </div>
                <div class="col-sm-9">
                <input v-bind:value="lastName" @input="inputLastName" type="text" autocomplete="family-name" class="form-control" id="inputLastName">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="inputAddress" class="col-sm-2 form-label">Адрес:</label>
                </div>
                <div class="col-sm-9">
                    <input v-bind:value="address" @input="inputAddress" type="text" autocomplete="address-level1" class="form-control" id="inputAddress">
                </div>
            </div>
            <div class="row d-flex align-items-end">
                <button type="button" class="btn btn-success " @click="saveUser">Сохранить</button>
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
                phoneNumber: '',
                address: '',
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
            inputAddress(event) {
                this.address = event.target.value;
            },
            saveUser() {
                axios({
                    method: 'post',
                    url: `${this.$store.state.apiUrl}/api/v1/customers/customer_update/`,
                    headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                    data: {
                        'phone_number': this.phoneNumber, 
                        'firstName': this.firstName, 
                        'lastName': this.lastName,
                        'email': this.$store.state.email,
                        'address': this.address
                    }
                })
                .then((response) => {
                    if (response.data.response == 'ok') {
                        this.$store.commit('updateUser', {'first_name': this.firstName, 'last_name': this.lastName, 'address': this.address})
                        this.$emit('update:show', false);
                    }
                })
                .catch((error) => {
                    if (error.response) {
                        for (let index in error.response.data) {
                            this.messages.push({ 'field': index, 'error': error.response.data[index] });
                        }
                        this.message = error.response;
                    }
                });
                this.$emit('update:show', false);
            }
        },
        mounted() {
            this.firstName = this.$store.state.user.first_name
            this.lastName = this.$store.state.user.last_name
            this.phoneNumber = this.$store.state.user.phone_number
            this.address = this.$store.state.user.address
        }
    }
</script>

<style scoped>

</style>