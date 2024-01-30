function checkColorSlider(){
    let slider = document.querySelector("#carouselColorSlider");
    let sliderElementCount = slider.querySelector(".carousel-inner").children.length;
    let sliderWidth = slider.children[0].scrollWidth;
    let sliderElementWidth = slider.querySelector(".carousel-inner").children[0].scrollWidth;

    if(sliderElementCount * sliderElementWidth < sliderWidth) {
        let carouselControlPrev = slider.querySelector(".carousel-control-prev");
        let carouselControlNext = slider.querySelector(".carousel-control-next");
        carouselControlPrev.style.visibility='hidden';
        carouselControlNext.style.visibility='hidden';
    }
}

function checkColorSliderResize(){
    let slider = document.querySelector("#carouselColorSlider");
    let sliderElementCount = slider.querySelector(".carousel-inner").children.length;
    let sliderWidth = slider.children[0].offsetWidth;
    let sliderElementWidth = slider.querySelector(".carousel-inner").children[0].scrollWidth;

    if(sliderElementCount * sliderElementWidth < sliderWidth) {
        let carouselControlPrev = slider.querySelector(".carousel-control-prev");
        let carouselControlNext = slider.querySelector(".carousel-control-next");
        carouselControlPrev.style.visibility='hidden';
        carouselControlNext.style.visibility='hidden';
    } else {
        let carouselControlPrev = slider.querySelector(".carousel-control-prev");
        let carouselControlNext = slider.querySelector(".carousel-control-next");
        carouselControlPrev.style.visibility='visible';
        carouselControlNext.style.visibility='visible';
    }
}

document.addEventListener("DOMContentLoaded", checkColorSlider);
window.onresize = checkColorSliderResize