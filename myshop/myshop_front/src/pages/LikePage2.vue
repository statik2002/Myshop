<template>
    <header-component></header-component>
    <div class="wrapper">
        
        <!--== Start Preloader Content ==-->
        <div class="preloader-wrap" v-if="!isLikesLoading">
            <div class="preloader">
                <span class="dot"></span>
                <div class="dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
                <span class="text">Загрузка...</span>
            </div>
            
        </div>
        <!--== End Preloader Content ==-->

        <main class="main-content">
            <!--== Start Page Header Area Wrapper ==-->
            <div class="page-header-area">
                <div class="container">
                    <div class="row">
                        <div class="col-12 text-center">
                            <div class="page-header-content">
                                <nav class="breadcrumb-area">
                                    <ul class="breadcrumb">
                                    <li><router-link to="/">Главная</router-link></li>
                                    <li class="breadcrumb-sep">/</li>
                                    <li>Избранное</li>
                                    </ul>
                                </nav>
                                <h4 class="title">Избранное</h4>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!--== End Page Header Area Wrapper ==-->

            <!--== Start Wishlist Area Wrapper ==-->
            <section class="product-area product-wishlist-area">
                <div class="container">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="shopping-wishlist-table table-responsive">
                                <table class="table text-center table-striped">
                                    <thead>
                                        <tr >
                                            <th class="product-remove p-2">Удалить</th>
                                            <th class="product-thumb p-2">Изображение</th>
                                            <th class="product-name p-2">Товар</th>
                                            <th class="product-name p-2">Статус</th>
                                            <th class="product-price p-2">Цена</th>
                                            <th class="product-name p-2">Действие</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr class="cart-wishlist-item" v-for="product in likedProducts">
                                            <td class="product-remove">
                                                <a href="#" @click="dislike(product)"><i class="bi bi-trash3"></i></a>
                                            </td>
                                            <td class="product-thumb">
                                                <router-link :to="{name: 'product2', params: {id: product.id}}">
                                                    <img v-if="product.product_images.length > 0" :src=product.product_images[0].image :alt=product.product_images[0].alt>
                                                    <img v-else src="@/assets/no_image.png" alt="no image">
                                                </router-link>
                                            </td>
                                            <td class="product-name ps-2">
                                                <h4 class="title">
                                                    <router-link :to="{name: 'product2', params: {id: product.id}}">{{ product.name }}</router-link>
                                                </h4>
                                            </td>
                                            <td class="product-stock-status ps-2">
                                                <span v-if="product.quantity > 0" class="stock">В наличии</span>
                                                <span v-else class="outstock">Нет в наличии</span>
                                            </td>
                                            <td class="product-price">
                                                <span class="price">{{ product.price }} &#8381;</span>
                                            </td>
                                            <td class="product-action">
                                                <a v-if="product.quantity > 0" class="btn-cart" href="#" @click="addToCart(product)">В корзину</a>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!--== End Wishlist Area Wrapper ==-->
        </main>
        
    </div>
    <footer-component></footer-component>
</template>

<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                isLikesLoading: false,
                likedProducts: [],
            }
        },
        methods: {
            getLikedProducts() {
                try {
                      axios(
                        {
                          url: `${this.$store.state.apiUrl}/api/v1/like/get_sliced_liked_products/`,
                          method: 'post',
                          data: this.$store.getters.getLikedProducts
                        }
                      ).then((response) => {
                            this.likedProducts=response.data
                            this.isLikesLoading = true
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },
            addToCart(product) {
                this.$store.commit('addProductToCart', {'product': product, 'quantity': 1});
            },
            dislike(product) {
                // Implement send to backend like product
                if (!this.$store.getters.isUserLogin){
                    this.$store.commit('dislike', product.id)
                    this.$router.go()
                    return
                }
                const like = {
                    'user_id': this.$store.state.user.id,
                    'product_id': product.id,
                    'operation': 'dislike'
                }
                try {
                    axios(
                        {
                        url: `${this.$store.state.apiUrl}/api/v1/like/`,
                        method: 'post',
                        headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                        data: like
                        }
                    ).then((response) => {
                            //console.log(response)
                            this.$store.commit('dislike', product.id)
                            this.$router.go()
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },
        },
        mounted() {
            this.getLikedProducts()
        }
    }
</script>

<style scoped>

</style>