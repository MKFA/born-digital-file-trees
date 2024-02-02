// Define the correct password
const correctPassword = "poltergeist";

// Handle form submission
document.getElementById("passwordForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form submission

  // Get the entered password
  const password = document.getElementById("passwordInput").value;

  // Check if the entered password matches the correct password
  if (password === correctPassword) {
    // Redirect to the protected content
    window.location.href = "d-0199filetree.html";
  } else {
    alert("Incorrect password. Please try again.");
  }
});
