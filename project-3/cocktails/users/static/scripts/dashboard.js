const $dashboard = document.getElementById("checkbox-form");

$dashboard.addEventListener("submit", function (event) {
  event.preventDefault();
  var checkboxes = document.querySelectorAll('input[type="checkbox"]');
  var allChecked = true;
  checkboxes.forEach(function (checkbox) {
    if (!checkbox.checked) {
      allChecked = false;
    }
  });
  if (allChecked) {
    window.location.href = "/task1/";
  } else {
    alert("Please check all checkboxes before proceeding.");
  }
});
