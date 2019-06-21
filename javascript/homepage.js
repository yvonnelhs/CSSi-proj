var count=0;
$(document).ready(function(){
  $(window).scroll(function(){
    //Check for user has reached bottom of Page
    if($(window).scrollTop()==($(document).height()-window.innerHeight)){
      $('#loading').fadeIn();
      setTimeout("appendContent()", 500);
    }
  });
});
var appendContent=function(){
  $('.boxes').append("<br>Title: {{fakeNewsTitle}} <br>Link: {{fakeNewsLink}} <br>Message: {{fakeNewsMessage}}<br><hr>");

  $('#loading').fadeOut();
};
