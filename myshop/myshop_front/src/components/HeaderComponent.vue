<template>
    <div>
        <!--Правая панель-->
        <aside class="offcanvas offcanvas-start right-menu" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasExampleLabel">Каталог</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <div class="row pt-2">
              <div class="col">
                <a href="#"><i class="bi bi-caret-right pe-2"></i> Сантехника</a>
              </div>
            </div>
            <div class="row pt-2">
              <div class="col">
                <a href="#"> <i class="bi bi-caret-right pe-2"></i> Обои</a>
              </div>
            </div>
            <div class="row pt-2">
              <div class="col">
                <a href="#"><i class="bi bi-caret-right pe-2"></i> Ванны</a>
              </div>
            </div>
            <div class="row pt-2">
              <div class="col">
                <a href="#"><i class="bi bi-caret-right pe-2"></i> Потолочная плитка</a>
              </div>
            </div>
            <div class="row pt-2">
              <div class="col">
                <a href="#"><i class="bi bi-caret-right pe-2"></i> Линолеум</a>
              </div>
            </div>
            <div class="row pt-2">
              <div class="col">
                <a href="#"><i class="bi bi-paint-bucket pe-2"></i> Краски</a>
              </div>
            </div>
          </div>
        </aside>
        <!--end Off Canvas-->
        <ul class="nav flex-column bg-dark menu-background">
        <div class="container-xl">
          <!--Top line of links-->
          <li class="nav-item d-none d-lg-block">
            <ul class="nav">
              <li class="nav-link menu1">
                <router-link to="/about">&#8226; About</router-link>
              </li>
              <li class="nav-link menu1">
                <router-link to="/">&#8226; My Cart</router-link>
              </li>
              <li class="nav-link menu1">
                <router-link to="/">&#8226; {{ $store.state.likes }}</router-link>
              </li>
            </ul>
          </li>
          <!--Middle navbar-->
          <li class="nav-item">
            <div class="container-fluid py-1">
              <div class="row pe-2 align-items-center">
                <!--Logo-->
                <div class="col-md-auto logo d-none d-lg-block">
                  <router-link to="/">
                    <h2><span class="logoM">М</span><span class="logo-end">озаика</span></h2>
                  </router-link>
                </div>
                <!--Off canvas button-->
                <div class="col-md-auto text-light d-none d-lg-block">
                  <button class="btn btn-outline-light" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample" aria-controls="">
                    <i class="bi bi-list"></i>
                  </button>
                </div>
                <div class="col">
                    <div class="form-group has-search">
                        <div class="form-control-feedback">
                            <i class="bi bi-search"></i>
                        </div>
                        <input 
                          v-model="searchQuery"
                          type="text" 
                          name="query" 
                          class="form-control rounded-9" 
                          placeholder="Нати на сайте Мозаика" 
                          value=""
                          @change="searh">
                    </div>
                </div>
                <div class="col-md-auto d-none d-lg-block">
                  <div class="container">
                    <div class="row menu1">
                      <div class="col">
                        <UserTab></UserTab>
                      </div>
                      <div class="col">
                        <router-link to="/cart">
                          <i class="bi bi-bag position-relative" style="font-size: 1.5rem;">
                            <span v-if="$store.getters.getCartPositionCount>0" class="position-absolute top-100 start-100 translate-middle badge rounded-pill bg-danger" style="font-size: 0.6rem;">
                              {{ $store.getters.getCartPositionCount }}
                              <span class="visually-hidden">unread messages</span>
                            </span>
                          </i>
                        </router-link>
                      </div>
                      <div class="col">
                        <router-link to="/">
                          <i class="bi bi-heart" style="font-size: 1.5rem;"></i>
                        </router-link>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </li>
          <!--Bottom nav element-->
          <li class="nav-item d-none d-lg-block">
            <div class="container-fluid text-light">
              <div class="p-2">
                Other nav element
              </div>
            </div>
          </li>
        </div>
      </ul>
    </div>
</template>

<script>
import UserTab from '@/components/UserTab.vue'

    export default {
    components: { UserTab },
    data() {
      return {
        searchQuery: ''
      }
    },
    methods: {
      searh() {
        this.$router.push({name: 'search', params: {query: this.searchQuery}})
      }

    }
}
</script>

<style scoped>

</style>