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
            registerUser() {
                this.$store.dispatch('loginUser', {'phone': this.phone, 'password': this.password})
                    .then(
                        console.log('login OK')
                    )
                    .finally(
                        this.$emit('update:show', false)
                    )
                
            }
        }
    }
</script>

<style scoped>

</style>