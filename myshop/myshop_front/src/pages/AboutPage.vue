<template>
    <div>
        <h1>About store. Likes = {{ $store.state.likes }}</h1>
        <h2>Double likes = {{ $store.getters.doubleLikes }}</h2>
        <h2>{{ $store.state.isAuth ? 'Пользователь авторизован' : 'Ползователь не авторизован!' }}</h2>
        <div>
            <button type="button" class="btn btn-primary" @click="$store.commit('incrementLikes')">Like +</button>
        </div>
        <div>
            <button type="button" class="btn btn-primary" @click="$store.commit('decrementLikes')">Disike -</button>
        </div>
        <div><button type="button" class="btn btn-success" @click="$router.push('/')">Back</button></div>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style scoped>

</style>