<template>
    <!--== Start Header Wrapper ==-->
    <header class="header-area header-default sticky-header">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-6 col-sm-2 col-lg-2">
                    <div class="header-logo-area">
                        <router-link to="/">
                            <img class="logo-main" src="@/assets/img/logo_m3.png" alt="Logo" />
                            <img class="logo d-none" src="@/assets/img/logo_m3.png" alt="Logo" />
                        </router-link>
                    </div>
                </div>
                <div class="col-lg-5 d-none d-lg-block">
                    <div class="header-navigation-area">
                        <ul class="main-menu nav position-relative">
                            <li class="has-submenu"><a href="#/">Покупателям</a>
                                <ul class="submenu-nav">
                                    <li v-for="page in $store.state.simplePages">
                                        <router-link :to="{name: 'simplePage', params: {pk: page.pk}}">{{ page.title }}</router-link>
                                    </li>
                                </ul>
                            </li>
                            <li class="has-submenu full-width"><a href="#/">Каталог</a>
                                <ul class="submenu-nav">
                                    <li v-for="catalog in $store.getters.getCatalog">
                                        <a href="shop-3-grid.html">{{ catalog.name }}</a>
                                    </li>
                                </ul>
                            </li>
                            <li class="has-submenu"><a href="#/">Акции</a>
                                <ul class="submenu-nav">
                                    <li><a href="single-product-simple.html">Распродажа обоев</a></li>
                                    <li><a href="single-product.html">Уцененные товары</a></li>
                                    <li><a href="single-product-affiliate.html">Скидки</a></li>
                                </ul>
                            </li>
                            <!--
                            <li class="has-submenu"><a href="#/">Blog</a>
                                <ul class="submenu-nav">
                                    <li><a href="blog-left-sidebar.html">Blog Left Sidebar</a></li>
                                    <li><a href="blog.html">Blog Right Sidebar</a></li>
                                    <li><a href="blog-grid.html">Blog Grid Layout</a></li>
                                    <li><a href="single-blog.html">Single Blog Left Sidebar</a></li>
                                    <li><a href="single-blog-right-sidebar.html">Single Blog Right Sidebar</a></li>
                                </ul>
                            </li>
                            -->
                            <li><a href="contact.html">Контакты</a></li>
                            <li><a href="about-us.html">О нас</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-sm-3 col-lg-2 d-none d-lg-block">
                    <div class="search-form">
                        <div class="form-group">
                            <input v-model="searchQuery" class="form-control" id="searchlg" type="search" placeholder="Поиск товара" @change="$router.push({name: 'search2', params: {query: searchQuery}})">
                            <button class="btn-search" @click="$router.push({name: 'search2', params: {query: searchQuery}})"><i class="bi bi-search"></i></button>
                        </div>
                    </div>
                </div>
                <div class="col-sm-9 col-lg-3 d-none d-sm-block text-end">
                    <div class="header-action-area">
                        <ul class="header-action">
                            <li class="search-item d-lg-none">
                                <div class="search-form">
                                    <form action="#">
                                        <div class="form-group">
                                            <input class="form-control" id="searchsm" type="search" placeholder="Поиск товара">
                                            <button class="btn-search"><i class="bi bi-search"></i></button>
                                        </div>
                                    </form>
                                </div>
                            </li>
                            <li class="currency-menu">
                                <router-link class="action-item" to="#"><i class="bi bi-lock" style="font-size: 1.3rem;"></i></router-link>
                                <ul class="currency-dropdown">
                                    <li class="account">
                                        <a href="#"><span class="current-account">Акаунт</span></a>
                                        <ul v-if="!$store.getters.isUserLogin">
                                            <li><a href="#offcanvasLoginView" data-bs-toggle="modal" role="button" aria-controls="offcanvasLoginView">Войти</a></li>
                                            <li><router-link to="/register_user">Регистрация</router-link></li>
                                        </ul>
                                        <ul v-else>
                                            <li><router-link to="/cabinet2">Личный кабинет</router-link></li>
                                            <li><a href="#" @click="userLogout">Выйти</a></li>
                                        </ul>
                                    </li>
                                </ul>
                            </li>
                            <li class="mini-cart">
                                <router-link to="/like2" class="action-item">
                                    <i class="bi bi-heart" style="font-size: 1.3rem;"></i>
                                    <span v-if="$store.getters.getLikedProductsCount > 0" class="cart-quantity">{{ $store.getters.getLikedProductsCount }}</span>
                                </router-link>
                            </li>
                            <li class="mini-cart">
                                <router-link class="action-item" to="/cart2">
                                    <i class="bi bi-cart-plus" style="font-size: 1.3rem;"></i>
                                    <span class="cart-quantity" v-if="$store.getters.getCartPositionCount > 0">{{ $store.getters.getCartPositionCount }}</span>
                                </router-link>
                                <div class="mini-cart-dropdown">
                                    <div class="cart-item" v-for="cartItem in $store.getters.productsInCart">
                                        <div class="thumb">
                                            <img v-if="cartItem.product.product_images.length > 0" class="w-100" :src=cartItem.product.product_images[0].image :alt=cartItem.product.product_images[0].alt>
                                            <img v-else class="w-100" src="@/assets/no_image.png" alt="no image">
                                        </div>
                                        <div class="content">
                                            <h5 class="title"><a href="#/">{{ cartItem.product.name }}</a></h5>
                                            <span class="product-quantity">{{ cartItem.quantity }} × {{ cartItem.fixed_price }} &#8381;</span>
                                            <a class="cart-trash" href="#" @click="$store.commit('deleteProductFromCart', cartItem.id)"><i class="bi bi-trash3"></i></a>
                                        </div>
                                    </div>
                                    <div class="cart-total-money">
                                        <h5>Итого: <span class="money">{{ $store.getters.getCartTotal }} &#8381;</span></h5>
                                    </div>
                                    <div class="cart-btn">
                                        <router-link to="/cart2">Открыть корзину</router-link>
                                        <a href="checkout.html">Оплатить</a>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="col-6 col-sm-1 d-block d-lg-none text-end">
                    <button class="btn-menu" type="button" id="togler" data-bs-toggle="offcanvas" data-bs-target="#sideMenu" aria-controls="sideMenu">
                        <i class="zmdi zmdi-menu"></i>
                    </button>
                </div>
            </div>
        </div>
    </header>
    <!--== End Header Wrapper ==-->
    <!--== Start Quick View Menu ==-->
    <div class="modal" tabindex="-1" id="offcanvasLoginView">
        <div class="modal-dialog product-quick-view-inner">
            <div class="product-quick-view-content">
                <div class="account-form-wrap">
                    <div class="login-form">
                        <div class="content">
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                                <i class="bi bi-x-lg"></i>
                            </button>
                            <h4 class="title">Войти в аккаунт</h4>
                            <p>Введите ваши учетные данные.</p>
                        </div>
                        <div v-if="messages.length > 0">
                            <div class="alert alert-danger" role="alert" v-for="message in messages">
                                {{ message }}
                            </div>
                        </div>
                        <form @submit.prevent>
                            <div class="row">
                                <div class="col-12">
                                    <div class="form-group">
                                        <input 
                                        v-model="phone" 
                                        id="phone" 
                                        class="form-control" 
                                        type="tel" 
                                        placeholder="Телефон" 
                                        v-mask="['(+7) ###-###-##-##']"
                                        autocomplete="username"
                                        >
                                    </div>
                                </div>
                                <div class="col-12">
                                    <div class="form-group">
                                        <input v-model="password" id="password" class="form-control" type="password" placeholder="пароль" autocomplete="current-password">
                                    </div>
                                </div>
                                <div class="col-12">
                                    <div class="login-form-group">
                                        <button class="btn-sign" type="submit" @click="loginUser">Войти</button>
                                        <a class="btn-pass-forgot" href="#/">Забыли пароль?</a>
                                    </div>
                                </div>
                                <div class="col-12">
                                    <div class="account-optional-group">
                                        <a class="btn-create" href="#/">Зарегистрироваться</a>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!--== End Quick View Menu ==-->  

    <!--== Start Side Menu ==-->
    <aside class="offcanvas offcanvas-start right-menu" tabindex="-1" id="sideMenu">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Меню</h5>
            <button type="button" id="offCanvasCloseButton" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            <div class="search-form">
                <div class="form-group">
                    <input v-model="searchQuery" class="form-control" id="search" type="search" placeholder="Поиск товара" @change="makeSearch">
                    <button class="btn-search" data-bs-dismiss="offcanvas" @click="$router.push({name: 'search2', params: {query: searchQuery}})"><i class="bi bi-search"></i></button>
                </div>
            </div>
            <div class="d-flex flex-column">
                <button class="btn btn-link" data-bs-dismiss="offcanvas" @click="$router.push('newfront')">Главная</button>
                <div class="d-flex flex-row justify-content-evenly" v-if="$store.getters.isUserLogin">
                    <button class="btn btn-link" data-bs-dismiss="offcanvas" @click="$router.push('/cabinet2')">Кабинет</button>
                    <button class="btn btn-link" data-bs-dismiss="offcanvas" @click="userLogout">Выйти</button>
                </div>
                <div class="d-flex flex-row justify-content-evenly" v-else>
                    <button class="btn-theme" data-bs-target="#offcanvasLoginView" data-bs-toggle="modal" type="button" aria-controls="offcanvasLoginView">
                        Войти
                    </button>
                </div>
                
                <button class="btn btn-link" data-bs-dismiss="offcanvas" @click="$router.push('/like2')">Лайки</button>
                <button class="btn btn-link" data-bs-dismiss="offcanvas" @click="$router.push('/cart2')">Корзина</button>
            </div>
        </div>
    </aside>
    <!--== End Side Menu ==-->
