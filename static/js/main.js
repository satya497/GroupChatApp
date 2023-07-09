// main.js

// Show and hide forms based on the selected action
document.getElementById("selectAction").addEventListener("change", function() {
  var selectedAction = this.value;
  var forms = document.getElementsByClassName("form");

  for (var i = 0; i < forms.length; i++) {
      forms[i].style.display = "none";
  }

  if (selectedAction) {
      document.getElementById(selectedAction + "Form").style.display = "block";
  }
});

// Handle form submissions
document.getElementById("createUser").addEventListener("submit", function(event) {
  event.preventDefault();
  // Code to handle the form submission
});

document.getElementById("editUser").addEventListener("submit", function(event) {
  event.preventDefault();
  // Code to handle the form submission
});

document.getElementById("login").addEventListener("submit", function(event) {
  event.preventDefault();
  // Code to handle the form submission
});

document.getElementById("logout").addEventListener("submit", function(event) {
  event.preventDefault();
  // Code to handle the form submission
});

document.getElementById("createGroup").addEventListener("submit", function(event) {
  event.preventDefault();
  // Code to handle the form submission
});

document.getElementById("deleteGroup").addEventListener("submit", function(event) {
  event.preventDefault();
  // Code to handle the form submission
});

document.getElementById("searchGroups").addEventListener("submit", function(event) {
  event.preventDefault();
  // Code to handle the form submission
});

document.getElementById("sendMessage").addEventListener("submit", function(event) {
  event.preventDefault();
  // Code to handle the form submission
});

document.getElementById("likeMessage").addEventListener("submit", function(event) {
  event.preventDefault();
  // Code to handle the form submission
});
