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
            <div class="d-flex flex-row gap-2">
                <label for="productOrigin" class="form-label">Производство</label>
                <input type="text" class="form-control" id="productOrigin" :value=product.production_origin @input="productOrigin">
            </div>
            <div v-if="product.properties.length > 0">
                <div class="d-flex flex-column gap-2" v-for="property in product.properties">
                    <div v-for="key of Object.keys(property)">
                        {{ key }} + {{ property[key] }}
                    </div>
                </div>
            </div>
            <div v-if="product.product_images.length > 0" class="d-flex gap-2 pt-2">
                <div v-for="image in product.product_images">
                    <div class="d-flex flex-column gap-2">
                        <img :src=image.image :alt=image.alt height="50px">
                        <button class="btn btn-sm btn-danger" @click="deleteImage(image)">Удалить</button>
                    </div>
                </div>
            </div>
            <div class="d-flex flex-column gap-2">
                <label for="uploadedFile" class="form-label">Добавить изображение</label>
                <input type="file" class="form-control" @change="onFileChanged" id="uploadedFile" autocomplete="photo">
                <button type="button" class="btn btn-success mt-3" @click="onUpload">Загрузить</button>
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
                productName: this.product.name,
                uploadedFile: null
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
            productOrigin(event) {
                this.product.production_origin = event.target.value
            },
            onFileChanged(event) {
                //console.log(event.target.file)
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
                          this.$router.go()
                        }
                          
                      )
                } catch(e) {
                    messages.push(`Error: ${e}`)
                }
                finally {
        
                }
            },

            deleteImage(image) {
                try {
                    axios(
                      {
                        url: `http://127.0.0.1:8000/api/v1/products/delete_image/`,
                        method: 'post',
                        headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                        data: image
                      }
                    ).then((response) => {
                            //console.log(response)
                            this.$router.go()
                          //this.$emit('update:show', false)
                        }
                      )
                } catch(e) {
                    messages.push(`Error: ${e}`)
                }
                finally {
        
                }
            },

            onFileChanged(event) {
                this.uploadedFile = event.target.files[0]
            },

            onUpload() {
                this.messages = []
                try {
                    let formData = new FormData();
                    if (['image/png', 'image/jpg', 'image/jpeg', 'image/webp'].includes(this.uploadedFile['type'])==false)
                    {
                        this.messages.push('Некорректный тип файла!')
                        return
                    }
                    formData.append('file', this.uploadedFile);
                    const fileMetadata = this.readMetadata(this.uploadedFile)
                    if (fileMetadata.size > 300000) {
                        this.messages.push('Слишком большой файл!')
                        return
                    }
                    formData.append('product_id', this.product.id)
                    axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/products/upload_image/`,
                          method: 'post',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`, 'Content-Type': 'multipart/form-data'},
                          data: formData
                        }
                      ).then((response) => {
                            //console.log(response)
                            this.$router.go()
                        })
               } catch (e) {
                    console.log(`Connection error: ${e}`);
               } finally {

               }
                
            },

            readMetadata(file) {
                const name = file.name ? file.name : 'Not supported'
                const type = file.type ? file.type : 'Not supported'
                const size = file.size ? file.size : 'Not supported'

                return {'name': name, 'type': type, 'size': size}
            }
        },
        mounted() {
            //console.log(this.product)
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