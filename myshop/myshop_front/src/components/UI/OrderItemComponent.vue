<template>
    <div class="widget">
        <div class="d-flex gap-3 p-2">
            <div>ID: {{ order.id }}</div>
            <div>Created: {{ formatDate(order.order_create) }}</div>
            <div>Status: {{ order.order_status }}</div>
            <div>Total: {{ order.total_amount }} Руб.</div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'order-item',
        props: {
            order: {
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
            }
        }
    }
</script>

<style scoped>

</style>