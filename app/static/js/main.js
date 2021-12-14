var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

$(document).ready(function () {
  $("#sCard").hover(function (event) {
    event.preventDefault();
    $("#arrow3").toggle(500);
    $("#Three").css("color", "#ffde22")
  });
  $("#sCard").mouseout(function (event) {
    event.preventDefault();
    $("#Three").removeAttr("style");
  });
});

$(function () {
  $("#typ").typed({
    strings: ["See The News, Feel The Shine!"],
    typeSpeed:200
  });
});
$(document).ready(function() {
  $('body').bootstrapMaterialDesign();
  
  
});
var $ps = $("#wraps").children("#area");
$ps.slice(4).hide(); // hide all p-tags after the first one
// add the read more after the first element
$ps.eq(3).after($('<button class="btn btn-success" id="mybut" type="button">Load More <i class="fas fa-chevron-circle-down"></i></button>').click(function(){
    // if the read more link is clicked, remove the read more link and show all p-tags
    $(this).remove();
    $ps.show();
})); 
//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
$(document).ready(function(){
  $("#query").val('')
});