<template>
    <div class="row pb-4 cart-product" id="{{id}}">
        <div class="col pe-5">
        <div class="row">
            <div class="col-auto" v-for="image in product_images">
                <img class="" :src="image" alt="" style="max-height: 100px; width: auto;">
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
                    <a href="#" class="minus-button" id="product1-minus" @click="sub"><i class="bi bi-dash-square fs-3 text-dark"></i></a>
                    <div class="px-1 input-wrapper"><input size="2" type="text" id="product_{{id}}" class="quantity" disabled :value="quantity" maxlength="2" min="1"></div>
                    <a href="#" class="plus-button" @click="add"><i class="bi bi-plus-square fs-3 text-dark"></i></a>
                </div>
                </div>
                <div class="input-hidden">
                    <input type="text" value="{{price}}" class="price">
                </div>
                <div class="d-flex flex-column justify-content-start">
                <div class="pt-2 pb-3 fw-bold input-total-wrapper">
                    <input type="text" :value="total" class="total" disabled maxlength="2" min="1" size="1">
                </div>
                <div class="">
                    <div class="d-flex gap-3 ms-auto cart-product-icons align-items-start">
                    <a href="#"><i class="bi bi-heart"></i></a>
                    <form action="{% url 'cart:remove_from_cart' cart_product.id %}" method="post">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-success"><i class="bi bi-trash3"></i></button>
                    </form>

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
        props: [
            'id',
            'name',
            'product_images',
            'description',
            'available',
            'slug',
            'rating',
            'show_count',
            'create_date',
            'price',
            'discount',
            'code_1c',
            'quantity',
            'catalog',
            'tags'
        ],
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