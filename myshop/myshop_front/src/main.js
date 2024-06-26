import '@/assets/css/animate.css'
import '@/assets/css/elegant-icons.css'
import '@/assets/css/headroom.css'
import '@/assets/css/ionicons.css'
import '@/assets/css/material-design-iconic-font.css'
import '@/assets/css/style.css'
import '@/assets/css/my.css'

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
import humanizie_order from './plugins/humanizie_order'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

const app = createApp(App);

components.forEach(component => {
   app.component(component.name, component) 
});

app.component('font-awesome-icon', FontAwesomeIcon)

app
    .use(router)
    .use(store)
    .use(VueCookies)
    .use(get_token_plugin)
    .use(format_date)
    .use(humanizie_order)
    .mount('#app')
