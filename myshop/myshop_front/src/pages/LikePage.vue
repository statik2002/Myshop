<template>
    <HeaderComponent></HeaderComponent>
    <div class="container py-3">
        <div v-if="$store.state.userIsAuth">
            <div v-if="isLikedProductsLoad">
                <ProductsList 
                :products="likedProducts"
                v-if="likedProducts.length > 0"
                />
                <div v-else>
                    У вас пока нет любимых товаров
                </div>
            </div>
            <div v-else class="d-flex justify-content-center align-items-center" style="min-height: 80vh;">
                <div class="spinner-grow" style="width: 5rem; height: 5rem;" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
        </div>
        <div v-else>Небходимо зарегистрироваться или войти в аккаунт!</div>
    </div>
    <FooterComponent></FooterComponent>
</template>

<script>
    import axios from 'axios'
    import HeaderComponent from '@/components/HeaderComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
    import ProductsList from '@/components/ProductsList.vue'
    export default {
        components: {HeaderComponent, FooterComponent, ProductsList},
        data() {
            return {
                likedProducts: [],
                isLikedProductsLoad: false
            }
        },
        methods: {
            getLikedProducts() {
                try {
                      axios(
                        {
                          url: `${this.$store.state.apiUrl}/api/v1/like/get_sliced_liked_products/`,
                          method: 'post',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          data: this.$store.state.user.likes
                        }
                      ).then((response) => {
                            this.likedProducts=response.data
                            this.isLikedProductsLoad = true
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            }
        },

        mounted() {
            if (this.$store.state.userIsAuth)
            {
                this.getLikedProducts()
            }
            
        }
    }
</script>

<style scoped>

</style>