<template>
    <div class="card-body p-3">
        <div class="row">
            <rating-component :rating="feedback.rating"></rating-component>
        </div>
        <div class="row pe-2 pt-2">
            <div class="col-auto" v-if="feedback.customer.avatar">
                <img :src=feedback.customer.avatar :alt=feedback.customer.id height="40">
            </div> 
            <div class="col">
                <div class="row">{{ feedback.customer.first_name }} {{ feedback.customer.last_name }}</div>
                <div class="row datetime">{{ formatDate(feedback.post_at) }}</div>
            </div>
        </div>
        <p class="card-text pt-3">{{ feedback.summary }}</p>
    </div>
</template>

<script>
    export default {
        name: 'feedback-widget',
        props: {
            feedback: {
                type: Object,
                required: true
            }
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