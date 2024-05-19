<template>
    <header-component></header-component>
    <div class="wrapper">
        <div class="container">
            <div class="block">
                <div v-if="activationResult == 0">
                    <p class="text">Идет активация аккаунта.</p>
                </div>
                <div v-else-if="activationResult == 1">
                    <p class="text">Активация прошла успешно. Вы можете войти в свой аккаунт.</p>
                </div>
                <div v-else>
                    <p>При активации аккаунта произошла ошибка.</p>
                </div>
            </div>
        </div>
    </div>
    <footer-component></footer-component>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                activationTocken: '',
                activationResult: 0
            }
        },
        methods: {
            async activate(){
                try {
                      axios(
                        {
                          url: `${this.$store.state.apiUrl}/api/v1/customers/user_activation/?q=${this.activationTocken}`,
                          method: 'get',
                        }
                      ).then((response) => {
                            if (response.status == 200){
                                this.activationResult = 1
                            } else {
                                this.activationResult = 2
                            }
                        })
                } catch(e) {
                    console.log(`Connection error: ${e}`);
                }
                finally {
        
                }
            }
        },
        mounted() {
            this.activationTocken = this.$route.query.q
            this.activate()
        }
    }
</script>

<style scoped>
.block {
    width: 400px;
    height: 300px;
    position: relative;
    margin-top: 50px;
    margin-bottom: 50px;
    padding: 20px;
    top: 50%;
    left: 30%;
    border: 1px;
    border-style: solid;
    border-color: black;
}
.block .text {
    position: absolute;
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%);
}
</style>