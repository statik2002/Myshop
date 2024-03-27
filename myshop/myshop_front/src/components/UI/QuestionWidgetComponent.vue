<template>
    <div class="card mx-0 rounded-3" style="width: 300px;">
        <div class="card-body">
            <div class="row">
                <div class="col-auto">
                <img src="..." alt="" height="40">
                </div>
                <div class="col">
                <div class="row">{{ question.customer.first_name }} {{ question.customer.last_name }}</div>
                <div class="row datetime">{{ formatDate(question.created) }}</div>
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
            formatDate(date){
                date = new Date(date)
                let year = new Intl.DateTimeFormat('ru', { year: 'numeric' }).format(date);
                let month = new Intl.DateTimeFormat('ru', { month: 'short' }).format(date);
                let day = new Intl.DateTimeFormat('ru', { day: '2-digit' }).format(date);
                let hour = new Intl.DateTimeFormat('ru', { hour: '2-digit' }).format(date);
                let minute = new Intl.DateTimeFormat('ru', { minute: '2-digit' }).format(date);
                return `${day} ${month} ${year} ${hour}:${minute}`
            },
        }
    }
</script>

<style scoped>

</style>