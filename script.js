function toggleDropdown(button) {
  var parentDiv = button.parentNode; // Get the parent div element
  var dropdownContent = parentDiv.querySelector('.dropdown-content');
  dropdownContent.classList.toggle('hide');
}

function toggleCollapse() {
  var dropdownContents = document.querySelectorAll('.dropdown-content');
  var button = document.getElementById("collapseButton");
  
  // Check the current state of the button text
  var buttonText = button.innerHTML.trim(); // Trim whitespace for consistency
  
  // Toggle the button text
  if (buttonText === "Collapse All Directories") {
    button.innerHTML = "Show All Directories";
    // Set all elements with class .dropdown-content to be hidden
    dropdownContents.forEach(function(element) {
      element.classList.add('hide');
    });
  } else {
    button.innerHTML = "Collapse All Directories";
    // Remove the hide class from all elements with class .dropdown-content
    dropdownContents.forEach(function(element) {
      element.classList.remove('hide');
    });
  }
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
