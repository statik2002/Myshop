<template>
    <div>
        <ul class="nav flex-column bg-dark menu-background">
        <div class="container-xl">
          <!--Top line of links-->
          <li class="nav-item d-none d-lg-block">
            <ul class="nav">
              <li class="nav-link menu1">
                <a href="" @click="$router.push('/about')">&#8226; About</a>
              </li>
              <li class="nav-link menu1">
                <a href="#">&#8226; Two</a>
              </li>
              <li class="nav-link menu1">
                <a href="#">&#8226; Three</a>
              </li>
            </ul>
          </li>
          <!--Middle navbar-->
          <li class="nav-item">
            <div class="container-fluid py-1">
              <div class="row pe-2 align-items-center">
                <!--Logo-->
                <div class="col-md-auto logo d-none d-lg-block">
                  <a href="#" @click="$router.push('/')">
                    <h2><span class="logoM">М</span><span class="logo-end">озаика</span></h2>
                  </a>
                </div>
                <!--Off canvas button-->
                <div class="col-md-auto text-light d-none d-lg-block">
                  <button class="btn btn-outline-light" type="button" data-bs-toggle="offcanvas" data-bs-target="#" aria-controls="">
                    <i class="bi bi-list"></i>
                  </button>
                </div>
                <div class="col">
                  <form>
                    <div class="form-group has-search">
                      <!--
                        <span class="form-control-feedback">
                            <i class="bi bi-search"></i>
                        </span>
                      -->
                        <input type="text" name="query" class="form-control rounded-9" placeholder="Нати на сайте Мозаика" value="">
                    </div>
                  </form>
                </div>
                <div class="col-md-auto d-none d-lg-block">
                  <div class="container">
                    <div class="row menu1">
                      <div class="col">
                        <a href="#" data-bs-title="Cabinet"><i class="bi bi-person-circle" style="font-size: 1.5rem;"></i></a>
                      </div>
                      <div class="col">
                        <a href="#" data-bs-title="Your cart"><i class="bi bi-bag" style="font-size: 1.5rem;"></i></a>
                      </div>
                      <div class="col">
                        <a href="#" data-bs-title="Your likes"><i class="bi bi-heart" style="font-size: 1.5rem;"></i></a>
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
import router from '@/router/router';

    export default {
    components: { router }
}
</script>

<style scoped>

</style>