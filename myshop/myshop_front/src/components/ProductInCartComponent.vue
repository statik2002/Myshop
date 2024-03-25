<template>
    <div class="row p-2 cart-product widget" :id="cart_product.id">
        <div class="col pe-5">
            <div class="row">
                <div class="col-auto" v-if="cart_product.product.product_images.length > 0">
                    <img class="" :src="cart_product.product.product_images[0].image" :alt="cart_product.product.product_images[0].alt" style="max-height: 100px; width: auto;">
                </div>
                <div class="col-auto" v-else>
                    <img class="" src="@/assets/no_image.png" alt="no image" style="max-height: 100px; width: auto;">
                </div>
                <div class="col">
                    <div class="col product-description">{{cart_product.product.name}}</div>
                </div>
            </div>
        </div>
        <div class="col-auto">
            <div class="row h-100">
                <div class="col-auto">
                    <div class="d-flex gap-3 h-100">
                        <div>
                            {{cart_product.fixed_price}}
                        </div>
                        <div class="d-flex align-items-start pe-5">
                        <div class="d-flex gap-2 align-items-center">
                            <a href="#" class="minus-button" @click="sub"><i class="bi bi-dash-square fs-3 text-dark"></i></a>
                            <div class="px-1 input-wrapper"><input size="2" type="text" :name="cart_product.id" class="quantity" disabled :value="cart_product.quantity" maxlength="2" min="1"></div>
                            <a href="#" class="plus-button" @click="add"><i class="bi bi-plus-square fs-3 text-dark"></i></a>
                        </div>
                        </div>
                        <div class="d-flex flex-column justify-content-start">
                        <div class="pt-2 pb-3 fw-bold input-total-wrapper">
                            <span class="total">{{ total }}</span>
                        </div>
                        <div class="">
                            <div class="d-flex gap-3 ms-auto cart-product-icons align-items-start">
                            <button v-if="$store.state.userIsAuth" type="button" class="btn btn-success btn-light" @click="checkOut"><i class="bi bi-cart-check"></i></button>
                            <button type="button" class="btn btn-success btn-light" @click="$store.commit('deleteProductFromCart', cart_product.id)"><i class="bi bi-trash3"></i></button>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <modal-component v-model:show="dialogMessageShow">
            <div class="d-flex flex-column gap-3 justify-content-center">
                <div class="d-flex justify-content-center">{{ message }}</div>
                <div class="d-flex justify-content-center"><button type="button" class="btn btn-success " @click="deleteItemFromCart">Ok</button></div>
            </div>
        </modal-component>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                dialogMessageShow: false,
                message: ''
            }
        },
        props: {
            cart_product: {
                type: Object,
                required: true
            }
        },
        computed: {
            total() {
                return (this.cart_product.fixed_price * this.cart_product.quantity).toFixed(2);
            }
        },
        methods: {
            add() {
                this.$store.commit('addOne', this.cart_product.id)
            },
            sub() {
                this.$store.commit('subOne', this.cart_product.id)
            },
            checkOut() {
               const order_product = [{
                'product': this.cart_product.id,
                'quantity': this.cart_product.quantity,
                'fixed_price': this.cart_product.fixed_price
               }]

               const order = {
                'customer': this.$store.state.user.id,
                'order_products': order_product
               }

               try {
                axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/order/`,
                          method: 'post',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          data: order
                        }
                      ).then((response) => {
                            //console.log(response.status)
                            if (response.status == 200){
                                this.message = 'Ваш заказ отправлен!'
                                this.dialogMessageShow = true
                            }
                            else {
                                this.message = 'При отправке заказа произошла ошибка!'
                                this.dialogMessageShow = true
                            }
                        })
               } catch (e) {
                    console.log(`Connection error: ${e}`);
               } finally {

               }
            },
            deleteItemFromCart() {
                this.$store.commit('deleteProductFromCart', this.cart_product.id)
                this.dialogMessageShow = false
            }
        },
    }
</script>

<style scoped>

</style>