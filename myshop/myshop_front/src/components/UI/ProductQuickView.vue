<template>
    <div class="product-quick-view-content">
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            <span class="close-icon"><i class="bi bi-x-lg"></i></span>
        </button>
        <div class="row">
        <div class="col-lg-6 col-md-6 col-12">
            <div class="thumb">
                <img v-if="product.product_images.length > 0" :src=product.product_images[0].image alt="Alan-Shop">
                <img v-else src="@/assetes/no_image.png" alt="Alan-Shop">
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
                    <div class="inc qty-btn">+</div>
                    <input type="text" id="quantity4" title="Quantity" value="1" />
                    <div class= "dec qty-btn">-</div>
                </div>
                <button class="btn btn-black">Add to cart</button>
            </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            product: {
                type: Object
            }
        }
    }
</script>

<style scoped>

</style>