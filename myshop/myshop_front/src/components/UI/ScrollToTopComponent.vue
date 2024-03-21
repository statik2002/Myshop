<template>
    <button v-if="isVisible" type="button" @click="scrollToTop" class="btn btn-success gotopbtn" id="scrollButton">
        <i class="bi bi-arrow-up-square"></i>
    </button>
</template>

<script>
    export default {
        name: 'scroll-to-top',
        props: {
            productsContainer: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                isVisible: true,
            }
        },
        methods: {
            scrollToTop(){
                window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
            },
            onResize() {
                if(this.getHeigth() > window.innerHeight) {
                    this.isVisible = true
                    let button = document.getElementById('scrollButton')
                    if (!button) return
                    if (this.productsContainer.innerContainer.getBoundingClientRect().bottom > window.innerHeight) {
                            button.style.position = 'fixed'
                            button.style.right = 20+'px'
                            button.style.bottom = 20+'px'
                    } else {
                       this.isVisible = false
                    }
                } else {
                    this.isVisible = false
                }

            },
            onScroll() {
                if(this.getHeigth() > window.innerHeight) {
                    this.isVisible = true
                    let button = document.getElementById('scrollButton')

                    if (!button) return
                    if (!this.isEmptyObject(this.productsContainer.innerContainer)) return

                    if (this.productsContainer.innerContainer.getBoundingClientRect().bottom > window.innerHeight) {
                        button.style.position = 'fixed'
                        button.style.right = 20+'px'
                        button.style.bottom = 20+'px'
                    } else {
                        button.style.position = 'fixed'
                        button.style.right = 20+'px'
                        button.style.bottom = window.innerHeight - this.productsContainer.innerContainer.getBoundingClientRect().bottom+20+'px'
                    }
                } else {
                    this.isVisible = false
                }
            },

            getHeigth() {
                return Math.max(
                    document.body.scrollHeight, document.documentElement.scrollHeight,
                    document.body.offsetHeight, document.documentElement.offsetHeight,
                    document.body.clientHeight, document.documentElement.clientHeight
                    );
            },

            isEmptyObject(obj) {
                return JSON.stringify(obj) ==='{}';
            }
        },
        computed: {

        },
        watch: {
            productsContainer(newProductContainer, oldProductContainer) {         
                if (newProductContainer.isLoaded) {
                    if(this.getHeigth() > window.innerHeight) {
                        this.isVisible = true
                        let button = document.getElementById('scrollButton')
                        if (this.productsContainer.innerContainer.getBoundingClientRect().bottom > window.innerHeight) {
                            button.style.position = 'absolute'
                            button.style.bottom = 20+'px'
                        } else {
                           this.isVisible = false
                        }
                    } else {
                        this.isVisible = false
                    }
                }
            }
        },
        mounted() {
            this.$nextTick(() => {
                window.addEventListener('resize', this.onResize);
                window.addEventListener('scroll', this.onScroll);
            })
        }
    }
</script>

<style scoped>
    .gotopbtn {
        position: fixed;
        font-size: 1.5em;
        bottom: 20px;
        right: 20px;
        z-index: 9999;
    }
</style>