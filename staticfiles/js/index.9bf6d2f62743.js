$(function(){
    var company_img_top = $("#company-img").offset().top;
    var win_h = $(window).height();
    var start_c_img = company_img_top - win_h;

    $(window).scroll(function () {
        var y = $(this).scrollTop();
        if (y >= start_c_img) {
            $('#company-img').css('background-position-y', +(y - company_img_top) * 0.5 + 'px');
        }
    });
});

