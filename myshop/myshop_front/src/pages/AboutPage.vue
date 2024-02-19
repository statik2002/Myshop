<template>
    <div class="container">
        <div class="d-flex flex-column gap-5">
            <div>About store. Likes = {{ $store.state.likes }}</div>
            <div>Double likes = {{ $store.getters.doubleLikes }}</div>
            <div>User: {{ user }}</div>
            <div>
                <button type="button" class="btn btn-primary" @click="$store.commit('incrementLikes')">Like +</button>
            </div>
            <div>
                <button type="button" class="btn btn-primary" @click="$store.commit('decrementLikes')">Disike -</button>
            </div>
            <div><button type="button" class="btn btn-success" @click="$router.push('/')">Back</button></div>
            <div>
                {{ $store.state.some }}
                <button type="button" class="btn btn-success" @click="changeValue">Change storage Value</button>
            </div>
            <div>
                <div>{{ some }}</div>
                <div>{{ $store.state.some2 }}</div>
                <div><button @click="addSome">Add +</button></div>
            </div>
        </div>
        
    </div>
</template>

<script>
    import { useStorage } from '@vueuse/core'
    export default {
        components: {useStorage},
        data() {
            return {
                user: useStorage('user'),
                some: useStorage('some2')
            }
        },
        methods: {
            changeValue() {
                let value = useStorage('some')
                console.log(value.value)
                useStorage('some', value.value++)
            },
            addSome() {
                let data = JSON.parse(this.some)
                data.val1++
                this.some = JSON.stringify(data)
            }
        }
    }
</script>

<style scoped>

</style>