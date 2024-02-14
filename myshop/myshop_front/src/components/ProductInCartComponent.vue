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
                            <a href="#"><i class="bi bi-heart"></i></a>
                                <button type="button" class="btn btn-success" @click="$store.commit('deleteProductFromCart', id)"><i class="bi bi-trash3"></i></button>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
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
            }
        }
    }
</script>

<style scoped>

</style>