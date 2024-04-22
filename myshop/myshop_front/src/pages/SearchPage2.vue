<template>
    <header-component></header-component>
    <div class="wrapper">
        
        <!--== Start Preloader Content ==-->
        <div class="preloader-wrap" v-if="!isSearchLoading">
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

        <!--== Start Page Header Area Wrapper ==-->
        <div class="page-header-area">
            <div class="container">
                <div class="row">
                    <div class="col-12 text-center">
                        <div class="page-header-content">
                            <nav class="breadcrumb-area">
                                <ul class="breadcrumb">
                                    <li><router-link to="/newfront">Главная</router-link></li>
                                    <li class="breadcrumb-sep">/</li>
                                    <li>Поиск</li>
                                </ul>
                            </nav>
                            <h4 class="title">Поиск по запросу: {{ $route.params.query }}</h4>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!--== End Page Header Area Wrapper ==-->

        <!--== Start Product Area Wrapper ==-->
        <section class="container-xl py-5">
            <div class="row p-0">
                <TransitionGroup name="products">
                    <div v-for="product in products" :key="product" class="col-xxl-2 col-xl-2 col-lg-2 col-md-3 col-sm-6 p-1">
                    <!--== Start Shop Item ==-->
                        <div class="product-item">
                            <div class="inner-content" >
                                <div class="product-thumb">
                                    <a href="#" @click="$router.push({name: 'product2', params: {id: product.id}})">
                                        <img v-if="product.product_images.length > 0" :src=product.product_images[0].image alt="...">
                                        <img v-else src="@/assets/no_image.png" class="card-img-top product-image" alt="no image">
                                    </a>
                                    <span v-if="product.discount > 0" class="percent-count sticker">- {{ Math.floor(product.discount) }}%</span>
                                    <div class="product-action">
                                        <div class="addto-wrap">
                                            <a class="add-cart" href="javascript:void(0);" @click="addToCartButton(product)">
                                                <i class="zmdi zmdi-shopping-cart-plus icon"></i>
                                            </a>
                                            <div v-if="!likedProducts.includes(product.id)">
                                                <a class="add-wishlist" href="javascript:void(0);" @click="like(product)">
                                                    <i class="bi bi-heart"></i>
                                                </a>
                                            </div>
                                            <div v-else>
                                                <a class="add-wishlist" href="javascript:void(0);" @click="dislike(product)">
                                                    <i class="bi bi-heart-fill"></i>
                                                </a>
                                            </div>
                                            <a class="add-quick-view" href="#offcanvasQuickProductView" data-bs-toggle="modal" role="button" aria-controls="offcanvasQuickProductView" @click="showProductQuickModal(product)">
                                                <i class="zmdi zmdi-search icon"></i>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="product-desc">
                                    <div class="product-info">
                                        <h6 class="title">
                                            <a href="#" @click="$router.push({name: 'product2', params: {id: product.id}})">{{ product.name }}</a>
                                        </h6>
                                        <div class="star-content">
                                            <rating-component :rating="product.rating" :num_rating="product.num_rating"></rating-component>
                                        </div>
                                        <div class="prices">
                                            <div v-if="product.discount > 0">
                                                <span class="price">{{ product.price - product.price * product.discount/100 }} &#8381;</span>
                                                <span v-if="product.discount > 0" class="price-old">{{ product.price % 1 > 0 ? product.price : product.price | 0 }} &#8381;</span>
                                            </div>
                                            <div v-else>
                                                <span class="price">{{ product.price % 1 > 0 ? product.price : product.price | 0 }} &#8381;</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--== End Shop Item ==-->
                    </div>
                </TransitionGroup>
            </div>
        </section>
        <!--== End Product Area Wrapper ==-->
        <div ref="observer" class="observer"></div>

    </div>

    <modal-component v-model:show="addToCartModalIsVisible">
        <div class="d-flex flex-column gap-3">
            <div>{{ addModalProductName }} уже в корзине</div>
            <div class="d-flex justify-content-between gap-4 account-optional-group">
                <router-link to="/cart2">Посмотреть корзину</router-link>
                <button class="btn btn-link" @click="addToCartModalIsVisible=false">Продолжить покупки</button>
            </div>
        </div>
    </modal-component>

    <!--== Start Quick View Menu ==-->
    <div class="modal " tabindex="-1" id="offcanvasQuickProductView">
        <div class="modal-dialog modal-xl product-quick-view-inner">
            <div class="product-quick-view-content" v-if="productAtModal !== null">
                <button type="button" class="btn-close" id="closeProductModal" data-bs-dismiss="modal" aria-label="Close">
                    <span class="close-icon"><i class="bi bi-x-lg"></i></span>
                </button>
                <div class="row">
                <div class="col-lg-6 col-md-6 col-12">
                    <div class="thumb">
                        <img v-if="productAtModal.product_images.length > 0" :src=productAtModal.product_images[0].image :alt=productAtModal.product_images[0].alt>
                        <img v-else src="@/assets/no_image.png" alt="no image">
                    </div>
                </div>
                <div class="col-lg-6 col-md-6 col-12">
                    <div class="content">
                    <h4 class="title">{{ productAtModal.name }}</h4>
                    <div class="prices">
                        <div v-if="productAtModal.discount > 0">
                            <del class="price-old">{{ productAtModal.price }} &#8381;</del>
                            <span class="price">{{ productAtModal.price - productAtModal.price * productAtModal.discount/100 }} &#8381;</span>
                        </div>
                        <div v-else>
                            <span class="price">{{ productAtModal.price % 1 > 0 ? productAtModal.price : productAtModal.price | 0 }} &#8381;</span>
                        </div>
                    </div>
                    <p>{{ productAtModal.description }}</p>
                    <!--
                    <div class="quick-view-select">
                        <div class="quick-view-select-item">
                        <label for="forSizes" class="form-label">Size:</label>
                        <select class="form-select" id="forSizes" required>
                            <option selected value="">s</option>
                            <option>m</option>
                            <option>l</option>
                            <option>xl</option>
                        </select>
                        </div>
                        <div class="quick-view-select-item">
                        <label for="forColors" class="form-label">Color:</label>
                        <select class="form-select" id="forColors" required>
                            <option selected value="">red</option>
                            <option>green</option>
                            <option>blue</option>
                            <option>yellow</option>
                            <option>white</option>
                        </select>
                        </div>
                    </div>
                    -->
                    <div class="action-top">
                        <div class="pro-qty">
                            <div class="inc qty-btn" @click="add">+</div>
                            <input type="text" id="quantity4" title="Quantity" v-model="productQuantityModal" />
                            <div class= "dec qty-btn" @click="sub">-</div>
                        </div>
                        <button class="btn btn-black" @click="addToCart(productAtModal, productQuantityModal)">В корзину</button>
                    </div>
                    </div>
                </div>
                </div>
            </div>
        </div>
    </div>
    <!--== End Quick View Menu ==-->  

    <footer-component></footer-component>
    <!--== Scroll Top Button==-->
    <scroll-to-top></scroll-to-top>
