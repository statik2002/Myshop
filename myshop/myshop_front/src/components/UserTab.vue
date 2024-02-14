<template>
    <div class="d-flex">
        <div v-if="Object.entries($store.state.user).length === 0">
            <a href="#" data-bs-title="Cabinet" @click="showLoginDialog"><i class="bi bi-person-circle" style="font-size: 1.5rem;"></i></a>
        </div>
        <div v-else>Авторизованы</div>
        <login-dialog v-model:show="loginModalVisible">
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
                        <button type="button" class="btn btn-success " @click="saveUserData">Save</button>
                    </div>
                    
                </div>
            </form>
        </login-dialog>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                userIsAuthenticated: false,
                loginModalVisible: false,
                phone: '',
                password: ''
            }
        },
        methods: {
            showLoginDialog() {
                this.loginModalVisible = true
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