<template>
    <header-component></header-component>
    <div class="wrapper">
        

        <!--== Start Preloader Content ==-->
        <div class="preloader-wrap" v-if="!isCabinetLoad">
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

        <main class="main-content">
            <div class="container mt-5">
                <div class="row">
                    <div class="col-xl-6 p-3 border">
                        <widget-component>Widget</widget-component>
                    </div>
                    <div class="col-xl-6 p-3 border">
                        <div class="p-3 border">Widget1</div>
                    </div>
                </div>
            </div>
        </main>
        
    </div>
    <footer-component></footer-component>
</template>

<script>
    export default {
        data() {
            return {
                isCabinetLoad: true
            }
        }
    }
</script>

<style scoped>

</style>