function writeFakeNews() {
  $("#summary").empty();
  let title = $("#title").value();
  let link = $("#link1").value();

  let text = "title: " + title + "link:" + link

  $("#summary").append("fake news reported: " + text);

function initializeJs() {
  $(".clickableArea").append("hi");
}

$(document).ready(initializeJs);
