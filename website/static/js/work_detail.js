$(function() {
  let tabs = $(".img-window");
  console.log(tabs);
  $(".img-window").on("click", function() {
    $(".active").removeClass("active");
    $(this).addClass("active");
    const index = tabs.index(this);
    $(".thumbnail-img").removeClass("show").eq(index).addClass("show");
  })
})