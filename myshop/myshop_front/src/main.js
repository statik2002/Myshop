import '@/assets/style.css'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import "bootstrap-icons/font/bootstrap-icons.css"


import { createApp } from 'vue'

import App from '@/App.vue'
import router from '@/router/router'
import store from '@/store/'
import components from '@/components/UI'
import VueCookies from 'vue-cookies'

const app = createApp(App);

components.forEach(component => {
   app.component(component.name, component) 
});

app
    .use(router)
    .use(store)
    .use(VueCookies, { expires: '7d'})
    .mount('#app')
