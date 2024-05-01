<template>
    <div>
        <h1>User Activation</h1>
        <div>
            <p>Activation status</p>
            <div v-if="isActivated">Ваша учетная запись активирована!</div>
            <div v-else>
                <div>По каким то причинам ваша запись не активировалась!</div>
                <div>{{ error }}</div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

    export default {
        data() {
            return {
                isActivated: false,
                error: ''
            }
        },

        mounted() {
            const query = this.$route.query
            console.log(query)
            try {
                axios(
                {
                    url: `${this.$store.state.apiUrl}/api/v1/customers/user_activation/?q=${query.token}/`,
                    method: 'get'
                }
                ).then((response) => {
                    if(response.status == 200)
                    {
                        this.isActivated = true
                    } else {
                        this.error = response.data
                    }
                    
                })
                .catch((error) => {
                    this.error = error
                })
            } catch(e) {
                alert(`Connection error: ${e}`);
            }
            finally {
        
            }
        }
    }
</script>

<style scoped>

</style>