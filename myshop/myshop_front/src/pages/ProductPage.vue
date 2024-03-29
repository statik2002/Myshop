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
            <rating-component :rating="product.rating"></rating-component>
            <div class="ps-1 fw-lighter fst-italic">
              &#x2022; {{ product.num_ratings }} оценок
            </div>
          </div>
        </div>
      </div>
      <div class="row mt-2 d-flex">
        <!--Carousel-->
        <div class="col-sm-6 col-lg-4 col-md-6">
          <div id="carouselFade" class="carousel slide carousel-fade" data-bs-ride="carousel">
            <div class="carousel-inner">
              <div v-for="(image, index) in product.product_images" v-if="product.product_images.length > 0" >
                <div class="carousel-item active carousel-item-zoomed" v-if="index === 0" @mousemove="zoom($event)" style="background-image: url(image.image);">
                  <img :src="image.image" class="d-block w-100" :alt="image.alt">
                </div>
                <div class="carousel-item carousel-item-zoomed" v-else @mousemove="zoom($event)" style="background-image: url(image.image);">
                  <img :src="image.image" class="d-block w-100" :alt="image.alt">
                </div>
              </div>
              <div v-else>
                <div class="carousel-item active carousel-item-zoomed" @mousemove="zoom($event)" style="background-image: url(@/assets/no_image.png);">
                  <img src="@/assets/no_image.png" class="d-block w-100" alt="No image">
                </div>
              </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselFade" data-bs-slide="prev">
              <svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" fill="currentColor" class="bi bi-arrow-left-circle-fill" viewBox="-1 -1 18 18">
                <path class="bold-icon-carousel" fill-rule="evenodd" d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0m3.5 7.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5z"/>
              </svg>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselFade" data-bs-slide="next">
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
              <span class="badge bg-danger">Выгодное предложение {{ humanViewNumber(product.discount) }}% скидка</span>
            </div>
          </div>
          <div class="d-flex align-items-end" v-if="product.discount > 0">
              <h1><b>{{ product.price - product.price * product.discount/100 }} &#8381;</b></h1>
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
                  <div class="text-secondary">Артикул: </div>
                </div>
                <div class="col-7">
                  <div class="">{{ product.id }}</div>
                </div>
              </div>
              <div v-if="product.properties.length > 0">
                <div class="row g-1 my-2" v-if="product.properties[0].hasOwnProperty('production_origin')">
                  <div class="col">
                    <div class="text-secondary">Страна производства</div>
                  </div>
                  <div class="col-7">
                    <div class="">{{ product.properties[0].production_origin }}</div>
                  </div>
                </div>
                <div class="row g-1 my-2" v-if="product.properties[0].hasOwnProperty('weight')">
                  <div class="col">
                    <div class="text-secondary">Вес товара</div>
                  </div>
                  <div class="col-7">
                    <div class="">{{ humanViewNumber(product.properties[0].weight) }} кг</div>
                  </div>
                </div>
                <div class="row g-1 my-2" v-if="product.properties[0].hasOwnProperty('material')">
                  <div class="col">
                    <div class="text-secondary">Состав/материал</div>
                  </div>
                  <div class="col-7">
                    <div class="">{{ product.properties[0].material }}</div>
                  </div>
                </div>
                <div class="row g-1 my-2" v-if="product.properties[0].hasOwnProperty('expiration_date')">
                  <div class="col">
                    <div class="text-secondary">Срок годности</div>
                  </div>
                  <div class="col-7">
                    <div class="">{{ product.properties[0].expiration_date }} месяцев</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row my-3" v-if="$store.state.userIsAuth">
            <div v-if="$store.state.user.is_staff" class="col-12">
              <button type="button" class="btn btn-success" @click="editProduct">Редактировать<i class="bi bi-pencil-square"></i></button>
              <button type="button" class="btn btn-success" @click="uploadImages">Изображения<i class="bi bi-pencil-square"></i></button>
            </div>
            <div v-else class="d-flex gap-2">
                <button type="button" class="btn btn-success" @click="addToCart">Добавить в корзину  <i class="bi bi-cart"></i></button>
                <div v-if="!$store.state.user.likes.includes(product.id)">
                    <button  type="button" class="btn btn-outline-success" @click="like"><i class="bi bi-heart"></i></button>
                </div>
                <div v-else>
                  <button type="button" class="btn btn-danger" @click="dislike"><i class="bi bi-heart-fill"></i></button>
                </div>
                
            </div>
          </div>
          <div class="row my-3" v-else>
            <div class="d-flex gap-2">
                <button type="button" class="btn btn-success" @click="addToCart">Добавить в корзину  <i class="bi bi-cart"></i></button>
            </div>
          </div>
          <div class="row">
            <div class="col-auto">
              <span class="text-secondary" style="font-size: 0.8em;"><i class="bi bi-box"></i></span>
              <span class="text-secondary ps-2" style="font-size: 0.8em;">27 ноября</span>
            </div>
            <div class="col">
              <span class="text-secondary" style="font-size: 0.8em;"><i class="bi bi-shop"></i></span>
              <span class="text-secondary ps-2" style="font-size: 0.8em;">Пункт выдачи: ул. Ленина д.1</span>
            </div>
          </div>
        </div>
        <!--Widget-->
        <div class="col-lg-3 border d-none d-lg-block">
          <span>Widget</span>
        </div>
        <!--End Widget-->
      </div>
      <!--About Product-->
      <div class="row mt-5">
        <div class="row">
          <div class="col">
            <h3>О товаре</h3>
          </div>
        </div>
        <div class="col mt-3">
          <span><b>Характеристики</b></span>
          <div class="row mt-3" v-for="property in product.properties">
            <div class="d-flex justify-content-between">
              <div class="text-secondary">Цвет</div>
              <div class="justify-content-start">{{ property.color }}</div>
            </div>
            <div class="d-flex justify-content-between">
              <div class="text-secondary">Вес</div>
              <div class="justify-content-start">{{ humanViewNumber(property.weight) }} кг</div>
            </div>
            <div class="d-flex justify-content-between">
              <div class="text-secondary">Длинна</div>
              <div class="justify-content-start">{{ property.length }} м</div>
            </div>
            <div class="d-flex justify-content-between">
              <div class="text-secondary">Ширина</div>
              <div class="justify-content-start">{{ property.width }} м</div>
            </div>
            <div class="d-flex justify-content-between">
              <div class="text-secondary">Высота</div>
              <div class="justify-content-start">{{ property.height }} м</div>
            </div>
            <div class="row mt-3">
              <div class="d-flex justify-content-between">
                <div class="text-secondary">Дополнительная информация</div>
                <div class="ms-3" style="text-align: justify; font-size: 0.9em;">
                  {{ property.description }}
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col mt-3 ms-3">
          <span><b>Описание</b></span>
          <div class="row mt-3" style="text-align: justify; font-size: 0.9em;">
            <div>{{ product.description }}</div>
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
            <div class="mt-3 d-flex flex-row gap-2">
                <div class="card mx-0 rounded-3" v-for="feedback in product.product_feedbacks" v-if="product.product_feedbacks.length > 0">
                  <feedback-widget :feedback="feedback">
                  </feedback-widget>
                </div>
                <div v-else>
                  Отзывов нет
                </div>
            </div>
          </div>
          <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
            <div class="col-12 mt-3" v-if="$store.state.userIsAuth">
              <product-question-form :user_id="$store.state.user.id" :product_id="product.id">
              </product-question-form>
            </div>
            <div class="mt-3 d-flex flex-row gap-2">
              <div v-for="question in product.questions" v-if="product.questions.length > 0">
                <question-widget :question="question"></question-widget>
              </div>
              <div v-else>
                Вопросов по данному товару нет
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
    <modal-component v-model:show="modalIsVisible">
      <div class="d-flex flex-column gap-3">
        <div>{{ product.name }} Добавлен</div>
        <div class="d-flex justify-content-between gap-4">
          <router-link to="/cart">Посмотреть корзину</router-link>
          <a href="#" @click="closeModal">Продолжить покупки</a>
        </div>
      </div>
    </modal-component>

    <modal-component v-model:show="editProductModal">
      <product-edit-component v-model:show="editProductModal" :product="product">
      </product-edit-component>
    </modal-component>

    <modal-component v-model:show="uploadImagesModal">
      <upload-image v-model:show="uploadImagesModal" :product="product"></upload-image>
    </modal-component>

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
                product: {},
                editProductData: {
                  product: this.product
                },
                modalIsVisible: false,
                editProductModal: false,
                uploadImagesModal: false,
            }
        },
        methods: {
            async uploadProduct() {
                try {
                      axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/products/${this.$route.params.id}/`,
                          method: 'get'
                        }
                      ).then((response) => {
                        if(response.data.his_rating.length != null)
                        {
                          response.data.his_rating.push({'value': 0.0, 'counter': 0})
                        }
                        this.product = response.data;
                        this.isProductLoading=true
                        })
                } catch(e) {
                    alert(`Connection error: ${e}`);
                }
                finally {
        
                }
            },

            async uploadProductEdit() {
              try {
                      axios(
                        {
                          url: `http://127.0.0.1:8000/api/v1/products/${this.$route.params.id}/`,
                          method: 'get'
                        }
                      ).then((response) => {
                        this.editProductData = response.data;
                        //this.isProductLoading=true
                        })
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
              this.modalIsVisible = true
            },

            like() {
              // Implement send to backend like product
              const like = {
                'product_id': this.product.id,
                'operation': 'like'
              }
              try {
                    axios(
                      {
                        url: `http://127.0.0.1:8000/api/v1/like/`,
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
              try {
                    axios(
                      {
                        url: `http://127.0.0.1:8000/api/v1/like/`,
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

            closeModal() {
              this.modalIsVisible = false
            },
            editProduct() {
              //this.uploadProductEdit()
              //console.log(this.product)
              this.editProductModal = true
            },
            uploadImages() {
              this.uploadImagesModal = true
            },
            formatDate(date){
                date = new Date(date)
                let year = new Intl.DateTimeFormat('ru', { year: 'numeric' }).format(date);
                let month = new Intl.DateTimeFormat('ru', { month: 'short' }).format(date);
                let day = new Intl.DateTimeFormat('ru', { day: '2-digit' }).format(date);
                let hour = new Intl.DateTimeFormat('ru', { hour: '2-digit' }).format(date);
                let minute = new Intl.DateTimeFormat('ru', { minute: '2-digit' }).format(date);
                return `${day} ${month} ${year} ${hour}:${minute}`
            },
            humanViewNumber(number) {
              return Number.parseFloat(number)
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