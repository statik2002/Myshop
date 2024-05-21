<template>
    <div class="wrapper">
        <header-component></header-component>
        <!--== Start Preloader Content ==-->
        <div class="preloader-wrap" v-if="!isProductLoading">
            <div class="preloader">
                <span class="dot"></span>
                <div class="dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
                
            </div>
        </div>
        <!--== End Preloader Content ==-->
        <main class="main-content pb-5">
            <!--== Start Page Header Area Wrapper ==-->
            <div class="page-header-area">
                <div class="container">
                    <div class="row">
                    <div class="col-12 text-center">
                        <div class="page-header-content">
                        <nav class="breadcrumb-area">
                            <ul class="breadcrumb">
                                <li><router-link to="/">Главная</router-link></li>
                                <li class="breadcrumb-sep">/</li>
                                <li>{{ product.name }}</li>
                            </ul>
                        </nav>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
            <!--== End Page Header Area Wrapper ==-->

            <!--== Start Product Single Area Wrapper ==-->
            <section class="product-area product-single-area" v-if="isProductLoading">
                <div class="container pt-60 pb-0">
                    <div class="row">
                        <div class="col-12">
                            <div class="product-single-item" data-margin-bottom="63">
                                <div class="row">
                                    <div class="col-lg-6">
                                        <!--== Start Product Thumbnail Area ==-->
                                        <div class="product-thumb">
                                            <div id="carouselProductIndicators" class="carousel slide carousel-fade" data-bs-ride="carousel">
                                                <div class="carousel-inner" v-if="product.product_images.length > 0">
                                                    <div v-for="(image, index) in product.product_images">
                                                        <div v-if="index === 0" class="carousel-item active">
                                                            <img :src=image.image class="d-block w-100" :alt=image.alt>
                                                        </div>
                                                        <div v-else class="carousel-item">
                                                            <img :src=image.image class="d-block w-100" :alt=image.alt>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="carousel-inner" v-else>
                                                    <div class="carousel-item active">
                                                        <img src="@/assets/no_image.png" class="d-block w-100" alt="No image">
                                                    </div>
                                                </div>
                                                <button class="carousel-control-prev" type="button" data-bs-target="#carouselProductIndicators" data-bs-slide="prev">
                                                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                                    <span class="visually-hidden">Previous</span>
                                                </button>
                                                <button class="carousel-control-next" type="button" data-bs-target="#carouselProductIndicators" data-bs-slide="next">
                                                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                                    <span class="visually-hidden">Next</span>
                                                </button>
                                            </div>
                                        </div>
                                        <!--== End Product Thumbnail Area ==-->

                                        <!--== Start Product Nav Area ==-->
                                        <!--
                                        <div class="swiper-container single-product-nav-slider product-nav">
                                            <div class="swiper-wrapper">
                                            <div class="swiper-slide">
                                                <img src="@/assets/img/shop/product-single/nav1.jpg" alt="Image-HasTech">
                                            </div>
                                            <div class="swiper-slide">
                                                <img src="@/assets/img/shop/product-single/nav2.jpg" alt="Image-HasTech">
                                            </div>
                                            <div class="swiper-slide">
                                                <img src="@/assets/img/shop/product-single/nav3.jpg" alt="Image-HasTech">
                                            </div>
                                            <div class="swiper-slide">
                                                <img src="@/assets/img/shop/product-single/nav4.jpg" alt="Image-HasTech">
                                            </div>
                                            <div class="swiper-slide">
                                                <img src="@/assets/img/shop/product-single/nav5.jpg" alt="Image-HasTech">
                                            </div>
                                            </div>

                                            <div class="swiper-button-prev"><i class="ei ei-icon_arrow_carrot-left"></i></div>
                                            <div class="swiper-button-next"><i class="ei ei-icon_arrow_carrot-right"></i></div>
                                        </div>
                                        -->
                                        <!--== End Product Nav Area ==-->
                                    </div>
                                    <div class="col-lg-6">
                                        <!--== Start Product Info Area ==-->
                                        <div class="product-single-info">
                                            <h4 class="title">{{ product.name }}</h4>
                                            <div class="prices">
                                                <div v-if="product.discount > 0">
                                                    <span class="price">{{ product.online_price - product.online_price * product.discount/100 }} &#8381;</span>
                                                    <span v-if="product.discount > 0" class="price-old">{{ product.online_price }} &#8381;</span>
                                                </div>
                                                <div v-else>
                                                    <span class="price">{{ product.online_price }} &#8381;</span>
                                                </div>
                                            </div>
                                            <div class="rating-box-wrap">
                                                <rating-component :rating="product.rating" :num_rating="product.num_ratings"></rating-component>
                                                <div class="review-status">
                                                    <a href="#">( 1 Отзыв )</a>
                                                </div>
                                            </div>
                                            <p v-html="product.description"></p>
                                            <!--
                                            <div class="product-select-action">
                                                <div class="select-item">
                                                    <label for="productSizeSelect">Size</label>
                                                    <select class="form-select" id="productSizeSelect" aria-label="Size select example">
                                                    <option selected>s</option>
                                                    <option value="m">m</option>
                                                    <option value="l">l</option>
                                                    <option value="xl">xl</option>
                                                    </select>
                                                </div>
                                                <div class="select-item">
                                                    <label for="productColorSelect">Color</label>
                                                    <select class="form-select" id="productColorSelect" aria-label="Color select example">
                                                    <option selected>purple</option>
                                                    <option value="violet">violet</option>
                                                    <option value="black">black</option>
                                                    <option value="pink">pink</option>
                                                    <option value="orange">orange</option>
                                                    </select>
                                                </div>
                                                <div class="select-item">
                                                    <label for="productMaterialSelect">Material</label>
                                                    <select class="form-select" id="productMaterialSelect" aria-label="Material select example">
                                                    <option selected>metal</option>
                                                    <option value="resin">resin</option>
                                                    <option value="leather">leather</option>
                                                    <option value="slag">slag</option>
                                                    <option value="fiber">fiber</option>
                                                    </select>
                                                </div>
                                            </div>
                                            -->
                                            <div class="product-action-simple">
                                                <div class="product-quick-action" v-if="product.quantity==1">
                                                    <span class="product-badge">Остался всего 1</span>
                                                </div>
                                                <div class="product-quick-action">
                                                    <div class="product-quick-qty">
                                                        <div class="pro-qty">
                                                            <div class="inc qty-btn" @click="addOne">+</div>
                                                            <input type="text" id="quantity" title="Количество" v-model="productQuantity" @input="inputQuantity">
                                                            <div class= "dec qty-btn" @click="subOne">-</div>
                                                        </div>
                                                    </div>
                                                    <div class="pe-3" v-if="product.unit">{{ product.unit.short_name }}</div>
                                                    <button class="btn-product-add border-0" @click="addToCart(product)">В корзину</button>
                                                </div>
                                                
                                                <div class="product-wishlist">
                                                    <div v-if="!likedProducts.includes(product.id)">
                                                        <a href="#" class="btn-wishlist" @click="like">В избранное</a>
                                                    </div>
                                                    <div v-else>
                                                        <a href="#" class="btn-wishlist" @click="dislike">Из избранного</a>
                                                    </div>
                                                </div>
                                                <div class="payment-button" v-if="$store.getters.isUserLogin">
                                                    <button class="btn-payment border-0" @click="confirmOrderModal=true">Купить сейчас</button>
                                                </div>
                                                <div class="social-sharing">
                                                    <span>Поделиться:</span>
                                                    <div class="social-icons">
                                                        <a href="#/"><i class="bi bi-telegram"></i></a>
                                                        <a href="#/"><i class="bi bi-whatsapp"></i></a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <!--== End Product Info Area ==-->
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row pt-5" v-if="product.linked_products.length > 0">
                        <h5 class="title">С этим товаром покупают</h5>
                        <linked-products :products="product.linked_products"></linked-products>
                    </div>
                    <div class="row pt-5">
                        <div class="col-12">
                            <div class="product-review-tabs-content">
                            <ul class="nav product-tab-nav" id="ReviewTab" role="tablist">
                                <li role="presentation">
                                    <a class="active" id="description-tab" data-bs-toggle="pill" href="#description" role="tab" aria-controls="description" aria-selected="true">Характеристики</a>
                                </li>
                                <li role="presentation">
                                    <a id="reviews-tab" data-bs-toggle="pill" href="#reviews" role="tab" aria-controls="reviews" aria-selected="false">Отзывы</a>
                                </li>
                                <li role="presentation">
                                    <a id="shipping-policy-tab" data-bs-toggle="pill" href="#shipping-policy" role="tab" aria-controls="shipping-policy" aria-selected="false">Условия продажи</a>
                                </li>
                                <!--
                                <li role="presentation">
                                    <a id="size-chart-tab" data-bs-toggle="pill" href="#size-chart" role="tab" aria-controls="size-chart" aria-selected="false">Размеры</a>
                                </li>
                                -->
                            </ul>
                            <div class="tab-content product-tab-content" id="ReviewTabContent">
                                <div class="tab-pane fade show active" id="description" role="tabpanel" aria-labelledby="description-tab">
                                <div class="row">
                                    <div class="col-xl-6 col-md-12">
                                        <table class="table table-striped table-hover">
                                            <thead class="table-dark">
                                                <tr>
                                                    <th scope="col">Тип</th>
                                                    <th scope="col">Свойство</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <template v-for="(value, index) in properties">
                                                    <tr v-if="value">
                                                        <td>{{ index }}</td>
                                                        <td v-if="!isNaN(parseFloat(value))">{{ parseFloat(value) }}</td>
                                                        <td v-else>{{ value }}</td>
                                                    </tr>
                                                </template>
                                            </tbody>
                                        </table>
                                    </div>
                                    <div class="col-xl-6 col-md-12">
                                        <table class="table">
                                            <thead class="table-dark">
                                                <tr>
                                                    <th scope="col">Описание</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                    <td v-html="product.description">
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                                </div>
                                <div class="tab-pane fade" id="reviews" role="tabpanel" aria-labelledby="reviews-tab">
                                    <!--
                                    <div class="product-review-content">
                                        <div class="review-content-header">
                                        <h3>Отзыв</h3>
                                        <div class="review-info">
                                            <ul class="review-rating">
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star-o"></li>
                                            </ul>
                                            <span class="review-caption">Based on 7 reviews</span>
                                            <span class="review-write-btn show">Write a review</span>
                                        </div>
                                        </div>


                                        <div class="reviews-form-area show">
                                        <h4 class="title">Write a review</h4>
                                        <div class="reviews-form-content">
                                            <form action="#">
                                            <div class="row">
                                                <div class="col-md-12">
                                                <div class="form-group">
                                                    <label for="for_name">Name</label>
                                                    <input id="for_name" class="form-control" type="text" placeholder="Enter your name">
                                                </div>
                                                </div>
                                                <div class="col-md-12">
                                                <div class="form-group">
                                                    <label for="for_email">Email</label>
                                                    <input id="for_email" class="form-control" type="email" placeholder="john.smith@example.com">
                                                </div>
                                                </div>
                                                <div class="col-md-12">
                                                <div class="form-group">
                                                    <span class="title">Rating</span>
                                                    <ul class="review-rating">
                                                    <li class="fa fa-star-o"></li>
                                                    <li class="fa fa-star-o"></li>
                                                    <li class="fa fa-star-o"></li>
                                                    <li class="fa fa-star-o"></li>
                                                    <li class="fa fa-star-o"></li>
                                                    </ul>
                                                </div>
                                                </div>
                                                <div class="col-md-12">
                                                <div class="form-group">
                                                    <label for="for_review-title">Review Title</label>
                                                    <input id="for_review-title" class="form-control" type="text" placeholder="Give your review a title">
                                                </div>
                                                </div>
                                                <div class="col-md-12">
                                                <div class="form-group">
                                                    <label for="for_comment">Body of Review (1500)</label>
                                                    <textarea id="for_comment" class="form-control" placeholder="Write your comments here"></textarea>
                                                </div>
                                                </div>
                                                <div class="col-md-12">
                                                <div class="form-submit-btn">
                                                    <button type="submit" class="btn-submit">Post comment</button>
                                                </div>
                                                </div>
                                            </div>
                                            </form>
                                        </div>
                                        </div>


                                        <div class="reviews-content-body">

                                        <div class="review-item">
                                            <ul class="review-rating">
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            </ul>
                                            <h3 class="title">Awesome shipping service!</h3>
                                            <h5 class="sub-title"><span>Nantu Nayal</span> no <span>Sep 30, 2018</span></h5>
                                            <p>It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
                                            <a href="#/">Report as Inappropriate</a>
                                        </div>

                                        <div class="review-item">
                                            <ul class="review-rating">
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star-o"></li>
                                            <li class="fa fa-star-o"></li>
                                            <li class="fa fa-star-o"></li>
                                            <li class="fa fa-star-o"></li>
                                            </ul>
                                            <h3 class="title">Low Quality</h3>
                                            <h5 class="sub-title"><span>Oliv hala</span> no <span>Sep 30, 2018</span></h5>
                                            <p>My Favorite White Sneakers From Splurge To Save the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.</p>
                                            <a href="#/">Report as Inappropriate</a>
                                        </div>

                                        <div class="review-item">
                                            <ul class="review-rating">
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            </ul>
                                            <h3 class="title">Excellent services!</h3>
                                            <h5 class="sub-title"><span>Halk Marron</span> no <span>Sep 30, 2018</span></h5>
                                            <p>The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.</p>
                                            <a href="#/">Report as Inappropriate</a>
                                        </div>

                                        <div class="review-item">
                                            <ul class="review-rating">
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star-o"></li>
                                            <li class="fa fa-star-o"></li>
                                            </ul>
                                            <h3 class="title">Price is very high</h3>
                                            <h5 class="sub-title"><span>Musa</span> no <span>Sep 30, 2018</span></h5>
                                            <p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.</p>
                                            <a href="#/">Report as Inappropriate</a>
                                        </div>

                                        <div class="review-item">
                                            <ul class="review-rating">
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star"></li>
                                            <li class="fa fa-star-o"></li>
                                            </ul>
                                            <h3 class="title">Normal</h3>
                                            <h5 class="sub-title"><span>Muhammad</span> no <span>Sep 30, 2018</span></h5>
                                            <p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour</p>
                                            <a href="#/">Report as Inappropriate</a>
                                        </div>

                                        </div>


                                        <div class="review-pagination">
                                        <span class="pagination-pag">1</span>
                                        <span class="pagination-pag">2</span>
                                        <span class="pagination-next">Next »</span>
                                        </div>

                                    </div>
                                    -->
                                </div>
                                <div class="tab-pane fade" id="shipping-policy" role="tabpanel" aria-labelledby="shipping-policy-tab">
                                    <div class="product-shipping-policy">
                                        <div class="section-title">
                                        <h2 class="title">Условия продажи товара</h2>
                                        <p>При заказе и покупке товаров в нашем интернет магазине просим обратить внимание на следующее:</p>
                                        </div>
                                        <ul class="shipping-policy-list">
                                            <li>Цены товаров на сайте только при заказе и покупке онлайн. Цены непосредственно в магазине, могут быть значительно больше.</li>
                                            <li>Акции и распродажи на сайте, относятся только к товарам заказываемым или покупаемым на сайте.</li>
                                            <li>На данный момент товар можно заказать и получить в пункте выдачи.</li>
                                            <li>Оплата товара производиться в пункте выдачи при получении заказа.</li>
                                            <li>Если товар не подошел, то его можно вернуть в течении 14 дней. Товар необходимо вернуть в пункт выдачи.</li>
                                            <li>При возврате товара необходимо написать заявление на возврат товара. </li>
                                        </ul>
                                    </div>
                                </div>
                                <!--
                                <div class="tab-pane fade" id="size-chart" role="tabpanel" aria-labelledby="size-chart-tab">
                                    <div class="product-size-chart">
                                        <h4>Size Chart</h4>
                                        <table class="table">
                                        <tbody>
                                            <tr>
                                            <td class="cun-name"><span>UK</span></td>
                                            <td>18</td>
                                            <td>20</td>
                                            <td>22</td>
                                            <td>24</td>
                                            <td>26</td>
                                            </tr>
                                            <tr>
                                            <td class="cun-name"><span>European</span></td>
                                            <td>46</td>
                                            <td>48</td>
                                            <td>50</td>
                                            <td>52</td>
                                            <td>54</td>
                                            </tr>
                                            <tr>
                                            <td class="cun-name"><span>usa</span></td>
                                            <td>14</td>
                                            <td>16</td>
                                            <td>18</td>
                                            <td>20</td>
                                            <td>22</td>
                                            </tr>
                                            <tr>
                                            <td class="cun-name"><span>Australia</span></td>
                                            <td>28</td>
                                            <td>10</td>
                                            <td>12</td>
                                            <td>14</td>
                                            <td>16</td>
                                            </tr>
                                            <tr>
                                            <td class="cun-name"><span>Canada</span></td>
                                            <td>24</td>
                                            <td>18</td>
                                            <td>14</td>
                                            <td>42</td>
                                            <td>36</td>
                                            </tr>
                                        </tbody>
                                        </table>
                                    </div>
                                </div>
                                -->
                            </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!--== End Product Single Area Wrapper ==-->

            <!--== Start Product Area Wrapper ==-->
            <!--
            <section class="product-area product-new-arrivals-area product-related-area">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-7 m-auto">
                            <div class="section-title text-center"  >
                            <h2 class="title">С этим товаром покупают</h2>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <swiper
                                :slidesPerView="4"
                                :spaceBetween="30"
                                :navigation="true"
                                class="mySwiper"
                                
                            >
                                <swiper-slide>
                                    <div class="card bg-dark text-white">
                                        <img src="@/assets/img/shop/1.jpg" class="card-img" alt="...">
                                        <div class="card-img-overlay">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                            <p class="card-text">Last updated 3 mins ago</p>
                                        </div>
                                    </div>
                                </swiper-slide>
                                <swiper-slide>
                                    <div class="card bg-dark text-white">
                                        <img src="@/assets/img/shop/1.jpg" class="card-img" alt="...">
                                        <div class="card-img-overlay">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                            <p class="card-text">Last updated 3 mins ago</p>
                                        </div>
                                    </div>
                                </swiper-slide>
                                <swiper-slide>
                                    <div class="card bg-dark text-white">
                                        <img src="@/assets/img/shop/1.jpg" class="card-img" alt="...">
                                        <div class="card-img-overlay">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                            <p class="card-text">Last updated 3 mins ago</p>
                                        </div>
                                    </div>
                                </swiper-slide>
                                <swiper-slide>
                                    <div class="card bg-dark text-white">
                                        <img src="@/assets/img/shop/1.jpg" class="card-img" alt="...">
                                        <div class="card-img-overlay">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                            <p class="card-text">Last updated 3 mins ago</p>
                                        </div>
                                    </div>
                                </swiper-slide>
                                <swiper-slide>
                                    <div class="card bg-dark text-white">
                                        <img src="@/assets/img/shop/1.jpg" class="card-img" alt="...">
                                        <div class="card-img-overlay">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                            <p class="card-text">Last updated 3 mins ago</p>
                                        </div>
                                    </div>
                                </swiper-slide>
                                <swiper-slide>
                                    <div class="card bg-dark text-white">
                                        <img src="@/assets/img/shop/1.jpg" class="card-img" alt="...">
                                        <div class="card-img-overlay">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                            <p class="card-text">Last updated 3 mins ago</p>
                                        </div>
                                    </div>
                                </swiper-slide>
                                <swiper-slide>
                                    <div class="card bg-dark text-white">
                                        <img src="@/assets/img/shop/1.jpg" class="card-img" alt="...">
                                        <div class="card-img-overlay">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                            <p class="card-text">Last updated 3 mins ago</p>
                                        </div>
                                    </div>
                                </swiper-slide>
                                <swiper-slide>
                                    <div class="card bg-dark text-white">
                                        <img src="@/assets/img/shop/1.jpg" class="card-img" alt="...">
                                        <div class="card-img-overlay">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                            <p class="card-text">Last updated 3 mins ago</p>
                                        </div>
                                    </div>
                                </swiper-slide>
                            </swiper>
                        </div>
                    </div>
                </div>
            </section>
            -->
            <!--== End Product Area Wrapper ==-->

            <modal-component v-model:show="addToCartModalIsVisible">
                <div class="d-flex flex-column gap-3">
                    <div class="align-self-center">{{ product.name }} уже в корзине</div>
                    <div class="d-flex justify-content-between gap-4 account-optional-group">
                        <button class="btn-theme" @click="$router.push('/cart2')">Посмотреть корзину</button>
                        <button class="btn-theme" @click="addToCartModalIsVisible=false">Продолжить покупки</button>
                    </div>
                </div>
            </modal-component>

            <modal-component v-model:show="buyNowModal">
                <div class="d-flex flex-column gap-3">
                    <h4 class="align-self-center">Ваш заказ отправлен.</h4> 
                    <p class="align-self-center">Статус заказа и подробности можно посмотреть в личном кабинете.</p>
                    <button class="btn-theme align-self-center" @click="buyNowModal=false">Ок</button>
                </div>
            </modal-component>

            <modal-component v-model:show="confirmOrderModal">
                <div class="d-flex flex-column gap-3">
                    <h4 class="align-self-center">Заказ на {{ product.name }}</h4>
                    <p class="align-self-center">
                        В количестве {{ productQuantity }} на сумму {{ ((product.online_price - product.online_price * product.discount/100) * productQuantity).toFixed(2) }} &#8381;
                    </p>
                    <p class="align-self-center">Вы подтверждаете заказ?</p>
                    <button class="btn-theme align-self-center" @click="{confirmOrderModal=false; sendOrder()}">Подтверждаю</button>
                </div>
            </modal-component>

            <!--== Scroll Top Button==-->
            <scroll-to-top></scroll-to-top>
        </main>
        <footer-component></footer-component>
    </div>
