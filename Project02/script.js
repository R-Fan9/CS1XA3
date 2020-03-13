function displaySlides(n) {
  var slides = document.getElementsByClassName("mySlides");
  var options = document.getElementsByClassName("option");
  if (n > slides.length) {sIndex = 1}
  if (n < 1) {sIndex = slides.length}

  for (var i = 0; i < options.length; i++) {
    options[i].className = options[i].className.replace(" active", "");
  }

  for (var i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }

  slides[sIndex-1].style.display = "block";
  options[sIndex-1].className += " active";
}

var sIndex = 1;
displaySlides(sIndex);

function curSlide(n) {
  displaySlides(sIndex = n);
}

$(document).ready(function() {
    var lSTop = 0;

    $(window).on('scroll', function () {
        var cSTop = $(this).scrollTop();

        if (cSTop > lSTop){
            $('.navbar').addClass('hide');
        }else{
            $('.navbar').removeClass('hide');
        }

        lSTop=cSTop;
    });

    function slideShow(){
        var current=$('.slideShow img.active');
        if (current.length==0){
            $('.slideShow img:first-child').addClass('active');
        } else{
            var next=current.removeClass('active').next();
            if (next.length==0){
                $('.slideShow img:first-child').addClass('active');
            } else{
                next.addClass('active');
            }
        }
    }
    setInterval(slideShow,2000);

    $('#changeColor li').hover(function(){
        $(this).css({color:"red"})
    }, function(){
        $(this).css({color:"#5A5D5E"})
    });

    $('#expand').click(function(){
        $('.me').slideToggle('slow');
        $(this).toggleClass('active');
    });

    $('#expand2').click(function(){
        $('.me2').slideToggle('slow');
        $(this).toggleClass('active');
    });

});
