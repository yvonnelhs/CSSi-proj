var count=0;
$(document).ready(function(){
  $(window).scroll(function(){
    //Check for user has reached bottom of Page
    if($(window).scrollTop()==($(document).height()-window.innerHeight)){
      $('#loading').fadeIn();
      setTimeout("appendContent()", 1000);
    }
  });
});
var appendContent=function(){
  $('#content').prepend("---------------------<br>Title: {{fakeNewsTitle}} <br>Link: {{fakeNewsLink}} <br>Message: {{fakeNewsMessage}}<br>---------------------");

  $('#loading').fadeOut();
};
