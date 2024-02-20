<template>
    <div class="container">
        <div class="d-flex flex-column gap-5">
            <div>About store. Likes = {{ $store.state.likes }}</div>
            <div>Double likes = {{ $store.getters.doubleLikes }}</div>
            <div>
                <button type="button" class="btn btn-primary" @click="$store.commit('incrementLikes')">Like +</button>
            </div>
            <div>
                <button type="button" class="btn btn-primary" @click="$store.commit('decrementLikes')">Disike -</button>
            </div>
            <div><button type="button" class="btn btn-success" @click="$router.push('/')">Back</button></div>
            <div>{{ $store.state.user }}</div>
        </div>
    </div>
</template>

<script>
    import { useStorage } from '@vueuse/core'
    export default {
        data() {
            return {
            }
        },
        methods: {
        }
    }
</script>

<style scoped>

</style>