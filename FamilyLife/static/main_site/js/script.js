const passwordInput = document.getElementById("password");
const showPasswordButton = document.getElementById("show-password-button");

showPasswordButton.addEventListener("click", () => {
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        showPasswordButton.querySelector("img").src = "../../static/main_site/img/view.png";
    } else {
        passwordInput.type = "password";
        showPasswordButton.querySelector("img").src = "../../static/main_site/img/hide.png";
    }
});
