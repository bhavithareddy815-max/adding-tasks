function validateLogin() {
    let email = document.getElementById("login_email").value;
    let password = document.getElementById("login_password").value;

    if (email === "" || password === "") {
        alert("All fields are required!");
        return false;
    }

    if (!email.includes("@")) {
        alert("Enter a valid email address!");
        return false;
    }

    if (password.length < 6) {
        alert("Password must be at least 6 characters");
        return false;
    }

    return true;
}


// -------- REGISTER VALIDATION --------
function validateRegister() {
    let email = document.getElementById("reg_email").value;
    let password = document.getElementById("reg_password").value;

    if (!email.includes("@")) {
        alert("Enter a valid email address!");
        return false;
    }

    if (password.length < 6) {
        alert("Password must be at least 6 characters");
        return false;
    }

    return true;
}