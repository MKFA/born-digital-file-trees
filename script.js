function toggleDropdown(button) {
  var parentDiv = button.parentNode; // Get the parent div element
  var dropdownContent = parentDiv.querySelector('.dropdown-content');
  dropdownContent.classList.toggle('show');
}

// Function to show the password modal
function showPasswordModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "block";
}

// Function to check the password
function checkPassword() {
  var password = document.getElementById("password").value;
  // Replace 'your_password' with the actual password
  if (password === 'poltergeist') {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
  } else {
    alert("Incorrect password. Please try again.");
  }
}
