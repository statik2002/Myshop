<template>
    <div v-bind="scrollClass" @click="scrollUp">
        <i class="bi bi-arrow-up-square"></i>
    </div>
</template>

<script>
    export default { 
        name: 'scroll-to-top',
        data() {
            return {
                scrollClass: {
                    id: 'scroll-id',
                    class: 'scroll-to-top',
                },
                lastScroll: 0
            }
        },
        methods: {
            scrollToTop(event){ 
                const scrollY = window.top.scrollY
                const windowHeight = window.innerHeight

                if (scrollY < this.lastScroll) {
                    if (scrollY < windowHeight) {
                        this.scrollClass.class = 'scroll-to-top'
                    } else {
                        this.scrollClass.class = 'scroll-to-top show'
                    } 
                } else {
                    if (scrollY > windowHeight) {
                        this.scrollClass.class = 'scroll-to-top show'
                    } else {
                        this.scrollClass.class = 'scroll-to-top'
                    }
                }
                this.lastScroll = scrollY
            },
            scrollUp() {
                window.scrollTo({top: 0, behavior: "smooth"})
            }
        },
        computed: {

        },
        mounted() {
            window.addEventListener('scroll', this.scrollToTop);
        }
    }
</script>

<style scoped>
</style>