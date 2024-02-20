import Main from '@/pages/Main.vue';
import ProductsPage from '@/pages/ProductsPage.vue';
import AboutPage from '@/pages/AboutPage.vue';
import ProductPage from '@/pages/ProductPage.vue';
import CartPage from '@/pages/CartPage.vue'
import RegistrationPage from '@/pages/RegistrationPage.vue'
import EmailActivation from '@/pages/EmailActivation.vue'
import UserActivation from '@/pages/UserActivation.vue'
import SearchPage from '@/pages/SearchPage.vue'
import CheckoutPage from "@/pages/CheckoutPage.vue"
import {createRouter, createWebHistory} from 'vue-router'

const routes = [
    {
        path: '/',
        component: Main,
        name: 'main'
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
    },
    {
        path: '/register_user',
        component: RegistrationPage,
        name: 'register_user'
    },
    {
        path: '/email_activation',
        component: EmailActivation,
        name: 'email_activation'
    },
    {
        path: '/user_activation',
        component: UserActivation,
        name: 'user_activation'
    },
    {
        path: '/search/:query',
        component: SearchPage,
        name: 'search',
    },
    {
        path: '/checkout/:product',
        component: CheckoutPage,
        name: 'checkout'
    }
]

const router = createRouter({
    routes,
    history: createWebHistory()
});

export default router