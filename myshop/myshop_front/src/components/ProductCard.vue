<template>
    <div class="card border-0 p-1 card-content">
        <div class="overlay">
            <a href="#" class="product-like-container">
                <div v-if="$store.state.userIsAuth">
                    <div v-if="$store.state.user.likes.includes(product.id)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-heart" viewBox="-1 -1 18 18">
                            <path class="bold-icon-active" fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314"/>
                        </svg>
                    </div>
                    <div v-else>
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-heart" viewBox="-1 -1 18 18">
                            <path class="bold-icon" fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314"/>
                        </svg>
                    </div>
                </div>
            </a>
        </div>
        <div class="row vw-25">
            <div class="col-12">
                <a href="#" @click="$router.push({name: 'product', params: {id: product.id}})" class="stretched-link">
                    <img v-if="product.product_images.length > 0" :src=product.product_images[0].image class="card-img-top product-image" alt="...">
                    <img v-else src="@/assets/no_image.png" class="card-img-top product-image" alt="no image">
                </a>
            </div>
        </div>
        <div class="row p-0 m-0">
            <div class="col-12 p-0">
                <div class="d-flex justyfy-content-start" v-if="product.discount > 0">
                    <b class="pe-1 product-price-list">{{ product.discount }} &#8381;</b>
                    <s class="text-secondary"><small>{{ product.price }} &#8381;</small></s>
                </div>
                <div class="d-flex justyfy-content-start" v-else>
                    <b class="pe-1 product-price-list">{{ product.price }} &#8381;</b>
                    <!--<s class="text-secondary"><small>{{ product.price }} &#8381;</small></s>-->
                </div>                    
                <div class="text-truncate product-name ps-0">{{ product.name }}</div>
            </div>
        </div>
        <div class="row p-1 mt-0">
            <div class="col-12">
            <div class="text-truncate product-name">{{ product.description }}</div>
            </div>
        </div>
        <div class="row p-1">
            <div class="col-12">
            <div class="text-truncate product-description"><small>{{ product.description }}</small></div>
            </div>
        </div>
        <div class="row p-1">
            <div v-if="product.his_rating.length > 0" class="d-flex flex-row">
                <div class="stars">
                    <i class="bi bi-star-fill"></i>
                    {{ product.his_rating[0].value }}
                </div>
                    <div class="stars">
                    &#x2022; {{ product.his_rating[0].count }} оценок
                </div>
            </div>
            <div v-else class="d-flex flex-row gap-1">
                <div class="star-no">
                    <i class="bi bi-star-fill"></i>
                    0.0
                </div>
                    <div class="star-no">
                    &#x2022; 0 оценок
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
       name: 'product-card',
       props: {
        product: {
            type: Object,
            required: true
        }
       }
    }
</script>

<style scoped>

</style>