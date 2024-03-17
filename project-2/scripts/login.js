// Login functionality
const $loginForm = document.getElementById("login-form")
$loginForm.addEventListener("submit", function(event) {
    event.preventDefault(); // prevent default form submission
    // You can add your login logic here
    // For demonstration purpose, I'm just redirecting to the dashboard page
    window.location.href = "dashboard.html";
});