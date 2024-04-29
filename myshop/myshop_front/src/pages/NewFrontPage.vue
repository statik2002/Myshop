<template>
    <header-component></header-component>
    <div class="wrapper">
        <!--== Start Preloader Content ==-->
        <div class="preloader-wrap" v-if="!isProductsLoading">
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
            <!--== Start Hero Area Wrapper ==-->
            <section class="">
                <div id="carouselMainIndicators" class="carousel slide" data-bs-ride="true">
                    <div class="carousel-indicators">
                        <button type="button" data-bs-target="#carouselMainIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                        <button type="button" data-bs-target="#carouselMainIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                        <button type="button" data-bs-target="#carouselMainIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="@/assets/img/slider/Forsite.png" class="d-block w-100" alt="...">
                            <div class="carousel-caption d-none d-md-block slider-text">
                                <h5 class="slider-text-header">First slide label</h5>
                                <p class="slider-text-content">Some representative placeholder content for the first slide.</p>
                                <button class="btn btn-success slider-button">BUY</button>
                            </div>
                        </div>
                        <div class="carousel-item">
                            <img src="@/assets/img/slider/slider-01.jpg" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                            <img src="@/assets/img/slider/slider-01.jpg" class="d-block w-100" alt="...">
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselMainIndicators" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselMainIndicators" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </section>
            <!--== End Hero Area Wrapper ==-->

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
                                                <button class="add-cart" @click="addToCartButton(product)">
                                                    <i class="bi bi-cart-plus"></i>
                                                </button>
                                                <button v-if="!likedProducts.includes(product.id)" class="add-wishlist" @click="like(product)">
                                                    <i class="bi bi-heart"></i>
                                                </button>
                                                <button v-else class="add-wishlist" @click="dislike(product)">
                                                    <i class="bi bi-heart-fill"></i>
                                                </button>
                                                <a class="add-quick-view" href="#offcanvasQuickProductView" data-bs-toggle="modal" role="button" aria-controls="offcanvasQuickProductView" @click="showProductQuickModal(product)">
                                                    <i class="bi bi-search"></i>
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
        </main>

        <footer-component></footer-component>

        <!--== Scroll Top Button==-->
        <scroll-to-top></scroll-to-top>

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
                                <div class="inc qty-btn" @click="add(productAtModal)">+</div>
                                <input type="text" id="quantity4" title="Quantity" v-model="productQuantityModal" @input="inputQuantity(productAtModal, $event)" />
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

        <!--== Start Side Menu ==-->
        <aside class="off-canvas-wrapper">
            <div class="off-canvas-inner">
            <div class="off-canvas-overlay"></div>
            <!-- Start Off Canvas Content Wrapper -->
            <div class="off-canvas-content">
                <!-- Off Canvas Header -->
                <div class="off-canvas-header">
                <div class="close-action">
                    <button class="btn-menu-close">menu <i class="fa fa-chevron-left"></i></button>
                </div>
                </div>

                <div class="off-canvas-item">
                <!-- Start Mobile Menu Wrapper -->
                <div class="res-mobile-menu menu-active-one">
                    <!-- Note Content Auto Generate By Jquery From Main Menu -->
                </div>
                <!-- End Mobile Menu Wrapper -->
                </div>
            </div>
            <!-- End Off Canvas Content Wrapper -->
            </div>
        </aside>
        <!--== End Side Menu ==-->

    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                products: [],
                isProductsLoading: false,
                productsPage: 0,
                productsLimit: 30,
                productsTotalPages: 0,
                productsOffest: -30,
                productQantity: 1,
                productAtModal: null,
                productQuantityModal: 1,
                likedProducts: []
            }
        },
        methods: {
            async uploadProducts() {
                try {
                    this.productsPage += 1;
                    this.productsOffest += this.productsLimit;
                    let response = await fetch(
                        'http://127.0.0.1:8000/api/v1/products/?' + new URLSearchParams({limit: this.productsLimit, offset: this.productsOffest, page: this.productsPage}),
                        {method: 'GET'}
                    );
                    if (response.ok) {
                        let products = await response.json();
                        this.products = [...this.products, ...products.results];
                        this.productsTotalPages = Math.ceil(products.count / this.productsLimit);
                        this.isProductsLoading=true;
                    } else {
                        alert('Error get products');
                    }
                } catch(e) {
                    console.log(`Connection error ${e}`);
                }
                finally {
                    this.isProductsLoading=true;
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
            },
            like(product) {
                // Implement send to backend like product
                const like = {
                    'product_id': product.id,
                    'operation': 'like'
                }
                if (!this.$store.getters.isUserLogin){
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
                if (!this.$store.getters.isUserLogin){
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
            add(product) {
                if(this.productQuantityModal >= Number(product.quantity)){
                    this.productQuantityModal = Number(product.quantity)
                } else {
                    this.productQuantityModal = this.productQuantityModal + 1
                }
            },
            sub() {
                this.productQuantityModal > 1 ? this.productQuantityModal -= 1 : 1
            },
            inputQuantity(product, event){
                if(event.target.value < 1){
                    event.target.value = 1
                    this.productQuantityModal = 1
                } else if(event.target.value >= Number(product.quantity)) {
                    event.target.value = Number(product.quantity)
                    this.productQuantityModal = Number(product.quantity)
                }
            },
        },
        mounted() {
            this.uploadProducts();
            this.likedProducts = this.$store.getters.getLikedProducts
            
            const options = {
                rootMargin: '0px',
                thresold: 1.0
            }
            const callback = (entries, observer) => {
            if (entries[0].isIntersecting && this.productsPage < this.productsTotalPages) {
                this.uploadProducts()
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