<template>
    <div class="col-xxl-4 col-xl-4 col-lg-4 col-md-6 col-sm-6 mb-3">
        <div class="widget p-3 h-100">
            <div class="d-flex flex-column justify-content-between h-100">
                <slot></slot>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'widget-component'
    }
</script>

<style scoped>

</style>