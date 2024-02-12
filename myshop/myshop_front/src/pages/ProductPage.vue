<template>
    <header-component></header-component>
    <div class="container-lg pt-5" v-if="isProductLoading">
      <div class="row">
      </div>
      <div class="row">
        <div class="col-12 px-3">
          <h2>{{ product.name }}</h2>
        </div>
      </div>
      <div class="row">
        <div class="col-12 px-3">
          <div class="d-flex text-secondary justify-content-start p-1">
            <div class="product-stars">
              <i class="bi bi-star-fill star"></i>
              {{ product.rating }}
            </div>
            <div class="product-stars">
              &#x2022; 3224 оценок
            </div>
          </div>
        </div>
      </div>
      <div class="row mt-5 d-flex">
        <!--Carousel-->
        <div class="col-sm-6 col-lg-4 col-md-6">
          <div id="carouselExampleFade" class="carousel slide carousel-fade">
            <div class="carousel-inner">
              <div class="carousel-item active carousel-item-zoomed" v-if="product.product_images.length > 0" @mousemove="zoom($event)" style="background-image: url('http://127.0.0.1:8000'+product.product_images[0].image);">
                <img :src="product.product_images[0].image" class="d-block w-100" alt="...">
                <!--
                <img v-if="product.product_images.length > 0" :src=product.product_images[0].image alt="...">
                <img v-else src="..." class="card-img-top product-image" alt="...">
                -->
              </div>
              <!--
              <div class="carousel-item carousel-item-zoomed" onmousemove="zoom(event)" style="background-image: url(/media/avatar.webp);">
                <img src="..." class="d-block w-100" alt="...">
              </div>
              <div class="carousel-item carousel-item-zoomed" onmousemove="zoom(event)" style="background-image: url(/media/oboi.webp);">
                <img src="..." class="d-block w-100" alt="...">
              </div>
              -->
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
              <!--
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              -->
              <svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" fill="currentColor" class="bi bi-arrow-left-circle-fill" viewBox="-1 -1 18 18">
                <path class="bold-icon-carousel" fill-rule="evenodd" d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0m3.5 7.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"/>
              </svg>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
              <!--
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              -->
              <svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" fill="currentColor" class="bi bi-arrow-right-circle-fill" viewBox="-1 -1 18 18">
                <path class="bold-icon-carousel" fill-rule="evenodd" d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0M4.5 7.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5z"/>
              </svg>
              <span class="visually-hidden">Next</span>
            </button>
          </div>
        </div>
        <!--End Carousel-->
        <div class="col-sm-6 col-lg-5 col-md-6 pe-4">
          <div class="row my-2" v-if="product.discount > 0">
            <div class="col-12">
              <span class="badge bg-danger">Выгодное предложение</span>
            </div>
          </div>
          <div class="d-flex align-items-end" v-if="product.discount > 0">
              <h1><b>{{ product.discount }} &#8381;</b></h1>
              <h3 class="mx-2 "><s class="text-secondary"><small>{{ product.price }} &#8381;</small></s></h3>
          </div>
          <div class="d-flex align-items-end" v-else>
              <h1><b>{{ product.price }} &#8381;</b></h1>
              <!--<h3 class="mx-2 "><s class="text-secondary"><small>{{ product.price }} &#8381;</small></s></h3>-->
          </div>
          <div class="row my-3">
            <div class="col">
              <div class="row">
                <span>Общие характеристики</span>
              </div>
              <div class="row g-1 my-2">
                <div class="col">
                  <div class="text-secondary">Модель</div>
                </div>
                <div class="col-7">
                  <div class="">Высокая укрывистость</div>
                </div>
              </div>
              <div class="row g-1 my-2">
                <div class="col">
                  <div class="text-secondary">Вес товара</div>
                </div>
                <div class="col-7">
                  <div class="">1,5 кг</div>
                </div>
              </div>
              <div class="row g-1 my-2">
                <div class="col">
                  <div class="text-secondary">Страна производства</div>
                </div>
                <div class="col-7">
                  <div class="">Россия</div>
                </div>
              </div>
            </div>
          </div>
          <div class="row my-3">
            <div class="col-10">
              <div class="d-grid">
                <button type="button" class="btn btn-success" @click="addToCart">Добавить в корзину  <i class="bi bi-cart"></i></button>
              </div>
            </div>
            <div class="col-2">
              <button type="button" class="btn btn-outline-danger"><i class="bi bi-heart"></i></button>
            </div>
          </div>
          <div class="row">
            <div class="col-auto">
              <span class="text-secondary" style="font-size: 0.8em;"><i class="bi bi-box"></i></span>
              <span class="text-secondary" style="font-size: 0.8em;">27 ноября</span>
            </div>
            <div class="col">
              <span class="text-secondary" style="font-size: 0.8em;"><i class="bi bi-shop"></i></span>
              <span class="text-secondary" style="font-size: 0.8em;">Пункт выдачи: ул. Ленина д.1</span>
            </div>
          </div>
        </div>
        <!--Widget-->
        <div class="col-lg-3 border d-none d-lg-block">
          <span>Widget</span>
        </div>
        <!--End Widget-->
      </div>
      <!--Color slider-->
      <!--
      <div class="row">
        <div class="container">
          <div class="px-5">Выбор цвета</div>
          <div id="carouselColorSlider" class="carousel px-5" data-bs-ride="carousel">
            <div class="carousel-inner">
              <div class="carousel-item active p-1" style="min-width: 150px !important; max-width: 150px !important;" id="carouselColorItem">
                <div class="">
                  <a href="#">
                    <img src="..." class="d-block w-100" alt="...">
                  </a>
                  <div class="text-center" style="font-size: 0.7em;">205 Дуб капучино</div>
                </div>
              </div>
              <div class="carousel-item p-1" style="min-width: 150px !important; max-width: 150px !important;">
                <div class="">
                  <img src="..." class="d-block w-100" alt="...">
                </div>
                <div class="text-center" style="font-size: 0.7em;">217 Дуб темный</div>
              </div>
              <div class="carousel-item p-1" style="min-width: 150px !important; max-width: 150px !important;">
                <div class="">
                  <img src="..." class="d-block w-100" alt="...">
                </div>
                <div class="text-center" style="font-size: 0.7em;">253 Ясень серый</div>
              </div>
              <div class="carousel-item p-1" style="min-width: 150px !important; max-width: 150px !important;">
                <div class="">
                  <img src="..." class="d-block w-100" alt="...">
                </div>
                <div class="text-center" style="font-size: 0.7em;">262 Клен вермонт</div>
              </div>
              <div class="carousel-item p-1" style="min-width: 150px !important; max-width: 150px !important;">
                <div class="">
                  <img src="..." class="d-block w-100" alt="...">
                </div>
                <div class="text-center" style="font-size: 0.7em;">302 Венге черный</div>
              </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselColorSlider" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselColorSlider" data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </button>
          </div>
        </div>
      </div>
      -->
      <!--End color slider-->
      <!--About Product-->
      <div class="row mt-5">
        <div class="row">
          <div class="col">
            <h3>О товаре</h3>
          </div>
        </div>
        <div class="col mt-3">
          <span><b>Характеристики</b></span>
          <div class="row mt-3">
            <div class="d-flex justify-content-between">
              <div class="text-secondary">Модель</div>
              <div class="justify-content-start">Краска Текс 1,5л</div>
            </div>
          </div>
          <div class="row mt-3">
            <div class="d-flex justify-content-between">
              <div class="text-secondary">Дополнительная информация</div>
              <div class="ms-3" style="text-align: justify; font-size: 0.9em;">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut faucibus pulvinar elementum integer enim neque volutpat. In iaculis nunc sed augue lacus viverra vitae congue eu. Viverra suspendisse potenti nullam ac tortor vitae purus faucibus. Ac felis donec et odio pellentesque diam. Eget nunc scelerisque viverra mauris in aliquam. Nunc sed augue lacus viverra. Quam elementum pulvinar etiam non quam. Mattis pellentesque id nibh tortor id aliquet lectus. Sem nulla pharetra diam sit amet nisl. Eu scelerisque felis imperdiet proin fermentum leo vel orci porta.
              </div>
            </div>
          </div>
        </div>
        <div class="col mt-3 ms-3">
          <span><b>Описание</b></span>
          <div class="row mt-3" style="text-align: justify; font-size: 0.9em;">
            <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut faucibus pulvinar elementum integer enim neque volutpat. In iaculis nunc sed augue lacus viverra vitae congue eu. Viverra suspendisse potenti nullam ac tortor vitae purus faucibus. Ac felis donec et odio pellentesque diam. Eget nunc scelerisque viverra mauris in aliquam. Nunc sed augue lacus viverra. Quam elementum pulvinar etiam non quam. Mattis pellentesque id nibh tortor id aliquet lectus. Sem nulla pharetra diam sit amet nisl. Eu scelerisque felis imperdiet proin fermentum leo vel orci porta.</div>
          </div>
        </div>
      </div>
      <!--End About Product-->
      <!--Tabs start-->
      <div class="row mt-5">
        <ul class="nav nav-tabs" id="myTab" role="tablist">
          <li class="nav-item" role="presentation">
            <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">Отзывы</button>
          </li>
          <li class="nav-item" role="presentation">
            <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">Вопросы</button>
          </li>
          <li class="nav-item" role="presentation">
            <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact" type="button" role="tab" aria-controls="contact" aria-selected="false">Правила публикации</button>
          </li>
        </ul>
        <div class="tab-content mx-0" id="myTabContent">
          <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
            <div class="mt-3 d-flex gap-2">
                <div class="card mx-0 rounded-3" style="width: 800px;">
                  <div class="card-body">
                      <div class="row">
                        <div class="col-auto">
                          <img src="..." alt="" height="40">
                        </div>
                        <div class="col">
                          <div class="row">Василий</div>
                          <div class="row datetime">11 ноября 2023г. 23:15</div>
                        </div>
                        <div class="col-auto">
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star-no"></i>
                        </div>
                      </div>
                    <p class="card-text mt-3">Краска отличная но не дотягивает до Тикуриллы. За эти деньги вполне отличная краска.</p>
                  </div>
                </div>
                <div class="card mx-0 rounded-3" style="width: 800px;">
                  <div class="card-body">
                      <div class="row">
                        <div class="col-auto">
                          <img src="..." alt="" height="40">
                        </div>
                        <div class="col">
                          <div class="row">Василий</div>
                          <div class="row datetime">11 ноября 2023г. 23:15</div>
                        </div>
                        <div class="col-auto">
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star-no"></i>
                        </div>
                      </div>
                    <p class="card-text mt-3">Краска отличная но не дотягивает до Тикуриллы. За эти деньги вполне отличная краска.</p>
                  </div>
                </div>
                <div class="card mx-0 rounded-3" style="width: 800px;">
                  <div class="card-body">
                      <div class="row">
                        <div class="col-auto">
                          <img src="..." alt="" height="40">
                        </div>
                        <div class="col">
                          <div class="row">Василий</div>
                          <div class="row datetime">11 ноября 2023г. 23:15</div>
                        </div>
                        <div class="col-auto">
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star"></i>
                            <i class="bi bi-star-fill star-no"></i>
                        </div>
                      </div>
                    <p class="card-text mt-3">Краска отличная но не дотягивает до Тикуриллы. За эти деньги вполне отличная краска.</p>
                  </div>
                </div>
            </div>
          </div>
          <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
            <div class="col-12 mt-3">
              <form action="">
                <textarea class="form-control" id="question" rows=3 placeholder="Задайте вопрос"></textarea>
                <div class="d-flex gap-2">
                    <button type="submit" class="btn btn-success mt-2">Задать вопрос</button>
                    <button type="submit" class="btn btn-light mt-2">Отменить</button>
                </div>
              </form>
            </div>
            <div class="mt-3 d-flex gap-2">
              <div class="card mx-0 rounded-3" style="width: 300px;">
                <div class="card-body">
                    <div class="row">
                      <div class="col-auto">
                        <img src="..." alt="" height="40">
                      </div>
                      <div class="col">
                        <div class="row">Василий</div>
                        <div class="row datetime">11 ноября 2023г. 23:15</div>
                      </div>
                    </div>
                  <p class="card-text mt-3">В наличии есть 20 штук?</p>
                  <div class="card-text">
                    <i class="bi bi-hourglass"></i> Ждем ответ продавца
                  </div>
                </div>
              </div>
              <div class="card mx-0 rounded-3" style="width: 300px;">
                <div class="card-body">
                    <div class="row">
                      <div class="col-auto">
                        <img src="..." alt="" height="40">
                      </div>
                      <div class="col">
                        <div class="row">Валя</div>
                        <div class="row datetime">10 ноября 2023г. 10:45</div>
                      </div>
                    </div>
                  <p class="card-text mt-3">Подойдет для потолка?</p>
                  <div class="card-text">
                    <b><i class="bi bi-check"></i> Ответ продавца</b>
                  </div>
                  <div class="card-text">
                    Да. Данная краска подходит для покраски потолков.
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="tab-pane fade mt-3" id="contact" aria-labelledby="contact-tab">
            <h4>Правила оформления отзывов и вопросов</h4>
            <p class="text-black-50">В отзывах и вопросах должна содержаться информация только о товаре.</p>

            <p class="text-black-50">Отзывы можно оставить только на заказанный и полученный покупателем товар.
            К одному товару покупатель может оставить не более одного отзыва.
            К отзывам можно прикрепить до 5 фотографий. Товар на фото должен быть хорошо виден.</p>

            <p>К публикации не допускаются следующие отзывы и вопросы:</p>
            <ul>
              <li>Указывающие на покупку данного товара в других магазинах</li>
              <li>Содержащие любые контактные данные (номера телефонов, адреса, email, ссылки на сторонние сайты)</li>
              <li>С ненормативной лексикой, оскорбляющие достоинство других покупателей или магазина</li>
              <li>С обилием символов в верхнем регистре (заглавных букв)</li>
            </ul>
            <p class="text-black-50">Вопросы публикуются лишь после того, как на них получен ответ.</p>

            <p class="text-black-50">Мы оставляем за собой право редактировать или не публиковать отзыв и вопрос, который не соответствует установленным правилам!</p>
          </div>
        </div>
      </div>
      <!--Tabs end-->
      <div class="row mt-5">
        <div class="col">
          <span>Recomendation</span>
        </div>
      </div>
    </div>
    <div v-else class="d-flex justify-content-center align-items-center" style="min-height: 100vh;">
      <div class="spinner-grow" style="width: 5rem; height: 5rem;" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    <footer-component></footer-component>
