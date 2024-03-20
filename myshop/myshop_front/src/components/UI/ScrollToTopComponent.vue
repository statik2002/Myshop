<template>
    <button v-if="isVisible" type="button" @click="scrollToTop" class="btn btn-success gotopbtn">
        <i class="bi bi-arrow-up-square"></i>
        {{ isVisible }}
    </button>
</template>

<script>
    export default {
        name: 'scroll-to-top',
        data() {
            return {
                isVisible: false,
                winHeigth: 0,
            }
        },
        methods: {
            scrollToTop(){
                window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
            },
            onResize() {
                console.log(window.scrollbars.visible )
                if(window.scrollbars.visible == true) {
                    this.isVisible = true
                } else {
                    this.isVisible = false
                }
            }
        },
        computed: {

        },
        watch: {
            changeVisivility() {

            }
        },
        mounted() {
            if(window.scrollbars.visible == true) {
                this.isVisible = true
            }
            this.$nextTick(() => {
                window.addEventListener('resize', this.onResize);
            })
        }
    }
</script>

<style scoped>
    .gotopbtn {
        position: fixed;
        font-size: 1.5em;
        bottom: 40px;
        right: 5vw;
        z-index: 9999;
    }
</style>