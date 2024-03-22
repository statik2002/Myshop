<template>
    <div v-if="messages.length > 0">
        <div class="alert alert-danger" role="alert" v-for="message in messages">
            {{ message }}
        </div>
    </div>
    <div class="d-flex flex-column gap-2">
        <div class="d-flex flex-row gap-2">
            <label for="productName" class="form-label">Наименование</label>
            <input type="text" class="form-control" id="productName" v-bind:value="product.name" @input="productNameInput">
        </div>
        <div class="d-flex flex-row gap-2">
            <label for="productPrice" class="form-label">Цена</label>
            <input type="text" class="form-control" id="productPrice" :value=product.price @input="productPriceInput">
        </div>
        <div class="d-flex flex-row gap-2">
            <label for="productDescription" class="form-label">Описание</label>
            <textarea class="form-control" aria-label="With textarea" id="productDescription" @input="productDescriptionInput">{{ product.description }}</textarea>
        </div>
        <div class="d-flex flex-row gap-2">
            <label for="productDiscount" class="form-label">Скидка в %</label>
            <input type="text" class="form-control" id="productDiscount" :value=product.discount @input="productDiscountInput">
        </div>
        <div class="d-flex flex-row gap-2">
            <label for="productQuantity" class="form-label">Остаток</label>
            <input type="text" class="form-control" id="productQuantity" :value=product.quantity @input="productQuantityInput">
        </div>
        <div class="d-flex flex-row justify-content-between pt-5">
            <button class="btn btn-success" @click="updateProduct">Сохранить</button>
            <button class="btn btn-success">Галя! У нас отмена</button>
        </div>
    </div>
    
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'product-edit-component',
        props: {
            product: {
                type: Object,
                required: true
            },
            show: Boolean
        },
        data() {
            return {
                messages: [],
                productName: this.product.name,
            }
        },
        methods: {
            hideDialog() {
                this.$emit('update:show', false)
            },

            productNameInput(event) {
                this.product.name = event.target.value
            },

            productDescriptionInput(event) {
                this.product.description = event.target.value
            },

            productDiscountInput(event) {
                this.product.discount = event.target.value
            },

            productPriceInput(event) {
                this.product.price = event.target.value
            },

            productQuantityInput(event) {
                this.product.quantity = event.target.value
            },

            updateProduct() {
                try {
                    axios(
                      {
                        url: `http://127.0.0.1:8000/api/v1/products/${this.product.id}/`,
                        method: 'put',
                        headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                        data: this.product
                      }
                    ).then((response) => {
                          this.$emit('update:show', false)
                        }
                          
                      )
                } catch(e) {
                    messages.push(`Error: ${e}`)
                }
                finally {
        
                }
            }
        },
        mounted() {
            //console.log(this.product)
        }
    }
</script>

<style scoped>
</style>