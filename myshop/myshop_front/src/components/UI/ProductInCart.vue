<template>

        <td class="indecor-product-remove">
            <a href="#/"><i class="bi bi-trash3" @click="$store.commit('deleteProductFromCart', cart_product.id)"></i></a>
        </td>
        <td class="indecor-product-thumbnail">
            <a href="#/" v-if="cart_product.product.product_images.length > 0"><img :src=cart_product.product.product_images[0].image :alt=cart_product.product.product_images[0].alt></a>
            <a href="#/" v-else><img src="@/assets/no_image.png" alt="no image"></a>
        </td>
        <td class="indecor-product-name">
            <h4 class="title"><a href="#" @click="$router.push({ name: 'product2', params: { id: cart_product.id } })">{{ cart_product.product.name }}</a></h4>
        </td>
        <td class="indecor-product-price"><span class="price">{{ cart_product.fixed_price }} &#8381;</span></td>
        <td class="indecor-product-quantity">
            <div class="pro-qty">
                <div class="inc qty-btn" @click="add">+</div>
                <input type="text" title="Quantity" :value="cart_product.quantity | 0">
                <div class= "dec qty-btn" @click="sub">-</div>
            </div>
        </td>
        <td class="product-subtotal"><span class="price">{{ (cart_product.product.price - cart_product.product.price * cart_product.product.discount/100) * cart_product.quantity }}</span></td>

</template>

<script>
    export default {
        name: 'cart-product-2',
        props: {
            cart_product: {
                type: Object,
                required: true
            }
        },
        methods: {
            add() {
                this.$store.commit('addOne', this.cart_product.id)
            },
            sub() {
                this.$store.commit('subOne', this.cart_product.id)
            },
        }
    }
</script>

<style scoped>

</style>