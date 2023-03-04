$(document).ready(function(){
  //smoot scroll to the top
  $('footer a[href="#top"]').on('click', function(){
    $('html, body').animate({scrollTop:0}, 'slow');
    return false;
  })

  //navbar togller
  $(".menu-toggle-btn").click(function(){
    $(this).toggleClass("fa-times");
    $(".navigation-menu").toggleClass("active");
  });

  //account sign up popup
  //$("#create-account").dialog()
}); 

