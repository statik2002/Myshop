<template>
    <form @submit.prevent>
        <div v-if="messages.length > 0">
            <div class="alert alert-danger" role="alert" v-for="message in messages">
                {{ message }}
            </div>
        </div>
        <textarea class="form-control" id="question" rows=3 placeholder="Задайте вопрос" @input="inputText"></textarea>
        <div class="d-flex gap-2">
            <button type="submit" class="btn btn-success mt-2" @click="sendQuestion">Задать вопрос</button>
            <button type="submit" class="btn btn-light mt-2" @click="$emit('update:show', false)">Отменить</button>
        </div>
    </form>
    <modal-component :show="sendQuestionModal">
        <div class="d-flex flex-column gap-3">
            <div>Ваш вопрос отправлен</div>
            <button class="btn btn-success" @click="sendQuestionModal=false">OK</button>
        </div>
    </modal-component>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'product-question-form',
        props: {
            user_id: {type: Number, required: true},
            product_id: {type: Number, required: true},
        },
        data() {
            return {
                text: '',
                messages: [],
                sendQuestionModal: false
            }
        },
        methods: {
            inputText(event){
                this.text = event.target.value
            },
            sendQuestion() {
                try {
                    axios(
                      {
                        url: `http://127.0.0.1:8000/api/v1/questions/`,
                        method: 'post',
                        headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                        data: {'product': this.product_id, 'customer': this.user_id, 'question_text': this.text}
                      }
                    ).then((response) => {
                            this.sendQuestionModal = true
                            this.text = ''
                            this.$emit('update:show', false)
                        }     
                    ).catch((error) => {
                        if (error.response) {
                            for (let index in error.response.data) {
                                this.messages.push({ 'field': index, 'error': error.response.data[index] });
                            }
                            this.message = error.response;
                        }
                    })
                } catch(e) {
                    console.log(`Error: ${e}`)
                }
                finally {
        
                }
            }
        }
    }
</script>

<style scoped>

</style>