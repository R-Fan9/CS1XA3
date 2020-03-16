# CS 1XA3 Project02 - fanh11

## Overview
This webpage is Ricky Fan's custom CV; it consists of four different sections.
The fist section "About Me" describes my personal details, contact information,
professional story and highlights of qualification. The second section 
"Education & Skills" lays out all the programming languages, frameworks, tools and databases 
that I am capable of using. It also indicates my certification and 
current education. The third section "Projects" lists all of my personal and school
projects that I have done in the past. The last section "Award & ECA" displays
my respectable award and the extracurricular activities that I have participated

## Custom Javascript Code

### Feature 01 
```
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
  options[sIndex-1].className += " active");
}

var sIndex = 1;
displaySlides(sIndex);

function curSlide(n) {
  displaySlides(sIndex = n);
}
```
Description: This feature navigates the user to different sections of my CV.
By clicking on the labels in the tabbed menu, different information about me
will be displayed. By default, the text and background color of the labels are
black and white. However, if the webpage is freshly loaded or reloaded, 
the first label will be "active", which is indicated by its white text and 
blue background. Also, if the user clicked on a specific label, it will turn 
"active" and the rest will remain as default. 

### Feature 02
```
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
});
```
Description: This feature hides and displays the tabbed menu based on the user's
scrolling motion. Since the position of the tabbed menu is fixed at the top of the 
webpage, it can disappear and reappear regardless of the scroll position of webpage. 
The user can have access to the tabbed menu whenever a scroll up motion is
detected. On the other hand, scrolling down will slide up the tabbed menu, which
makes it disappear from the webpage.    

### Feature 03
```
$(document).ready(function() {
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
});
```
Description: This feature creates an automatic slide show of images. For every
2 seconds, an old image will be replaced by a new image. If the image is the 
last one in all the given images, the first image will reappear and the cycle 
repeats.

### Feature 04
```
$(document).ready(function() {
    $('#changeColor li').hover(function(){
        $(this).css({color:"red"})
    }, function(){
        $(this).css({color:"#5A5D5E"})
    });
});
```
Description: This feature changes the text color of a word to red whenever 
the cursor is hovered over it. Once the cursor moves away from the word, its 
text color will go back to its original. This feature can be found in the 
second section - Education & Skills - of my CV.

### Feature 05
```
$(document).ready(function() {
    $('#expand').click(function(){
        $('.me').slideToggle('slow');
        $(this).toggleClass('active');
    });

    $('#expand2').click(function(){
        $('.me2').slideToggle('slow');
        $(this).toggleClass('active');
    });
});
``` 
Description: This feature creates two collapsible divisions within the first 
section - About Me - of my CV. By default, the contents of these divisions
are hidden. However, if the user clicks on the heading of each division, its 
content will slide down. Also, the user can hide the contents by simply
clicking on the headings again.

## References
- Original HTML template, thus no reference.

- The following snippet of javascript code is altered from [ByATool](http://byatool.com/uncategorized/add-remove-or-replace-a-css-class-using-javascript/) 
```
options[i].className = options[i].className.replace(" active", "");
```

- The following snippets of javascript code were altered from [Stack Overflow](https://stackoverflow.com/questions/18986623/addclass-and-removeclass-in-jquery-not-removing-class)
```
options[sIndex-1].className.addClass("active");                                                                                                                     options[sIndex-1].className += " active";
```
```
$('.navbar').removeClass('hide');
'''
```

- The following snippet of javascript code is altered from [w3schools](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_setinterval)

```
setInterval(slideShow,2000);
```

- The following snippet of javascript code is altered from [w3schools](https://www.w3schools.com/jquery/sel_firstchild.asp) 

```
$('.slideShow img:first-child').addClass('active'); 
```


- The following snippet of javascript code is altered from [w3schools](https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_eff_slidetoggle)
```
$('.me').slideToggle('slow');
```
