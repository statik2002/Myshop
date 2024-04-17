<template>
    <div class="wrapper">
        <!--== Start Header Wrapper ==-->
        <header class="header-area header-default sticky-header">
            <div class="container">
            <div class="row align-items-center">
                <div class="col-6 col-sm-4 col-lg-3">
                <div class="header-logo-area">
                    <a href="index.html">
                    <img class="logo-main" src="@/assets/img/logo.png" alt="Logo" />
                    <img class="logo d-none" src="@/assets/img/logo-light.png" alt="Logo" />
                    </a>
                </div>
                </div>
                <div class="col-sm-4 col-lg-7 d-none d-lg-block">
                <div class="header-navigation-area">
                    <ul class="main-menu nav position-relative">
                    <li class="has-submenu"><a href="#/">Home</a>
                        <ul class="submenu-nav">
                        <li><a href="index.html">Home Demo 1</a></li>
                        <li><a href="index-two.html">Home Demo 2</a></li>
                        </ul>
                    </li>
                    <li class="has-submenu full-width"><a href="#/">Shop</a>
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
                    <li class="has-submenu"><a href="#/">Products</a>
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
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="about-us.html">About</a></li>
                    </ul>
                </div>
                </div>
                <div class="col-sm-7 col-lg-2 d-none d-sm-block text-end">
                <div class="header-action-area">
                    <ul class="header-action">
                    <li class="search-item">
                        <a class="action-item" href="page-search.html">
                        <i class="zmdi zmdi-search icon"></i>
                        </a>
                    </li>
                    <li class="currency-menu">
                        <a class="action-item" href="#/"><i class="zmdi zmdi-lock-outline icon"></i></a>
                        <ul class="currency-dropdown">
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
                        <li class="account">
                            <a href="#/"><span class="current-account">My account</span></a>
                            <ul>
                            <li><a href="login.html">Login</a></li>
                            </ul>
                        </li>
                        </ul>
                    </li>
                    <li class="mini-cart">
                        <a class="action-item" href="#/">
                        <i class="zmdi zmdi-shopping-cart-plus icon"></i>
                        <span class="cart-quantity">2</span>
                        </a>
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
                            <h5>Total: <span class="money">$159.00</span></h5>
                        </div>
                        <div class="cart-btn">
                            <a href="cart.html">View Cart</a>
                            <a href="checkout.html">Checkout</a>
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

        <main class="main-content">
            <!--== Start Hero Area Wrapper ==-->
            <section class="">
                <div id="carouselMainIndicators" class="carousel slide" data-bs-ride="true">
                    <div class="carousel-indicators">
                        <button type="button" data-bs-target="#carouselMainIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                        <button type="button" data-bs-target="#carouselMainIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                        <button type="button" data-bs-target="#carouselMainIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="@/assets/img/slider/slider-01.jpg" class="d-block w-100" alt="...">
                            <div class="carousel-caption d-none d-md-block slider-text">
                                <h5 class="slider-text-header">First slide label</h5>
                                <p class="slider-text-content">Some representative placeholder content for the first slide.</p>
                                <button class="btn btn-danger slider-button">BUY</button>
                            </div>
                        </div>
                        <div class="carousel-item">
                            <img src="@/assets/img/slider/slider-01.jpg" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                            <img src="@/assets/img/slider/slider-01.jpg" class="d-block w-100" alt="...">
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselMainIndicators" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselMainIndicators" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </section>
            <!--== End Hero Area Wrapper ==-->

            <!--== Start Product Area Wrapper ==-->
            <section class="container-xl py-5 border">
                <div class="row g-2 border">
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-3 col-sm-6 border">
                        <!--== Start Shop Item ==-->
                        <div class="product-item">
                            <div class="inner-content">
                                <div class="product-thumb">
                                    <a href="single-product-simple.html">
                                        <img class="w-100" src="@/assets/img/shop/oboi1.png" alt="Image-HasTech">
                                    </a>
                                    <div class="product-action">
                                        <div class="addto-wrap">
                                            <a class="add-cart" href="cart.html">
                                            <i class="zmdi zmdi-shopping-cart-plus icon"></i>
                                            </a>
                                            <a class="add-wishlist" href="wishlist.html">
                                            <i class="zmdi zmdi-favorite-outline zmdi-hc-fw icon"></i>
                                            </a>
                                            <a class="add-quick-view" href="javascript:void(0);">
                                            <i class="zmdi zmdi-search icon"></i>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="product-desc">
                                    <div class="product-info">
                                    <h4 class="title"><a href="single-product-simple.html">Flower Print dress</a></h4>
                                    <div class="star-content">
                                        <i class="fa fa-star-o"></i>
                                        <i class="fa fa-star-o"></i>
                                        <i class="fa fa-star-o"></i>
                                        <i class="fa fa-star-o"></i>
                                        <i class="fa fa-star-o"></i>
                                    </div>
                                    <div class="prices">
                                        <span class="price">$50.00</span>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--== End Shop Item ==-->
                    </div>
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-3 col-sm-6 border">
                        <!--== Start Shop Item ==-->
                        <div class="product-item">
                            <div class="inner-content">
                            <div class="product-thumb">
                                <a href="single-product-simple.html">
                                <img class="w-100" src="@/assets/img/shop/6.jpg" alt="Image-HasTech">
                                </a>
                                <div class="product-action">
                                <div class="addto-wrap">
                                    <a class="add-cart" href="cart.html">
                                    <i class="zmdi zmdi-shopping-cart-plus icon"></i>
                                    </a>
                                    <a class="add-wishlist" href="wishlist.html">
                                    <i class="zmdi zmdi-favorite-outline zmdi-hc-fw icon"></i>
                                    </a>
                                    <a class="add-quick-view" href="javascript:void(0);">
                                    <i class="zmdi zmdi-search icon"></i>
                                    </a>
                                </div>
                                </div>
                            </div>
                            <div class="product-desc">
                                <div class="product-info">
                                <h4 class="title"><a href="single-product-simple.html">Fit Wool Suit</a></h4>
                                <div class="star-content">
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                </div>
                                <div class="prices">
                                    <span class="price">$80.00</span>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <!--== End Shop Item ==-->
                    </div>
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-3 col-sm-6 border">
                        <!--== Start Shop Item ==-->
                        <div class="product-item">
                            <div class="inner-content">
                            <div class="product-thumb">
                                <a href="single-product-simple.html">
                                <img class="w-100" src="@/assets/img/shop/5.jpg" alt="Image-HasTech">
                                </a>
                                <div class="product-action">
                                <div class="addto-wrap">
                                    <a class="add-cart" href="cart.html">
                                    <i class="zmdi zmdi-shopping-cart-plus icon"></i>
                                    </a>
                                    <a class="add-wishlist" href="wishlist.html">
                                    <i class="zmdi zmdi-favorite-outline zmdi-hc-fw icon"></i>
                                    </a>
                                    <a class="add-quick-view" href="javascript:void(0);">
                                    <i class="zmdi zmdi-search icon"></i>
                                    </a>
                                </div>
                                </div>
                            </div>
                            <div class="product-desc">
                                <div class="product-info">
                                <h4 class="title"><a href="single-product-simple.html">Flower Print dress</a></h4>
                                <div class="star-content">
                                    <i class="fa fa-star-o"></i>
                                    <i class="fa fa-star-o"></i>
                                    <i class="fa fa-star-o"></i>
                                    <i class="fa fa-star-o"></i>
                                    <i class="fa fa-star-o"></i>
                                </div>
                                <div class="prices">
                                    <span class="price">$50.00</span>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <!--== End Shop Item ==-->
                    </div>
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-3 col-sm-6 border">
                        <!--== Start Shop Item ==-->
                        <div class="product-item">
                            <div class="inner-content">
                            <div class="product-thumb">
                                <a href="single-product-simple.html">
                                <img class="w-100" src="@/assets/img/shop/6.jpg" alt="Image-HasTech">
                                </a>
                                <div class="product-action">
                                <div class="addto-wrap">
                                    <a class="add-cart" href="cart.html">
                                    <i class="zmdi zmdi-shopping-cart-plus icon"></i>
                                    </a>
                                    <a class="add-wishlist" href="wishlist.html">
                                    <i class="zmdi zmdi-favorite-outline zmdi-hc-fw icon"></i>
                                    </a>
                                    <a class="add-quick-view" href="javascript:void(0);">
                                    <i class="zmdi zmdi-search icon"></i>
                                    </a>
                                </div>
                                </div>
                            </div>
                            <div class="product-desc">
                                <div class="product-info">
                                <h4 class="title"><a href="single-product-simple.html">Fit Wool Suit</a></h4>
                                <div class="star-content">
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                </div>
                                <div class="prices">
                                    <span class="price">$80.00</span>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <!--== End Shop Item ==-->
                    </div>
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-3 col-sm-6 border">
                        <!--== Start Shop Item ==-->
                        <div class="product-item">
                            <div class="inner-content">
                            <div class="product-thumb">
                                <a href="single-product-simple.html">
                                <img class="w-100" src="@/assets/img/shop/6.jpg" alt="Image-HasTech">
                                </a>
                                <div class="product-action">
                                <div class="addto-wrap">
                                    <a class="add-cart" href="cart.html">
                                    <i class="zmdi zmdi-shopping-cart-plus icon"></i>
                                    </a>
                                    <a class="add-wishlist" href="wishlist.html">
                                    <i class="zmdi zmdi-favorite-outline zmdi-hc-fw icon"></i>
                                    </a>
                                    <a class="add-quick-view" href="javascript:void(0);">
                                    <i class="zmdi zmdi-search icon"></i>
                                    </a>
                                </div>
                                </div>
                            </div>
                            <div class="product-desc">
                                <div class="product-info">
                                <h4 class="title"><a href="single-product-simple.html">Fit Wool Suit</a></h4>
                                <div class="star-content">
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                </div>
                                <div class="prices">
                                    <span class="price">$80.00</span>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <!--== End Shop Item ==-->
                    </div>
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-3 col-sm-6 border">
                        <!--== Start Shop Item ==-->
                        <div class="product-item">
                            <div class="inner-content">
                            <div class="product-thumb">
                                <a href="single-product-simple.html">
                                <img class="w-100" src="@/assets/img/shop/6.jpg" alt="Image-HasTech">
                                </a>
                                <div class="product-action">
                                <div class="addto-wrap">
                                    <a class="add-cart" href="cart.html">
                                    <i class="zmdi zmdi-shopping-cart-plus icon"></i>
                                    </a>
                                    <a class="add-wishlist" href="wishlist.html">
                                    <i class="zmdi zmdi-favorite-outline zmdi-hc-fw icon"></i>
                                    </a>
                                    <a class="add-quick-view" href="javascript:void(0);">
                                    <i class="zmdi zmdi-search icon"></i>
                                    </a>
                                </div>
                                </div>
                            </div>
                            <div class="product-desc">
                                <div class="product-info">
                                <h4 class="title"><a href="single-product-simple.html">Fit Wool Suit</a></h4>
                                <div class="star-content">
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                </div>
                                <div class="prices">
                                    <span class="price">$80.00</span>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <!--== End Shop Item ==-->
                    </div>
                    <div class="col-xxl-2 col-xl-2 col-lg-2 col-md-3 col-sm-6 border">
                        <!--== Start Shop Item ==-->
                        <div class="product-item">
                            <div class="inner-content">
                            <div class="product-thumb">
                                <a href="single-product-simple.html">
                                <img class="w-100" src="@/assets/img/shop/6.jpg" alt="Image-HasTech">
                                </a>
                                <div class="product-action">
                                <div class="addto-wrap">
                                    <a class="add-cart" href="cart.html">
                                    <i class="zmdi zmdi-shopping-cart-plus icon"></i>
                                    </a>
                                    <a class="add-wishlist" href="wishlist.html">
                                    <i class="zmdi zmdi-favorite-outline zmdi-hc-fw icon"></i>
                                    </a>
                                    <a class="add-quick-view" href="javascript:void(0);">
                                    <i class="zmdi zmdi-search icon"></i>
                                    </a>
                                </div>
                                </div>
                            </div>
                            <div class="product-desc">
                                <div class="product-info">
                                <h4 class="title"><a href="single-product-simple.html">Fit Wool Suit</a></h4>
                                <div class="star-content">
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                </div>
                                <div class="prices">
                                    <span class="price">$80.00</span>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        <!--== End Shop Item ==-->
                    </div>
                </div>
            </section>
            <!--== End Product Area Wrapper ==-->

        </main>

        <!--== Start Footer Area Wrapper ==-->
        <footer class="footer-area">
            <div class="footer-top-area">
            <div class="container">
                <div class="row">
                <div class="col-sm-6 col-lg-3">
                    <!--== Start widget Item ==-->
                    <div class="widget-item">
                    <div class="about-widget">
                        <div class="footer-logo-area">
                        <a href="index.html">
                            <img class="logo-main" src="@/assets/img/logo.png" alt="Logo" />
                        </a>
                        </div>
                        <p class="desc">Lorem ipsum dolor sit amet, consectet adipi elit, sed do eius tempor incididun ut labore gthydolore.</p>
                        <ul>
                        <li><i class="ion-ios7-location-outline"></i> 184 Main Rd E, St Albans VIC 3021,</li>
                        <li><i class="ion-ios7-email-outline"></i> <a href="mailto://info@example.com">info@example.com</a></li>
                        </ul>
                    </div>
                    </div>
                    <!--== End widget Item ==-->
                </div>
                <div class="col-sm-6 col-lg-3">
                    <!--== Start widget Item ==-->
                    <div class="widget-item widget-item-one">
                    <h4 class="widget-title">INFORMATION</h4>
                    <div class="widget-menu-wrap">
                        <ul class="nav-menu">
                        <li><a href="shop.html">Specials</a></li>
                        <li><a href="shop.html">New products</a></li>
                        <li><a href="shop.html">Top sellers</a></li>
                        <li><a href="shop.html">Our stores</a></li>
                        <li><a href="contact.html">Contact us</a></li>
                        </ul>
                    </div>
                    </div>
                    <!--== End widget Item ==-->
                </div>
                <div class="col-sm-6 col-lg-3">
                    <!--== Start widget Item ==-->
                    <div class="widget-item widget-item-two">
                    <h4 class="widget-title">QUICK LINKS</h4>
                    <div class="widget-menu-wrap">
                        <ul class="nav-menu">
                        <li><a href="login.html">New User</a></li>
                        <li><a href="about-us.html">Help Center</a></li>
                        <li><a href="about-us.html">Refund Policy</a></li>
                        <li><a href="about-us.html">Report Spam</a></li>
                        <li><a href="login.html">Account</a></li>
                        </ul>
                    </div>
                    </div>
                    <!--== End widget Item ==-->
                </div>
                <div class="col-sm-6 col-lg-3">
                    <!--== Start widget Item ==-->
                    <div class="widget-item">
                    <h4 class="widget-title">newsletter</h4>
                    <div class="widget-newsletter">
                        <p>Sign up for our newsletter & promotions</p>
                        <div class="newsletter-form">
                        <form>
                            <input type="email" class="form-control" placeholder="email@example.com">
                            <button class="btn-submit" type="button">Subscribe</button>
                        </form>
                        </div>
                    </div>
                    </div>
                    <!--== End widget Item ==-->
                </div>
                </div>
            </div>
            
            </div>
            <!--== Start Footer Bottom ==-->
            <div class="footer-bottom">
            <div class="container">
                <div class="row">
                <div class="col-12">
                    <p class="copyright">© 2021, <span>Julie</span>. Made with <i class="fa fa-heart icon-heart"></i> by <a target="_blank" href="https://themeforest.net/user/codecarnival/portfolio"> Codecarnival</a></p>
                </div>
                </div>
            </div>
            </div>
            <!--== End Footer Bottom ==-->
        </footer>
        <!--== End Footer Area Wrapper ==-->

        <!--== Scroll Top Button NOT WORKING==-->
        <div id="scroll-to-top" class="scroll-to-top"><span class="fa fa-angle-double-up"></span></div>

        <!--== Start Quick View Menu ==-->
        <aside class="product-quick-view-modal">
            <div class="product-quick-view-inner">
            <div class="product-quick-view-content">
                <button type="button" class="btn-close">
                <span class="close-icon"><i class="fa fa-close"></i></span>
                </button>
                <div class="row">
                <div class="col-lg-6 col-md-6 col-12">
                    <div class="thumb">
                    <img src="@/assets/img/shop/quick-view1.jpg" alt="Alan-Shop">
                    </div>
                </div>
                <div class="col-lg-6 col-md-6 col-12">
                    <div class="content">
                    <h4 class="title">Meta Slevless Dress</h4>
                    <div class="prices">
                        <del class="price-old">$85.00</del>
                        <span class="price">$70.00</span>
                    </div>
                    <p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia,</p>
                    <div class="quick-view-select">
                        <div class="quick-view-select-item">
                        <label for="forSizes" class="form-label">Size:</label>
                        <select class="form-select" id="forSizes" required>
                            <option selected value="">s</option>
                            <option>m</option>
                            <option>l</option>
                            <option>xl</option>
                        </select>
                        </div>
                        <div class="quick-view-select-item">
                        <label for="forColors" class="form-label">Color:</label>
                        <select class="form-select" id="forColors" required>
                            <option selected value="">red</option>
                            <option>green</option>
                            <option>blue</option>
                            <option>yellow</option>
                            <option>white</option>
                        </select>
                        </div>
                    </div>
                    <div class="action-top">
                        <div class="pro-qty">
                        <input type="text" id="quantity4" title="Quantity" value="1" />
                        </div>
                        <button class="btn btn-black">Add to cart</button>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <div class="canvas-overlay"></div>
        </aside>
        <!--== End Quick View Menu ==-->  

        <!--== Start Side Menu ==-->
        <aside class="off-canvas-wrapper">
            <div class="off-canvas-inner">
            <div class="off-canvas-overlay"></div>
            <!-- Start Off Canvas Content Wrapper -->
            <div class="off-canvas-content">
                <!-- Off Canvas Header -->
                <div class="off-canvas-header">
                <div class="close-action">
                    <button class="btn-menu-close">menu <i class="fa fa-chevron-left"></i></button>
                </div>
                </div>

                <div class="off-canvas-item">
                <!-- Start Mobile Menu Wrapper -->
                <div class="res-mobile-menu menu-active-one">
                    <!-- Note Content Auto Generate By Jquery From Main Menu -->
                </div>
                <!-- End Mobile Menu Wrapper -->
                </div>
            </div>
            <!-- End Off Canvas Content Wrapper -->
            </div>
        </aside>
        <!--== End Side Menu ==-->

    </div>
</template>

<script>
    export default {
        data() {
            return {
                
            }
        }
    }
</script>

<style scoped>

</style>