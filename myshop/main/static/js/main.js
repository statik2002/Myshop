function zoom(e){
    let zoomer = e.currentTarget;
    //let img = zoomer.querySelector("img");
    //zoomer.setAttribute('style', `background-image: url(${img.src})`);
    e.offsetX ? offsetX = e.offsetX : offsetX = e.touches[0].pageX
    e.offsetY ? offsetY = e.offsetY : offsetX = e.touches[0].pageX
    x = offsetX/zoomer.offsetWidth*100
    y = offsetY/zoomer.offsetHeight*100
    zoomer.style.backgroundPosition = x + '% ' + y + '%';
}

$(document).ready(function(){
    let multipleCardCarousel = document.querySelector("#carouselColorSlider");
    if (window.matchMedia("(min-width: 576px)").matches) {
        var carousel = new bootstrap.Carousel(multipleCardCarousel, {
            interval: false,
            wrap: false,
        });
        let carouselWidth = multipleCardCarousel.children[0].scrollWidth;
        let cardWidth = $("#carouselColorItem").width();
        let scrollPosition = 0;
        $("#carouselColorSlider .carousel-control-next").on("click", function () {
            if (scrollPosition < carouselWidth - cardWidth * 4) {
            scrollPosition += cardWidth;
            $("#carouselColorSlider .carousel-inner").animate(
                { scrollLeft: scrollPosition },
                600
            );
            }
        });
        $("#carouselColorSlider .carousel-control-prev").on("click", function () {
            if (scrollPosition > 0) {
            scrollPosition -= cardWidth;
            $("#carouselColorSlider .carousel-inner").animate(
                { scrollLeft: scrollPosition },
                600
            );
            }
        });
    } else {
        $(multipleCardCarousel).addClass("slide");
    }
});


