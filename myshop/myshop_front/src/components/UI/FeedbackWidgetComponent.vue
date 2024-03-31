<template>
    <div class="card-body p-3">
        <div class="row pe-2 pt-2">
            <div class="col-auto" v-if="feedback.customer.avatar">
                <img :src=feedback.customer.avatar :alt=feedback.customer.id height="40">
            </div> 
            <div class="col">
                <div class="d-flex flex-row justify-content-between">
                    <div>
                        {{ feedback.customer.first_name }} {{ feedback.customer.last_name }}
                    </div>
                    <div class="ps-5">
                        <i class="bi bi-star-fill star"></i>
                        {{ feedback.rating }}
                    </div>
                </div>
                <div class="d-flex datetime">{{ formatDate(feedback.post_at) }}</div>
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