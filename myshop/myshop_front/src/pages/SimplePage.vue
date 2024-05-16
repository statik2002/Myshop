<template>
    <div class="wrapper">
        <header-component></header-component>
        <!--== Start Preloader Content ==-->
        <div class="preloader-wrap" v-if="!isPageLoading">
            <div class="preloader">
                <span class="dot"></span>
                <div class="dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
                
            </div>
        </div>

        <main class="main-content">
            <div class="container">
                <div v-html="page.text"></div>
            </div>
        </main>
        <footer-component></footer-component>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                isPageLoading: false,
                page: {}
            }
        },
        methods: {
            uploadPage() {
                try {
                      axios(
                        {
                          url: `${this.$store.state.apiUrl}/api/v1/simple_pages/get_page_by_id/`,
                          method: 'POST',
                          data: {"pk": this.$route.params.pk}
                        }
                      ).then((response) => {
                        this.page = response.data;
                        this.isPageLoading=true
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            }
        },
        mounted() {
            this.uploadPage()
        }
    }
</script>

<style scoped>

</style>