<template>
    <div class="dialog p-2 border" v-if="show">
        <div class="d-flex flex-column justify-content-center gap-2" @click.stop>
            <div>На нашем сайте мы используем файлы cookie для улучшения навигациии и удобного функционала.</div>
            <button type="button" class="btn btn-sm btn-outline-success"  @click="hideDialog">Хорошо</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'accept-cookies',
        props: {
            show: false
        },
        methods: {
            hideDialog() {
                this.$cookies.set('accept_cookie', true)
                this.$emit('update:show', false)
            }
        }
    }
</script>

<style scoped>
.dialog {
    bottom: 10px;
    width: 250px;
    right: 100px;
    border-radius: 10px;
    background: rgba(241, 241, 241, 0.7);
    color: #757575;
    text-align: center;
    position: fixed;
    z-index: 999999;
}

.dialog-content {
    margin: auto;
    background: white;
    color: black;
    border-radius: 10px;
    min-width: 250px;
    min-height: 50px;
    padding: 20px;
}
</style>