</template>

<script>
    import axios from 'axios'
    import { mask } from 'vue-the-mask';
    export default {
        name: 'header-component',
        directives: { mask },
        data() {
            return {
                loginModalVisible: false,
                phone: '',
                password: '',
                searchQuery: '',
                messages: []
            }
        },
        methods: {
            showLoginDialog() {
                this.loginModalVisible = true
            },
            loginUser() {
                this.messages = []
                if (this.password.length<3) {
                    this.messages.push('Пароль не должен быть меньше 3-х символов!')
                    return
                }
                axios(
                    {
                        method: 'post',
                        url: `${this.$store.state.apiUrl}/api/v1/token/login/`,
                        headers: {'Content-Type': 'application/json;charset=utf-8'},
                        data: JSON.stringify({'phone_number': this.phone, 'password': this.password})
                    }
                )
                .then((response) => {
                    const token = response.data.access
                    axios(
                        {
                            method: 'get',
                            url: `${this.$store.state.apiUrl}/api/v1/customers/${response.data.user_id}/`,
                            headers: {'Content-Type': 'application/json;charset=utf-8', "Authorization" : `Bearer ${token}`},
                        }
                    )
                    .then((response) => {
                        this.$store.commit('setUser', response.data)
                        this.$cookies.set('login', this.phone)
                        this.$router.go()

                    })
                    .catch((error) => {
                        console.log(error)
                    })
                })
                .catch((error) => {
                    if (error.response.data.error) {
                        this.messages.push(error.response.data.error)
                        console.log(error.response.data.error)
                    }
                })
            },
            userLogout() {
                this.$store.dispatch('saveUserCartToServer')
                this.$store.commit('logoutUser')
                this.$router.push('/')
            },
            makeSearch() {
                document.getElementById("offCanvasCloseButton").click()
                this.$router.push({name: 'search2', params: {query: this.searchQuery}})
            }
        }
    }
</script>

<style scoped>

</style>