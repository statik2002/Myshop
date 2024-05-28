<template>
  <div class="app">
    <accept-cookies v-model:show="acceptCookiesDialog"></accept-cookies>
    <router-view>
    </router-view>
  </div>
  <!-- Yandex.Metrika counter -->
    <script type="text/javascript" >
    (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
    m[i].l=1*new Date();
    for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
    k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
    (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

    ym(97412226, "init", {
            clickmap:true,
            trackLinks:true,
            accurateTrackBounce:true,
            ecommerce:"dataLayer"
    });
    </script>
    <noscript><div><img src="https://mc.yandex.ru/watch/97412226" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
    <!-- /Yandex.Metrika counter -->
</template>

<script>
    export default {
        data() {
            return {
                acceptCookiesDialog: false
            }
        },
        methods:
        {
            async uploadSimplePages() {
                try {
                    let response = await fetch(
                        `${this.$store.state.apiUrl}/api/v1/simple_pages/`,
                        {method: 'GET'}
                    );
                    if (response.ok) {
                        let pages = await response.json();
                        this.$store.state.simplePages = pages.results
                    } else {
                        alert('Error get pages');
                    }
                } catch(e) {
                    console.log(`Connection error ${e}`);
                }
            },
        },
        mounted() {
            //Load user from useStorage
            const DEBUG = import.meta.env.VITE_DEBUG
            this.$store.state.apiUrl = import.meta.env.VITE_DEV_URL
            this.$store.state.mediaUrl = import.meta.env.VITE_DEV_MEDIA_URL
            if (DEBUG=='false'){
                this.$store.state.apiUrl = import.meta.env.VITE_PROD_URL
                this.$store.state.mediaUrl = import.meta.env.VITE_PROD_MEDIA_URL
            }
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
            this.uploadSimplePages()
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
