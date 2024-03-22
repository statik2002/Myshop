<template>
    <header-component/>
        <div class="container-xl pt-3">
            <ProductsList 
                :products="products"
                v-if="isProductsLoading"
            />
            <div v-else class="d-flex justify-content-center align-items-center" style="min-height: 80vh;">
                <div class="spinner-grow" style="width: 5rem; height: 5rem;" role="status">
                <span class="visually-hidden">Loading...</span>
                </div>
            </div>
            <div ref="observer" class="observer"></div>
        </div>
        <scroll-to-top></scroll-to-top>
    <footer-component/>
</template>

<script>
    import axios from 'axios';
    import HeaderComponent from '@/components/HeaderComponent.vue';
    import FooterComponent from '@/components/FooterComponent.vue';
    import ProductsList from '@/components/ProductsList.vue'
    export default {
        components: {HeaderComponent, FooterComponent, ProductsList},
        data() {
            return {
                products: [],
                isProductsLoading: false,
                productsPage: 0,
                productsLimit: 30,
                productsTotalPages: 0,
                productsOffest: -30,
            }
        },
        methods: {
            async uploadProducts() {
                try {
                    this.productsPage += 1;
                    this.productsOffest += this.productsLimit;
                    let response = await fetch(
                        'http://127.0.0.1:8000/api/v1/products/search/?' + new URLSearchParams({limit: this.productsLimit, offset: this.productsOffest, page: this.productsPage}),
                        {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json;charset=utf-8'},
                            body: JSON.stringify({query: this.$route.params.query})
                        }
                    );
                    if (response.ok) {
                        let products = await response.json();
                        this.products = [...this.products, ...products.results];
                        this.productsTotalPages = Math.ceil(products.count / this.productsLimit);
                    } else {
                        alert('Error get products');
                    }
                } catch(e) {
                    alert('Connection error');
                }
                finally {
                    this.isProductsLoading=true;
                }
            }
        },
        mounted() {
            this.uploadProducts()
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

</style>