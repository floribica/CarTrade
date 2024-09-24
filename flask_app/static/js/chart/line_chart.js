document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the JSON data from the hidden input
    const totalCarDataElement = document.getElementById('total-car-data');
    const totalCarData = JSON.parse(totalCarDataElement.value || '[]');
  
    // Check if data is valid
    if (!Array.isArray(totalCarData) || totalCarData.length === 0) {
      console.error('No data available for the chart.');
      return;
    }
  
    // Extract labels (months) and data (totals)
    const labels = totalCarData.map(item => item.month);
    const data = totalCarData.map(item => item.total_car);
  
    // Create the line chart
    const ctx = document.getElementById('morris-line-chart').getContext('2d');
    const myLineChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Total Cars',
          data: data,
          backgroundColor: 'rgba(255, 0, 0, 0.2)', // Light red fill
          borderColor: 'rgba(255, 0, 0, 1)', // Red line
          borderWidth: 2,
          fill: true, // Fill the area under the line
          pointRadius: 5, // Size of the dots
          pointBackgroundColor: 'rgba(255, 0, 0, 1)', // Dot color
          tension: 0.3 // Smoothing of the line
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  });
  