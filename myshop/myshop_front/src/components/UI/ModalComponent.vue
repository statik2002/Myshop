<template>
    <div class="dialog" v-if="show" @click="hideDialog">
        <div class="dialog-content" @click.stop>
            <slot></slot>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'modal-component',
        props: {
            show: {
                type: Boolean,
                default: false
            }
        },
        methods: {
            hideDialog() {
                this.$emit('update:show', false)
            }
        }
    }
</script>

<style scoped>
.dialog {
    top: 0px;
    bottom: 0px;
    right: 0px;
    left: 0px;
    background: rgba(0, 0, 0, 0.5);
    position: fixed;
    display: flex;
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