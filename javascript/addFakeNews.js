function writeFakeNews() {
  $("#summary").empty();
  let title = $("#title").value();
  let link = $("#link1").value();

  let text = "";
  if (title != "" && link != "") {
    text = title + " and " + link;
  } else if (title == "") {
    text = link;
  } else {
    text = title;
  }

  $("#summary").append("fake news reported: " + text);

function initializeJs() {
  $("#submitButton").click(writeFakeNews);
}

$(document).ready(initializeJs);
