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
import get_token_plugin from '@/plugins/get_token_plugin'
import format_date from '@/plugins/format_date'

const app = createApp(App);

components.forEach(component => {
   app.component(component.name, component) 
});

app
    .use(router)
    .use(store)
    .use(VueCookies)
    .use(get_token_plugin)
    .use(format_date)
    .mount('#app')
