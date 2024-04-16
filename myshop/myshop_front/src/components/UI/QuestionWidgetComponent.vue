<template>
    <div class="card mx-0 rounded-3" style="width: 300px;">
        <div class="card-body">
            <div class="row">
                <div class="col-auto">
                    <img v-if="question.customer.avatar" :src=question.customer.avatar alt="avatar" height="40">
                    <img v-else src="@/assets/avatar_blank.webp" alt="avatar" height="40">
                </div>
                <div class="col">
                <div class="row">{{ question.customer.first_name }} {{ question.customer.last_name }}</div>
                <div class="row datetime">{{ $FormatDate(question.created) }}</div>
                </div>
            </div>
            <p class="card-text mt-3">{{ question.question_text }}</p>
            <div class="card-text">
            <i class="bi bi-hourglass"></i> Ждем ответ продавца
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'question-widget',
        props: {
            question: {type: Object, required: true}
        },
        methods: {
        }
    }
</script>

<style scoped>

</style>