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
import CabinetPage from '@/pages/CabinetPage.vue';
import OrdersPage from '@/pages/OrdersPage.vue'
import LikePage from '@/pages/LikePage.vue'
import OrderPage from '@/pages/OrderPage.vue';
import TestPage from '@/pages/TestPage.vue';
import NewFrontPage from '@/pages/NewFrontPage.vue'
import ProductPage2 from '@/pages/ProductPage2.vue'
import CartPage2 from '@/pages/CartPage2.vue';
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
    },
    {
        path: '/cabinet',
        component: CabinetPage,
        name: 'cabinet'
    },
    {
        path: '/orders',
        component: OrdersPage,
        name: 'orders'
    },
    {
        path: '/likes',
        component: LikePage,
        name: 'likes'
    },
    {
        path: '/order/:id',
        component: OrderPage,
        name: 'show_order'
    },
    {
        path: '/testpage',
        component: TestPage,
        name: 'testpage'
    },
    {
        path: '/newfront',
        component: NewFrontPage,
        name: 'newfront'
    },
    {
        path: '/product2/:id',
        component: ProductPage2,
        name: 'product2'
    },
    {
        path: '/cart2',
        component: CartPage2,
        name: 'cart2'
    }
]

const router = createRouter({
    routes,
    history: createWebHistory()
});

export default router