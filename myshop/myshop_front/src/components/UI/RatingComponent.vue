<template>
    <div class="d-flex flex-row">
        <div v-for="(value, index) in blank_rating">
            <i class="bi bi-star-fill star" v-if="blank_rating[index]===1"></i>
            <i class="bi bi-star star-no" v-else></i>
        </div>
    </div>
    
</template>

<script>
    export default {
        name: 'rating-component',
        props: {
            rating: Number
        },
        data() {
            return {
                blank_rating: [0, 0, 0, 0, 0]
            }
        },
        methods: {
            fill_rating(){
                for(let index=0; index<this.rating; index++){
                    this.blank_rating[index] = 1
                }
            }
        },
        mounted() {
            this.fill_rating()
        }
    }
</script>

<style scoped>

</style>