<template>
    <div>
        <login-dialog v-model:show="loginModalVisible">
            <h1>{{ message }}</h1>
        </login-dialog>
    </div>
</template>

<script>
    export default {
        props: {
            message: {
                type: String,
                required: true
            },
            messageType: {
                type: messageTypes
            }
        },
        data() {
            return {
                messageTypes: {INFO: 'info', WARNING: 'warning'},
                loginModalVisible: false,
            }
        }
    }
</script>

<style scoped>

</style>