<template>
    <div v-if="messages.length > 0">
        <div class="alert alert-danger" role="alert" v-for="message in messages">
            {{ message }}
        </div>
    </div>
    <form @submit.prevent>
        <div class="d-flex flex-column">
            <div class="d-flex flex-column gap-2">
                <label for="uploadedFile" class="form-label">Выберите файл с аватаркой</label>
                <input type="file" class="form-control" @change="onFileChanged" id="uploadedFile">
                <button type="button" class="btn btn-success mt-3" @click="onUpload">Загрузить</button>
            </div>
        </div>
    </form>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'upload-avatar-form',
        props: {
            show: {
                type: Boolean,
                default: false
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
                    axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/customers/update_avatar/`,
                          method: 'post',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`, 'Content-Type': 'multipart/form-data'},
                          data: formData
                        }
                      ).then((response) => {
                            //console.log(response.status)
                            if (response.status == 200){
                                this.message = 'Ваш аватар обновлен!'
                                this.$store.commit('reloadUser')
                                this.$emit('update:show', false)
                            }
                            else {
                                this.message = 'При отправке аватара произошла ошибка!'
                                this.$emit('update:show', false)
                            }
                        })
               } catch (e) {
                    console.log(`Connection error: ${e}`);
               } finally {

               }
                this.$emit('update:show', false)
            },
            onFileChanged(event) {
                this.selectedFile = event.target.files[0]
            }
        }
    }
</script>

<style scoped>

</style>