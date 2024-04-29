<template>
    <div class="d-flex flex-row">
        <div>
            <span v-for="star in blank_rating">
                <i v-if="star==1" class="bi bi-star-fill star"></i>
                <i v-else class="bi bi-star star"></i>
            </span>
        </div>
        <div class="ps-1 fw-lighter fst-italic" v-if="num_rating">
            &#x2022; {{ num_rating }} 
            <span v-if="num_rating==1 || num_rating/10==1">оценка</span><span v-else>оценок</span> 
        </div>
    </div>
    
</template>

<script>
    export default {
        name: 'rating-component',
        props: {
            rating: Number,
            num_rating: Number
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