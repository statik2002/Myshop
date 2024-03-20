<template>
  <div class="app">
    <router-view>
    </router-view>
  </div>
</template>

<script>
    import { useStorage } from '@vueuse/core'
    export default {
        mounted() {
            const localStorageCart = localStorage.getItem('cart')
            if (localStorageCart) {
                this.$store.state.cart = JSON.parse(localStorageCart)
            } else {
                localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
            }

            //Load user from useStorage
            const user = localStorage.getItem('user')
            if (user) {
                this.$store.state.user = JSON.parse(user)
                this.$store.state.userIsAuth = true
            } else {
                this.$store.state.userIsAuth = false
            }
        }
  }
</script>

<style>
.menu-background {
    background: linear-gradient(to right, rgb(26, 158, 0), rgb(58, 184, 27));
}
.menu1 {
    color: rgba(231, 231, 231, 0.5);
}

.menu1 a:link {
    color: rgba(231, 231, 231, 0.5);
    text-decoration: none;
    font-size: 14px;
}

.menu1 a:visited {
    color: white;
    text-decoration: none;
}

.menu1 a:hover {
    color: white;
    text-decoration: none;
}
.logo {
    -webkit-text-stroke:1px rgb(255, 255, 255);
    color: rgb(255, 208, 0);
}

.logo a:link {
    -webkit-text-stroke:1px rgb(255, 255, 255);
    color: rgb(255, 208, 0);
    text-decoration: none;
}

.logo a:visited {
    text-decoration: none;
}

.logo a:hover {
    text-decoration: underline dotted;
    text-decoration-thickness: 1px;
}

.logoM {
    color: red;
}

.logo-end {
    color: green;
    font-size: 0.8em;
}
.search-line-icon {
    font-size: 0.8rem;
}

.has-search .form-control {
    padding-left: 2.375rem;
    border: none;
    background-color: #F5F5F5;
    border-radius: 0.5rem;
    height: 3rem;
}

.has-search .form-control-feedback {
    position: absolute;
    z-index: 2;
    display: block;
    width: 2.375rem;
    height: 2.375rem;
    line-height: 2.375rem;
    text-align: center;
    pointer-events: none;
    color: #aaa;
}
</style>
