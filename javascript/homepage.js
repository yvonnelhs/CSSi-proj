
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
  $('.boxes').append('<br><div style="background-color:#f4f8f9; padding:10px;"></div><div class="wrapping"><div id="newsTitle">Title: {{fakeNewsTitle}}</div><div id="newsLink">Link: <a href={{fakeNewsLink}}>{{fakeNewsLink}}</a></div><div id="newsContent">Description:{{fakeNewsMessage}}</div></div>');

  $('#loading').fadeOut();
};
