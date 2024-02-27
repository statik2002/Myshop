<template>
    <div class="row p-2 cart-product widget" :id="id">
        <div class="col pe-5">
            <div class="row">
                <div class="col-auto" v-if="product_images.length > 0">
                    <img class="" :src="product_images[0].image" :alt="product_images[0].alt" style="max-height: 100px; width: auto;">
                </div>
                <div class="col-auto" v-else>
                    <img class="" src="@/assets/no_image.png" alt="no image" style="max-height: 100px; width: auto;">
                </div>
                <div class="col">
                    <div class="col product-description">{{name}}</div>
                </div>
            </div>
        </div>
        <div class="col-auto">
            <div class="row h-100">
                <div class="col-auto">
                    <div class="d-flex gap-3 h-100">
                        <div>
                            {{price}}
                        </div>
                        <div class="d-flex align-items-start pe-5">
                        <div class="d-flex gap-2 align-items-center">
                            <a href="#" class="minus-button" @click="sub"><i class="bi bi-dash-square fs-3 text-dark"></i></a>
                            <div class="px-1 input-wrapper"><input size="2" type="text" :name="id" class="quantity" disabled :value="quantity" maxlength="2" min="1"></div>
                            <a href="#" class="plus-button" @click="add"><i class="bi bi-plus-square fs-3 text-dark"></i></a>
                        </div>
                        </div>
                        <div class="d-flex flex-column justify-content-start">
                        <div class="pt-2 pb-3 fw-bold input-total-wrapper">
                            <span class="total">{{ total }}</span>
                        </div>
                        <div class="">
                            <div class="d-flex gap-3 ms-auto cart-product-icons align-items-start">
                            <button v-if="$store.state.isUserAuth" type="button" class="btn btn-success btn-light" @click="checkOut"><i class="bi bi-cart-check"></i></button>
                            <button type="button" class="btn btn-success btn-light" @click="$store.commit('deleteProductFromCart', id)"><i class="bi bi-trash3"></i></button>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <modal-component v-model:show="dialogMessageShow">
            <div>Ваш заказ отправлен</div>
            <div><button type="button" class="btn btn-success " @click="deleteItemFromCart">Ok</button></div>
        </modal-component>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                dialogMessageShow: false
            }
        },
        props: {
            id: Number,
            name: String,
            product_images: Array,
            description: String,
            available: Boolean,
            slug: String,
            rating: String,
            show_count: Number,
            create_date: String,
            price: String,
            discount: String,
            code_1c: Number,
            quantity: Number,
            catalog: Number,
            tags: Array
        },
        computed: {
            total() {
                return (this.price * this.quantity).toFixed(2);
            }
        },
        methods: {
            add() {
                this.$store.commit('addOne', this.id)
            },
            sub() {
                this.$store.commit('subOne', this.id)
            },
            checkOut() {
               const order_product = [{
                'product': this.id,
                'quantity': this.quantity,
                'fixed_price': this.price
               }]

               const order = {
                'user': this.$store.state.user.id,
                'products_in_order': order_product
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
                            //console.log(response)
                            this.dialogMessageShow = true
                            //this.$store.commit('deleteProductFromCart', this.id)
                            
                        })
               } catch (e) {
                    console.log(`Connection error: ${e}`);
               } finally {

               }
            },
            deleteItemFromCart() {
                this.$store.commit('deleteProductFromCart', this.id)
                this.dialogMessageShow = false
            }
        },
    }
</script>

<style scoped>

</style>