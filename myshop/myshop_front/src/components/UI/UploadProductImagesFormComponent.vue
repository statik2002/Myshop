<template>
    <div v-if="messages.length > 0">
        <div class="alert alert-danger" role="alert" v-for="message in messages">
            {{ message }}
        </div>
    </div>
    <form @submit.prevent>
        <div class="d-flex flex-column">
            <div v-if="product.product_images.length > 0" class="d-flex gap-2 pt-2">
                <div v-for="image in product.product_images">
                    <div class="d-flex flex-column gap-2">
                        <img :src=image.image :alt=image.alt height="50px">
                        <button class="btn btn-sm btn-danger" @click="deleteImage(image)">Удалить</button>
                    </div>
                </div>
            </div>
            <div class="d-flex flex-column gap-2">
                <label for="uploadedFile" class="form-label">Выберите файл с Изображением</label>
                <input type="file" class="form-control" @change="onFileChanged" id="uploadedFile" autocomplete="photo">
                <button type="button" class="btn btn-success mt-3" @click="onUpload">Загрузить</button>
            </div>
        </div>
    </form>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'upload-image',
        props: {
            show: {
                type: Boolean,
                default: false
            },
            product: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                messages: [],
                selectedFile: null
            }
        },
        methods: {
            onUpload() {
                this.messages = []
                try {
                    let formData = new FormData();
                    if (['image/png', 'image/jpg', 'image/jpeg', 'image/webp'].includes(this.selectedFile['type'])==false)
                    {
                        this.messages.push('Некорректный тип файла!')
                        return
                    }
                    formData.append('file', this.selectedFile);
                    const fileMetadata = this.readMetadata(this.selectedFile)
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
                            console.log(response)
                            this.$emit('update:show', false)
                            this.$router.go()
                        })
               } catch (e) {
                    console.log(`Connection error: ${e}`);
               } finally {
                    this.$emit('update:show', false)
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
                this.selectedFile = event.target.files[0]
            },

            readMetadata(file) {
                const name = file.name ? file.name : 'Not supported'
                const type = file.type ? file.type : 'Not supported'
                const size = file.size ? file.size : 'Not supported'

                return {'name': name, 'type': type, 'size': size}
            }
        }
    }
</script>

<style scoped>

</style>