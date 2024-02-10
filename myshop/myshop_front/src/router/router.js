import Main from '@/pages/Main.vue';
import ProductsPage from '@/pages/ProductsPage.vue';
import AboutPage from '@/pages/AboutPage.vue';
import ProductPage from '@/pages/ProductPage.vue';
import CartPage from '@/pages/CartPage.vue'
import {createRouter, createWebHistory} from 'vue-router'

const routes = [
    {
        path: '/',
        component: Main
    },
    {
        path: '/products',
        component: ProductPage
    },
    {
        path: '/about',
        component: AboutPage,
        name: 'about'
    },
    {
        path: '/products/:id',
        component: ProductPage,
        name: 'product'
    },
    {
        path: '/cart',
        component: CartPage,
        name: 'cart'
    }
]

const router = createRouter({
    routes,
    history: createWebHistory()
});

export default router