</template>

<script>
    export default {
        data() {
            return {
                isSearchLoading: false,
                products: [],
                productsPage: 0,
                productsLimit: 30,
                productsTotalPages: 0,
                productsOffest: -30,
                likedProducts: [],
                productAtModal: null,
                productQuantityModal: 1,
                addToCartModalIsVisible: false,
                addModalProductName: ''
            }
        },
        watch: {
            $route (to, from) {
                this.isSearchLoading=false
                this.products = []
                this.productsPage = 0
                this.productsLimit = 30,
                this.productsTotalPages = 0,
                this.productsOffest = -30,
                this.uploadProducts(to.params.query)
            }
        },
        methods: {
            async uploadProducts(query) {
                try {
                    this.productsPage += 1;
                    this.productsOffest += this.productsLimit;
                    let response = await fetch(
                        'http://127.0.0.1:8000/api/v1/products/search/?' + new URLSearchParams({limit: this.productsLimit, offset: this.productsOffest, page: this.productsPage}),
                        {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json;charset=utf-8'},
                            body: JSON.stringify({query: query})
                        }
                    );
                    if (response.ok) {
                        let products = await response.json();
                        this.products = [...this.products, ...products.results];
                        this.productsTotalPages = Math.ceil(products.count / this.productsLimit);
                        this.isSearchLoading=true;
                    } else {
                        alert('Error get products');
                    }
                } catch(e) {
                    console.log(e)
                }
                finally {
                    this.isSearchLoading=true;
                }
            },
            like(product) {
                // Implement send to backend like product
                const like = {
                    'product_id': product.id,
                    'operation': 'like'
                }
                if (!this.$store.userIsAuth){
                    if (!this.$store.state.unregisteredUser.likes.includes(product.id)) {
                                this.$store.commit('like', product.id)
                        }
                    return
                }
                try {
                        axios(
                        {
                            url: `http://127.0.0.1:8000/api/v1/like/`,
                            method: 'post',
                            headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                            data: like
                        }
                        ).then((response) => {
                            //console.log(response)
                            if (!this.$store.state.user.likes.includes(product.id)) {
                                this.$store.commit('like', product.id)
                            }
                            
                        })
                    } catch(e) {
                        alert(`Connection error: ${e}`);
                    }
                    finally {
            
                    }
                },
            dislike(product) {
                // Implement send to backend like product
                const like = {
                    'user_id': this.$store.state.user.id,
                    'product_id': product.id,
                    'operation': 'dislike'
                }
                if (!this.$store.userIsAuth){
                    if (this.$store.state.unregisteredUser.likes.includes(product.id)) {
                                this.$store.commit('dislike', product.id)
                        }
                    return
                }
                try {
                        axios(
                        {
                            url: `http://127.0.0.1:8000/api/v1/like/`,
                            method: 'post',
                            headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                            data: like
                        }
                        ).then((response) => {
                            //console.log(response)
                            this.$store.commit('dislike', product.id)
                        })
                    } catch(e) {
                        alert(`Connection error: ${e}`);
                    }
                    finally {
            
                    }
            },
            showProductQuickModal(product) {
                this.productAtModal = product
                this.productQuantityModal = 1
            },
            addToCart(product, quantity = 1) {
                this.$store.commit('addProductToCart', {'product': product, 'quantity': quantity});
                const modalCloseButton = document.getElementById('closeProductModal')
                modalCloseButton.click()
            },
            addToCartButton(product) {
                this.$store.commit('addProductToCart', {'product': product, 'quantity': 1});
                this.addModalProductName = product.name
                this.addToCartModalIsVisible = true
            },
            add() {
                this.productQuantityModal += 1
            },
            sub() {
                this.productQuantityModal > 1 ? this.productQuantityModal -= 1 : 1
            }
        },
        mounted() {
            this.uploadProducts(this.$route.params.query)
            this.likedProducts = this.$store.getters.getLikedProducts
            const options = {
                rootMargin: '0px',
                thresold: 1.0
            }
            const callback = (entries, observer) => {
            if (entries[0].isIntersecting && this.productsPage < this.productsTotalPages) {
                this.uploadProducts(this.$route.params.query)
            }
            }
            const observer = new IntersectionObserver(callback, options);
            observer.observe(this.$refs.observer);
        }
    }
</script>

<style scoped>
.products-enter-active,
.products-leave-active {
  transition: all 0.5s ease;
}
.products-enter-from,
.products-leave-to {
  opacity: 0;
  transform: translateY(100px);
}
</style>