<template>
    <div v-for="linked_product in products" :key="linked_product" class="col-xxl-2 col-xl-2 col-lg-2 col-md-3 col-sm-6 p-1">
    <!--== Start Shop Item ==-->
        <div class="product-item">
            <div class="inner-content" >
                <div class="product-thumb">
                    <a href="#" @click="$router.push({name: 'product2', params: {id: linked_product.id}})">
                        <img v-if="linked_product.product_images.length > 0" :src=$store.state.mediaUrl+linked_product.product_images[0].image alt="...">
                        <img v-else src="@/assets/no_image.png" class="card-img-top product-image" alt="no image">
                    </a>
                    <span v-if="linked_product.discount > 0" class="percent-count sticker">- {{ Math.floor(linked_product.discount) }}%</span>
                </div>
                <div class="product-desc">
                    <div class="product-info">
                        <h6 class="title">
                            <a href="#" @click="$router.push({name: 'product2', params: {id: linked_product.id}})">{{ linked_product.name }}</a>
                        </h6>
                        <div class="star-content">
                            <rating-component :rating="linked_product.rating" :num_rating="linked_product.num_rating"></rating-component>
                        </div>
                        <div class="prices">
                            <div v-if="linked_product.discount > 0">
                                <span class="price">{{ linked_product.online_price - linked_product.online_price * linked_product.discount/100 }} &#8381;</span>
                                <span v-if="linked_product.discount > 0" class="price-old">{{ linked_product.online_price % 1 > 0 ? linked_product.online_price : linked_product.online_price | 0 }} &#8381;</span>
                            </div>
                            <div v-else>
                                <span class="price">{{ linked_product.online_price % 1 > 0 ? linked_product.online_price : linked_product.online_price | 0 }} &#8381;</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!--== End Shop Item ==-->
    </div>
</template>

<script>
    export default {
        name: 'linked-products',
        props: {
            products: {
                type: Array,
                required: true
            }
        }
    }
</script>

<style scoped>

</style>