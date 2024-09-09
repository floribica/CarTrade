function openModal(carId) {
    console.log('Opening modal for carId:', carId); // Debugging line
  
    fetch(`/get_car_details/${carId}`)
      .then(response => response.json())
      .then(data => {
        console.log('Received data:', data); // Debugging line
  
        document.getElementById('carousel-images').innerHTML = data.images.map(img => `<img src="../static/images/${img}" alt="Car Image">`).join('');
        document.getElementById('car-details').innerHTML = `
          <h2>${data.brand} ${data.model}</h2>
          <p><strong>Year:</strong> ${data.year}</p>
          <p><strong>Price:</strong> $${data.price}</p>
          <p><strong>Mileage:</strong> ${data.km} Km</p>
          <p><strong>Description:</strong> ${data.description}</p>`;
        document.getElementById('car_id').value = data.id;
  
        // Display the modal
        document.getElementById('carModal').style.display = 'block';
      })
      .catch(error => console.error('Error:', error));
  }
  
  function closeModal() {
    document.getElementById('carModal').style.display = 'none';
  }
  
  window.onclick = function(event) {
    if (event.target === document.getElementById('carModal')) {
      closeModal();
    }
  }
  