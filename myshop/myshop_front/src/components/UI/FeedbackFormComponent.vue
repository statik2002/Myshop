<template>
    <div v-if="messages.length > 0">
        <div class="alert alert-danger" role="alert" v-for="message in messages">
            {{ message }}
        </div>
    </div>
    <p>{{ product_id }}</p>
    <form @submit.prevent>
        <div class="d-flex flex-column">
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="summaryFeedback" class="col-sm-2 form-label">Общий отзыв</label>
                </div>
                <div class="col-sm-9">
                    <textarea 
                        class="form-control" 
                        aria-label="With textarea" 
                        id="summaryFeedback" 
                        @input="summaryFeedbackInput"
                        autocomplete="off"
                        >
                        
                    </textarea>
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="positiveFeedback" class="col-sm-2 form-label">Положительные качества</label>
                </div>
                <div class="col-sm-9">
                    <textarea 
                        class="form-control" 
                        aria-label="With textarea" 
                        id="positiveFeedback" 
                        @input="positiveFeedbackInput"
                        autocomplete="off"
                        >
                        
                    </textarea>
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-sm-3">
                    <label for="negativeFeedback" class="col-sm-2 form-label">Отрицательные качества</label>
                </div>
                <div class="col-sm-9">
                    <textarea 
                        class="form-control" 
                        aria-label="With textarea" 
                        id="negativeFeedback" 
                        @input="negativeFeedbackInput"
                        autocomplete="off"
                        >
                        
                    </textarea>
                </div>
            </div>
            <div class="mb-3 row">
                <label for="rating" class="form-label">Рейтинг: {{ rating }}</label>
                <input type="range" class="form-range" min="0" max="5" step="1" :value="rating" id="rating" @input="ratingInput" autocomplete="off">
            </div>
            <div class="row d-flex align-items-end">
                <button type="button" class="btn btn-success " @click="sendFeedback" >Отправить отзыв</button>
            </div>
        </div>
    </form>

</template>

<script>
    import axios from 'axios'
    export default {
        name: 'feedback-form',
        props: {
            show: {
                type: Boolean,
                default: false
            },
            product_id: 0
        },
        data() {
            return {
                messages: [],
                summaryFeedback: '',
                positiveFeedback: '',
                negativeFeedback: '',
                rating: 0
            }
        },
        methods: {
            summaryFeedbackInput(event) {
                this.summaryFeedback = event.target.value
            },
            positiveFeedbackInput(event) {
                this.positiveFeedback = event.target.value
            },
            negativeFeedbackInput(event) {
                this.negativeFeedback = event.target.value
            },
            ratingInput(event) {
                this.rating = event.target.value
            },
            sendFeedback() {
                const feedback = {
                    'product': this.product_id,
                    'customer': this.$store.state.user.id,
                    'positive': this.positiveFeedback,
                    'negative': this.negativeFeedback,
                    'summary': this.summaryFeedback,
                    'rating': this.rating
                }
                try {
                    axios(
                      {
                        url: `http://127.0.0.1:8000/api/v1/feedbacks/`,
                        method: 'post',
                        headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                        data: feedback
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
        }
    }
</script>

<style scoped>

</style>