function validateText(field) {
  if (field.value.trim().length < 3) {
    field.style.border = "2px solid red";
  } else {
    field.style.border = "2px solid green";
  }
}

function validateEmail(field) {
  let pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  if (!field.value.match(pattern)) {
    field.style.border = "2px solid red";
  } else {
    field.style.border = "2px solid green";
  }
}

function highlight(field) {
  field.style.backgroundColor = "#f0f8ff";
}

function removeHighlight(field) {
  field.style.backgroundColor = "white";
}

function confirmSubmit() {
  const name = document.getElementById("name");
  const email = document.getElementById("email");
  const message = document.getElementById("message");
  const error = document.getElementById("error");

  // Basic final validation before submit
  if (name.value.trim().length < 3) return error.textContent = "Name must be at least 3 characters.";
  if (!email.value.match(/^[^ ]+@[^ ]+\.[a-z]{2,3}$/)) return error.textContent = "Enter a valid email.";
  if (message.value.trim().length < 3) return error.textContent = "Message must be at least 3 characters.";

  error.textContent = "";

  // Double click confirmation popup
  if (confirm("Are you sure you want to submit feedback?")) {
    // If confirmed, submit the form now
    document.querySelector("form").submit();
  }
}