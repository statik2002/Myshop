import './assets/style.css'

import { createApp } from 'vue'
import App from '@/App.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import router from '@/router/router'
import store from '@/store/'
import components from '@/components/UI'

const app = createApp(App);

components.forEach(component => {
   app.component(component.name, component) 
});

app
    .use(router)
    .use(store)
    .mount('#app')
