<template>
    <div class="editmodal">
        <div v-if="messages.length > 0">
            <div class="alert alert-danger" role="alert" v-for="message in messages">
                {{ message }}
            </div>
        </div>
        <div class="d-flex flex-column gap-2">
            <div class="d-flex flex-row gap-2">
                <label for="productName" class="form-label">Наименование</label>
                <input type="text" class="form-control" id="productName" v-model="product.name">
            </div>
            <div class="d-flex flex-row gap-2">
                <label for="productPrice" class="form-label">Цена</label>
                <input type="text" class="form-control" id="productPrice" v-model="product.price">
            </div>
            <div class="d-flex flex-row gap-2">
                <label for="productDescription" class="form-label">Описание</label>
                <textarea class="form-control" aria-label="With textarea" id="productDescription" v-model="product.description"></textarea>
            </div>
            <div class="d-flex flex-row gap-2">
                <label for="productDiscount" class="form-label">Скидка в %</label>
                <input type="text" class="form-control" id="productDiscount" v-model="product.discount">
            </div>
            <div class="d-flex flex-row gap-2">
                <label for="productQuantity" class="form-label">Остаток</label>
                <input type="text" class="form-control" id="productQuantity" v-model="product.quantity">
            </div>
            <div class="d-flex flex-row gap-2" v-for="(property, index) in productProperty">
                <label :for=index class="form-label">{{property.name}}</label>
                <input :type=property.type class="form-control" :id=index @input="propertyInput" :value=property.value>
            </div>
            <div class="d-flex flex-row justify-content-between pt-5">
                <button class="btn btn-success" @click="$emit('update:show', false)">Галя! У нас отмена</button>
                <button class="btn btn-success" @click="updateProduct">Сохранить</button>
            </div>
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
                productProperty: {}
            }
        },
        methods: {
            hideDialog() {
                this.$emit('update:show', false)
            },

            propertyInput(event) {
                this.productProperty[event.target.id].value = event.target.value
            },

            updateProduct() {
                try {
                    let props = {}
                    for(const property in this.productProperty){
                        props[property] = this.productProperty[property].value
                    }
                    this.product.properties[0] = props
                    //console.log(this.product)
                    axios(
                      {
                        url: `http://127.0.0.1:8000/api/v1/products/${this.product.id}/`,
                        method: 'put',
                        headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                        data: this.product
                      }
                    ).then((response) => {
                          this.$emit('update:show', false)
                          //this.$router.go()
                        }
                          
                      )
                } catch(e) {
                    this.messages.push(`Error: ${e}`)
                }
                finally {
        
                }
            },
        },
        mounted() {
            //console.log(this.product)
            this.productProperty.product = {name: 'Товар', type: 'number', value: this.product.id}
            
            if (this.product.properties.length > 0)
            {
                this.productProperty.id = {name: 'Id', type: 'number', value: this.product.properties[0].id}
                this.productProperty.color = {name: 'Цвет', type: 'text', value: this.product.properties[0].color ?? ''}
                this.productProperty.weight = {name: 'Вес', type: 'number', value: Number(this.product.properties[0].weight ?? 0.0)}
                this.productProperty.width = {name: 'Ширина', type: 'number', value: Number(this.product.properties[0].width ?? 0.0)}
                this.productProperty.height = {name: 'Высота', type: 'number', value: Number(this.product.properties[0].height ?? 0.0)}
                this.productProperty.length = {name: 'Длинна', type: 'number', value: Number(this.product.properties[0].length ?? 0.0)}
                this.productProperty.description = {name: 'Описание', type: 'text', value: this.product.properties[0].description ?? ""}
                this.productProperty.material = {name: 'Материал/состав', type: 'text', value: this.product.properties[0].material ?? ""}
                this.productProperty.expiration_date = {name: 'Срок годности', type: 'number', value: Number(this.product.properties[0].expiration_date ?? 0.0)}
                this.productProperty.production_origin = {name: 'Производство', type: 'text', value: this.product.properties[0].production_origin ?? ""}
            } else {
                this.productProperty.id = {name: 'Id', type: 'number', value: 0}
                this.productProperty.color = {name: 'Цвет', type: 'text', value: ''}
                this.productProperty.weight = {name: 'Вес', type: 'number', value: 0.0}
                this.productProperty.width = {name: 'Ширина', type: 'number', value: 0.0}
                this.productProperty.height = {name: 'Высота', type: 'number', value: 0.0}
                this.productProperty.length = {name: 'Длинна', type: 'number', value: 0.0}
                this.productProperty.description = {name: 'Описание', type: 'text', value: ""}
                this.productProperty.material = {name: 'Материал/состав', type: 'text', value: ""}
                this.productProperty.expiration_date = {name: 'Срок годности', type: 'number', value: 0}
                this.productProperty.production_origin = {name: 'Производство', type: 'text', value: ""}
            }
            
        }
    }
</script>

<style scoped>
    .editmodal {
        height: 450px;
        width: 750px;
        overflow-y: auto;
    }
</style>