</template>

<script>
    import axios from 'axios'
    import HeaderComponent from '@/components/HeaderComponent.vue'
    import FooterComponent from '@/components/FooterComponent.vue'
    export default {
        components: {HeaderComponent, FooterComponent},
        data() {
            return {
                isProductLoading: false,
                product: {
                  available: true,
                  catalog: 0,
                  code_1c: 0,
                  create_date: "",
                  description: "Нет описания",
                  discount: "0.00",
                  id: 0,
                  name: "",
                  price: "0.00",
                  product_images: [],
                  quantity: "1.000",
                  rating: "0.0",
                  show_count: 0,
                  slug: "",
                  tags: []
                }
            }
        },
        methods: {
            async uploadProduct() {
                try {
                    axios(
                      {
                        method: 'post',
                        url: 'http://127.0.0.1:8000/api/token/',
                        headers: {'Content-Type': 'application/json;charset=utf-8'},
                        data: JSON.stringify({'phone_number': this.$store.state.userPhone, 'password': this.$store.state.userPassword})
                      }
                    ).then((response) => {
                      const token = response.data.access;
                      axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/products/${this.$route.params.id}/`,
                          method: 'get',
                          headers: {'Authorization': `Bearer ${token}`}
                        }
                      ).then((response) => {
                        this.product = response.data;
                        this.isProductLoading=true
                      })
                    });
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },

            zoom(event) {
                // console.log(event);
                const zoomer = event.currentTarget;
                let img = zoomer.querySelector("img");
                zoomer.setAttribute('style', `background-image: url(${img.src})`);
                // event.offsetX ? offsetX = event.offsetX : offsetX = event.touches[0].pageX
                // event.offsetY ? offsetY = event.offsetY : offsetX = event.touches[0].pageX
                const x = event.offsetX/zoomer.offsetWidth*100
                const y = event.offsetY/zoomer.offsetHeight*100
                zoomer.style.backgroundPosition = x + '% ' + y + '%';
            },

            addToCart() {
              this.$store.commit('addProductToCart', this.product);
            }
        },
        mounted() {
            this.routeParamId = this.$route.params.id;
            this.uploadProduct();
        }
    }
</script>

<style scoped>

</style>