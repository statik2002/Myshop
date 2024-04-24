<template>
  <div class="app">
    <accept-cookies v-model:show="acceptCookiesDialog"></accept-cookies>
    <router-view>
    </router-view>
  </div>
</template>

<script>
    export default {
        data() {
            return {
                acceptCookiesDialog: false
            }
        },
        mounted() {
            //Load user from useStorage
            const user = localStorage.getItem('user')
            const unregisteredUser = localStorage.getItem('unregisteredUser')
            if (user) {
                this.$store.state.user = JSON.parse(user)
                this.$store.state.userIsAuth = true
            }
            if (unregisteredUser){
                this.$store.state.unregisteredUser = JSON.parse(unregisteredUser)
                this.$store.state.userIsAuth = false
            }

            if (!this.$cookies.isKey('allow_cookie')) {
                this.$cookies.config('30d')
                this.$cookies.set('allow_cookie', true)
                this.acceptCookiesDialog = true
            }

            this.$store.dispatch('getCatalog')
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
