// Show the loader when an action button is clicked
function showLoader() {
    document.getElementById('loader').style.display = 'flex';
  }
  
  // Optionally, hide the loader after a delay (e.g., when the server responds)
  function hideLoader() {
    document.getElementById('loader').style.display = 'none';
  }
  
  // Add event listeners to all buttons
  document.querySelectorAll('.btn').forEach(function(button) {
    button.addEventListener('click', function() {
      showLoader();
      // Simulate delay (for example, until form is submitted or server responds)
      setTimeout(hideLoader, 5000); // Adjust time as needed
    });
  });
  