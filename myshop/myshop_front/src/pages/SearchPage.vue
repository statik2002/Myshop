<template>
    <header-component></header-component>
    <div class="container-xl pt-3">
        <div v-if="isProductsLoading">
            <ProductsList
            :products="products"
            v-if="products.length > 0"
            />
            <div v-else>Товаров с заросом [{{ $route.params.query }}] не найдено!</div>
        </div>
        <div v-else class="d-flex justify-content-center align-items-center" style="min-height: 80vh;">
            <div class="spinner-grow" style="width: 5rem; height: 5rem;" role="status">
            <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        <div ref="observer" class="observer"></div>
    </div>
    <footer-component></footer-component>
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
                query: this.$route.params.query
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
                        this.isProductsLoading=true;
                    } else {
                        alert('Error get products');
                    }
                } catch(e) {
                    console.log(e)
                }
                finally {
                    this.isProductsLoading=true;
                }
            }
        },
        watch: {
            $route (to, from) {
                this.isProductsLoading=false
                this.products = []
                this.productsPage = 0
                this.productsLimit = 30,
                this.productsTotalPages = 0,
                this.productsOffest = -30,
                this.uploadProducts(to.params.query)
            }
        },
        mounted() {
            this.uploadProducts(this.$route.params.query)
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