</template>

<script>
    import axios from 'axios'
    import { Swiper, SwiperSlide } from 'swiper/vue';
    import { Navigation } from 'swiper/modules';
    import 'swiper/css';
    import 'swiper/css/navigation';

    export default {
        components: {Swiper, SwiperSlide},
        data() {
            return {
                isProductLoading: false,
                product: {},
                productQuantity: 1,
                addToCartModalIsVisible: false,
                confirmOrderModal: false,
                buyNowModal: false,
                modules: [Navigation],
                likedProducts: [],
                properties: {}
            }
        },
        methods: {
            async uploadProduct() {
                try {
                      axios(
                        {
                          url: `${this.$store.state.apiUrl}/api/v1/products/${this.$route.params.id}/`,
                          method: 'get'
                        }
                      ).then((response) => {
                        if(response.data.his_rating.length != null)
                        {
                          response.data.his_rating.push({'value': 0.0, 'counter': 0})
                        }
                        this.product = response.data;
                        this.isProductLoading=true
                        for(const key in this.product.properties[0]) {
                            if(!['id', 'property_labels', 'description', 'product'].includes(key)) {
                                this.properties[this.product.properties[0].property_labels[key]]=this.product.properties[0][key]
                            }
                        }
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },
            addOne() {
                if(this.productQuantity + 1 <= this.product.quantity) {
                    this.productQuantity += 1
                }
                
            },
            subOne() {
                this.productQuantity > 1 ? this.productQuantity -=1 : 1
            },
            inputQuantity(event){
                if(event.target.value < 1){
                    event.target.value = 1
                    this.productQuantity = 1
                } else if(event.target.value >= Number(this.product.quantity)) {
                    event.target.value = Number(this.product.quantity)
                    this.productQuantity = Number(this.product.quantity)
                }
            },
            addToCart(product) {
                this.$store.commit('addProductToCart', {'product': product, 'quantity': this.productQuantity});
                this.addToCartModalIsVisible = true
            },
            like() {
                // Implement send to backend like product
                const like = {
                    'product_id': this.product.id,
                    'operation': 'like'
                }
                if (!this.$store.getters.isUserLogin){
                    if (!this.$store.state.unregisteredUser.likes.includes(this.product.id)) {
                                this.$store.commit('like', this.product.id)
                        }
                    return
                }
                try {
                        axios(
                        {
                            url: `${this.$store.state.apiUrl}/api/v1/like/`,
                            method: 'post',
                            headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                            data: like
                        }
                        ).then((response) => {
                            //console.log(response)
                            if (!this.$store.state.user.likes.includes(this.product.id)) {
                                this.$store.commit('like', this.product.id)
                            }
                            
                        })
                    } catch(e) {
                        alert(`Connection error: ${e}`);
                    }
                    finally {
            
                    }
            },
            dislike() {
              // Implement send to backend like product
              const like = {
                'user_id': this.$store.state.user.id,
                'product_id': this.product.id,
                'operation': 'dislike'
              }
              if (!this.$store.getters.isUserLogin){
                    if (this.$store.state.unregisteredUser.likes.includes(this.product.id)) {
                                this.$store.commit('dislike', this.product.id)
                        }
                    return
                }
              try {
                    axios(
                      {
                        url: `${this.$store.state.apiUrl}/api/v1/like/`,
                        method: 'post',
                        headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                        data: like
                      }
                    ).then((response) => {
                          //console.log(response)
                          this.$store.commit('dislike', this.product.id)
                      })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },
            async sendOrder() {
                //console.log(this.$store.state.user.access)
                let order_products = []

                order_products.push({
                    'product': this.product.id,
                    'quantity': this.productQuantity,
                    'fixed_price': (this.product.online_price - this.product.online_price * this.product.discount/100).toFixed(2),
                })
                //console.log(JSON.stringify(order_products))
                const order = {
                    'order_products': order_products
                }
                //console.log(JSON.stringify(order))

                try {
                      axios(
                        {
                          url: `${this.$store.state.apiUrl}/api/v1/order/`,
                          method: 'post',
                          headers: {'Authorization': `Bearer ${this.$store.state.user.access}`},
                          data: order
                        }
                      ).then((response) => {
                            //console.log(response)
                            //this.$store.commit('clearCart')
                            this.products = []
                            //this.$store.commit('deleteProductsFromCart', order_products)
                            //this.$router.go()
                            this.buyNowModal = true
                        })
                } catch(e) {
                    console.log(`Connection error: ${e}`);
                }
                finally {
        
                }
            },
        },
        mounted() {
            this.uploadProduct();
            this.likedProducts = this.$store.getters.getLikedProducts
        },
        watch: {
            $route(to, from) {
                this.$router.go(0)
            }
        }
    }
</script>

<style scoped>

</style>