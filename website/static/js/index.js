$(window).on('load',function(){
    $("#splash").delay(1500).fadeOut('slow');
	$("#splash_logo").delay(1500).fadeOut('slow');
});

$(function () {
    var company_img_top = $("#company-img").offset().top;
    var win_h = $(window).height();
    var start_c_img = company_img_top - win_h;

    $(window).scroll(function () {
        var y = $(this).scrollTop();
        if (y >= start_c_img) {
            $('#company-img').css('background-position-y', +(y - company_img_top) * 2 + 'px');
        }
    });
});

$(function () {
    const topRight = $(".top-right");
    const titleSvg = $(".title-svg");
    const titleImg =$(".title-img");
    let rightIndex = -1;
    let svgIndex = -1;
    let imgIndex = -1;
    topRight.hide();
    titleSvg.hide();
    titleImg.hide();

    function showNextTxt() {
        rightIndex++;
        topRight.eq(rightIndex % topRight.length).fadeIn('normal').delay(10000).fadeOut('slow', showNextTxt);
    }
    showNextTxt();

    function showNextSVG() {
        svgIndex++;
        titleSvg.eq(svgIndex % titleSvg.length).fadeIn('normal').delay(10000).fadeOut('slow', showNextSVG);
    }
    showNextSVG();

    function showNextImg() {
        imgIndex++;
        titleImg.eq(imgIndex % titleImg.length).fadeIn('normal').delay(10000).fadeOut('slow', showNextImg);
    }
    showNextImg();
});