import Main from '@/pages/Main.vue';
import ProductsPage from '@/pages/ProductsPage.vue';
import AboutPage from '@/pages/AboutPage.vue';
import ProductPage from '@/pages/ProductPage.vue';
import {createRouter, createWebHistory} from 'vue-router'

const routes = [
    {
        path: '/',
        component: ProductsPage
    },
    {
        path: '/main',
        component: Main
    },
    {
        path: '/about',
        component: AboutPage
    },
    {
        path: '/products/:id',
        component: ProductPage
    }
]

const router = createRouter({
    routes,
    history: createWebHistory()
});

export default router