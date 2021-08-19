$('.header-menu').on('click',function(){
    $('.menu-line-top').toggleClass('active-line-top');
    $('.menu-line-bottom').toggleClass('active-line-bottom');
    $('.full-nav').toggleClass('full-nav-active');
    $('header').toggleClass('active-header');
    $('body').toggleClass('active-body');

    $('.nav-item').toggleClass('scroll-in');
});

$(function(){
    var fadeIn = $(".fade-in");
    $(window).on("scroll", function () {
        $(fadeIn).each(function () {
        var offset = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        if (scroll > offset - windowHeight + 150) {
            $(this).addClass("scroll-in");
        }
        });
    });
});