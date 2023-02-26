// Smooth scroll to top
$('footer a[href="#top"]').on('click', function(){
  $('html, body').animate({scrollTop:0}, 'slow');
  return false;
});
