<template>
    <div>
        <header-component/>
        <!--Desktop-->
        <div v-if="$store.state.windowWidth=='xl'" class="container-xl pt-3" id="productContainer">
            <ProductsList 
                :products="products"
                v-if="isProductsLoading"
            >
            </ProductsList>
            <div v-else class="d-flex justify-content-center align-items-center" style="min-height: 80vh;">
                <div class="spinner-grow" style="width: 5rem; height: 5rem;" role="status">
                <span class="visually-hidden">Loading...</span>
                </div>
            </div>
            <div ref="observer" class="observer"></div>
        </div>
        <!--Telephone-->
        <div v-else class="container-fluid" id="productContainer">
            <ProductsList 
                :products="products"
                v-if="isProductsLoading"
            >
            </ProductsList>
            <div v-else class="d-flex justify-content-center align-items-center" style="min-height: 80vh;">
                <div class="spinner-grow" style="width: 5rem; height: 5rem;" role="status">
                <span class="visually-hidden">Loading...</span>
                </div>
            </div>
            <div ref="observer" class="observer"></div>
        </div>
        <scroll-to-top :productsContainer="productsContainer"></scroll-to-top>
        <footer-component/>
    </div>
</template>

<script>
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
                productsContainer: {},
            }
        },
        methods: {
            async uploadProducts() {
                try {
                    this.productsPage += 1;
                    this.productsOffest += this.productsLimit;
                    let response = await fetch(
                        `${this.$store.state.apiUrl}/api/v1/products/?` + new URLSearchParams({limit: this.productsLimit, offset: this.productsOffest, page: this.productsPage}),
                        {method: 'GET'}
                    );
                    if (response.ok) {
                        let products = await response.json();
                        this.products = [...this.products, ...products.results];
                        this.productsTotalPages = Math.ceil(products.count / this.productsLimit);
                        this.isProductsLoading=true;
                        this.productsContainer = {
                            'isLoaded': true, 
                            'container': document.getElementById("productContainer").getBoundingClientRect(),
                            'innerContainer': document.getElementById("productContainer")
                        }
                    } else {
                        alert('Error get products');
                    }
                } catch(e) {
                    alert('Connection error');
                }
                finally {
                    this.isProductsLoading=true;
                }
            },
        },
        mounted() {
            this.uploadProducts();
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