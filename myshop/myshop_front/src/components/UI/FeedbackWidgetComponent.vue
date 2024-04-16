<template>
    <div class="card-body">
        <div class="d-flex flex-row gap-2">
            <div class="" v-if="feedback.customer.avatar">
                <img :src=feedback.customer.avatar :alt=feedback.customer.id height="40">
            </div> 
            <div class="">
                <div class="d-flex flex-row justify-content-between gap-2">
                    <div>
                        {{ feedback.customer.first_name }} {{ feedback.customer.last_name }}
                    </div>
                    <div class="d-flex">
                        <i class="bi bi-star-fill star"></i>
                        {{ feedback.rating }}
                    </div>
                </div>
                <div class="d-flex datetime">{{ $FormatDate(feedback.post_at) }}</div>
            </div>
        </div>
        <p class="card-text pt-3">{{ feedback.summary }}</p>
        <p class="card-text pt-3"><i class="bi bi-plus-circle"></i> {{ feedback.positive }}</p>
        <p class="card-text pt-3"><i class="bi bi-dash-circle"></i> {{ feedback.negative }}</p>
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
        }
    }
</script>

<style scoped>

</style>