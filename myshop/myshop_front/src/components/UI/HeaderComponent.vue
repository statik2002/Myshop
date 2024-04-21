<template>
    <!--== Start Header Wrapper ==-->
    <header class="header-area header-default sticky-header">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-6 col-sm-2 col-lg-1">
                    <div class="header-logo-area">
                        <router-link to="/newfront">
                            <img class="logo-main" src="@/assets/img/logo.png" alt="Logo" />
                            <img class="logo d-none" src="@/assets/img/logo-light.png" alt="Logo" />
                        </router-link>
                    </div>
                </div>
                <div class="col-lg-6 d-none d-lg-block">
                    <div class="header-navigation-area">
                        <ul class="main-menu nav position-relative">
                            <li class="has-submenu"><a href="#/">Домой</a>
                                <ul class="submenu-nav">
                                    <li><a href="index.html">Home Demo 1</a></li>
                                    <li><a href="index-two.html">Home Demo 2</a></li>
                                </ul>
                            </li>
                            <li class="has-submenu full-width"><a href="#/">Каталог</a>
                                <ul class="submenu-nav submenu-nav-mega">
                                    <li class="mega-menu-item"><a href="#/" class="mega-title">Shop Layouts</a>
                                        <ul>
                                            <li><a href="shop-3-grid.html">Shop 3 Column</a></li>
                                            <li><a href="shop-4-grid.html">Shop 4 Column</a></li>
                                            <li><a href="shop-left-sidebar.html">Shop Left Sidebar</a></li>
                                            <li><a href="shop.html">Shop Right Sidebar</a></li>
                                            <li><a href="shop-list.html">Shop Listing View</a></li>
                                            <li><a href="shop-list-left-sidebar.html">Shop List left Sidebar</a></li>
                                            <li><a href="shop-list-right-sidebar.html">Shop List Right Sidebar</a></li>
                                        </ul>
                                    </li>
                                    <li class="mega-menu-item"><a href="#/" class="mega-title">Shop Pages</a>
                                        <ul>
                                            <li><a href="login.html">My Account</a></li>
                                            <li><a href="wishlist.html">Wishlist</a></li>
                                            <li><a href="cart.html">Cart</a></li>
                                            <li><a href="checkout.html">Checkout</a></li>
                                        </ul>
                                    </li>
                                    <li class="mega-menu-item"><a href="#/" class="mega-title">WOMEN</a>
                                        <ul>
                                            <li><a href="single-product-name-1.html">Bags &amp; Purses</a></li>
                                            <li><a href="single-product-name-1.html">Beauty</a></li>
                                            <li><a href="single-product-name-1.html">Coats &amp; Jackets</a></li>
                                            <li><a href="single-product-name-1.html">Curve &amp; Plus Size</a></li>
                                            <li><a href="single-product-name-1.html">Denim</a></li>
                                        </ul>
                                    </li>
                                </ul>
                            </li>
                            <li class="has-submenu"><a href="#/">Товары</a>
                                <ul class="submenu-nav">
                                    <li><a href="single-product-simple.html">Simple Product</a></li>
                                    <li><a href="single-product.html">Variable Product</a></li>
                                    <li><a href="single-product-affiliate.html">Affiliate Link product</a></li>
                                    <li><a href="single-product-soldout.html">Soldout Product</a></li>
                                    <li><a href="single-product-countdown.html">Countdown Product</a></li>
                                </ul>
                            </li>
                            <li class="has-submenu"><a href="#/">Blog</a>
                                <ul class="submenu-nav">
                                    <li><a href="blog-left-sidebar.html">Blog Left Sidebar</a></li>
                                    <li><a href="blog.html">Blog Right Sidebar</a></li>
                                    <li><a href="blog-grid.html">Blog Grid Layout</a></li>
                                    <li><a href="single-blog.html">Single Blog Left Sidebar</a></li>
                                    <li><a href="single-blog-right-sidebar.html">Single Blog Right Sidebar</a></li>
                                </ul>
                            </li>
                            <li><a href="contact.html">Контакты</a></li>
                            <li><a href="about-us.html">О нас</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-sm-3 col-lg-3 d-none d-lg-block">
                    <div class="search-form">
                        <form action="#">
                            <div class="form-group">
                                <input class="form-control" type="search" placeholder="Поиск товара">
                                <button class="btn-search"><i class="bi bi-search"></i></button>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="col-sm-9 col-lg-2 d-none d-sm-block text-end">
                    <div class="header-action-area">
                        <ul class="header-action">
                            <li class="search-item d-lg-none">
                                <div class="search-form">
                                    <form action="#">
                                        <div class="form-group">
                                            <input class="form-control" type="search" placeholder="Поиск товара">
                                            <button class="btn-search"><i class="bi bi-search"></i></button>
                                        </div>
                                    </form>
                                </div>
                            </li>
                            <li class="currency-menu">
                                <router-link class="action-item" to="#"><i class="bi bi-lock" style="font-size: 1.3rem;"></i></router-link>
                                <ul class="currency-dropdown">
                                    <li class="account py-2">
                                        <a href="#"><span class="current-account">Акаунт</span></a>
                                        <ul v-if="!$store.state.userIsAuth">
                                            <li><a href="#offcanvasLoginView" data-bs-toggle="modal" role="button" aria-controls="offcanvasLoginView">Войти</a></li>
                                            <li><a href="login.html">Регистрация</a></li>
                                        </ul>
                                        <ul v-else>
                                            <li><a href="cabinet.html">Личный кабинет</a></li>
                                            <li><a href="#" @click="userLogout">Выйти</a></li>
                                        </ul>
                                    </li>
                                    <li class="currency">
                                        <a href="#/"><span class="current-currency">USD</span></a>
                                        <ul>
                                            <li class="active"><a href="#/">USD - US Dollar</a></li>
                                            <li class="#/"><a href="#/">EUR - Euro</a></li>
                                            <li class="#/"><a href="#/">GBP - British Pound</a></li>
                                            <li class="#/"><a href="#/">INR - Indian Rupee</a></li>
                                            <li class="#/"><a href="#/">BDT - Bangladesh Taka</a></li>
                                            <li class="#/"><a href="#/">JPY - Japan Yen</a></li>
                                            <li class="#/"><a href="#/">CAD - Canada Dollar</a></li>
                                            <li class="#/"><a href="#/">AUD - Australian Dollar</a></li>
                                        </ul>
                                    </li>
                                </ul>
                            </li>
                            <li class="mini-cart">
                                <router-link to="" class="action-item">
                                    <i class="bi bi-heart" style="font-size: 1.3rem;"></i>
                                    <span v-if="$store.getters.getLikedProducts > 0" class="cart-quantity">{{ $store.getters.getLikedProducts }}</span>
                                </router-link>
                            </li>
                            <li class="mini-cart">
                                <router-link class="action-item" to="/cart2">
                                    <i class="bi bi-cart-plus" style="font-size: 1.3rem;"></i>
                                    <span class="cart-quantity" v-if="$store.getters.getCartPositionCount > 0">{{ $store.getters.getCartPositionCount }}</span>
                                </router-link>
                                <div class="mini-cart-dropdown">
                                    <div class="cart-item">
                                        <div class="thumb">
                                            <img class="w-100" src="@/assets/img/shop/cart/1.jpg" alt="Image-HasTech">
                                        </div>
                                        <div class="content">
                                            <h5 class="title"><a href="#/">Literature Classical - s</a></h5>
                                            <span class="product-quantity">1 ×</span>
                                            <span class="product-price">$79.00</span>
                                            <a class="cart-trash" href="javascript:void(0);"><i class="fa fa-trash"></i></a>
                                        </div>
                                    </div>
                                    <div class="cart-item">
                                        <div class="thumb">
                                            <img class="w-100" src="@/assets/img/shop/cart/2.jpg" alt="Image-HasTech">
                                        </div>
                                        <div class="content">
                                            <h5 class="title"><a href="#/">Fit Wool Suit - m / gold</a></h5>
                                            <span class="product-quantity">1 ×</span>
                                            <span class="product-price">$80.00</span>
                                            <a class="cart-trash" href="javascript:void(0);"><i class="fa fa-trash"></i></a>
                                        </div>
                                    </div>
                                    <div class="cart-total-money">
                                        <h5>Итого: <span class="money">$159.00</span></h5>
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
                    <button class="btn-menu" type="button"><i class="zmdi zmdi-menu"></i></button>
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
                        <form @submit.prevent>
                            <div class="row">
                                <div class="col-12">
                                    <div class="form-group">
                                        <input v-bind:phone @input="inputPhone" class="form-control" type="text" placeholder="логин" autocomplete="username">
                                    </div>
                                </div>
                                <div class="col-12">
                                    <div class="form-group">
                                        <input v-bind:password @input="inputPassword" class="form-control" type="password" placeholder="пароль" autocomplete="current-password">
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
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'header-component',
        data() {
            return {
                loginModalVisible: false,
                phone: '',
                password: '',
            }
        },
        methods: {
            inputPhone(event) {
                this.phone = event.target.value
            },
            inputPassword(event) {
                this.password = event.target.value
            },
            showLoginDialog() {
                this.loginModalVisible = true
            },
            loginUser() {
                this.messages = []
                if (this.phone.length<12) {
                    this.messages.push('Phone number wrong!')
                    return
                }
                if (this.password.length<3) {
                    this.messages.push('Password wrong!')
                    return
                }
                axios(
                    {
                        method: 'post',
                        url: 'http://127.0.0.1:8000/api/v1/token/login/',
                        headers: {'Content-Type': 'application/json;charset=utf-8'},
                        data: JSON.stringify({'phone_number': this.phone, 'password': this.password})
                    }
                )
                .then((response) => {
                    const token = response.data.access
                    axios(
                        {
                            method: 'get',
                            url: `http://127.0.0.1:8000/api/v1/customers/${response.data.user_id}/`,
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
                    }
                })
            },
            userLogout() {
                this.$store.dispatch('saveUserCartToServer')
                this.$store.commit('logoutUser')
                this.$router.go()
            },
        }
    }
</script>

<style scoped>

</style>