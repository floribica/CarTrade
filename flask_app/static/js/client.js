function openModalWithRentData() {
    // Collect data from the rent form
    const pickupLocation = document.getElementById('pickup_location').value;
    const dropoffLocation = document.getElementById('dropoff_location').value;
    const pickupDate = document.querySelector('input[name="pickup_date"]').value;
    const dropoffDate = document.querySelector('input[name="dropoff_date"]').value;
    const pickupTime = document.querySelector('input[name="pickup_time"]').value;
    const dropoffTime = document.querySelector('input[name="dropoff_time"]').value;
  
    // Populate hidden fields in the modal with rent form data
    document.getElementById('modal_pickup_location').value = pickupLocation;
    document.getElementById('modal_dropoff_location').value = dropoffLocation;
    document.getElementById('modal_pickup_date').value = pickupDate;
    document.getElementById('modal_dropoff_date').value = dropoffDate;
    document.getElementById('modal_pickup_time').value = pickupTime;
    document.getElementById('modal_dropoff_time').value = dropoffTime;
  
    // Open the modal
    document.getElementById('confirmationModal').style.display = 'block';
  }
  
  function closeModal() {
    document.getElementById('confirmationModal').style.display = 'none';
  }
  
  function submitBothForms(event) {
    event.preventDefault(); // Prevent the modal form from submitting by itself
  
    // Submit both forms together by creating a FormData object
    const rentForm = document.getElementById('rentForm');
    const registerForm = document.getElementById('registerForm');
  
    const formData = new FormData(rentForm);
  
    // Append the registration form data to the rent form data
    const registerFormData = new FormData(registerForm);
    for (let pair of registerFormData.entries()) {
      formData.append(pair[0], pair[1]);
    }
  
    // Send the combined form data using AJAX (or use a redirect if preferred)
    fetch(registerForm.action, {
      method: 'POST',
      body: formData
    }).then(response => {
      if (response.ok) {
        // Handle success, such as redirecting to another page
        window.location.href = `/rent/car/${document.querySelector('input[name="car_id"]').value}`;
      } else {
        // Handle error
        console.error('Error submitting form');
      }
    });
  }
  