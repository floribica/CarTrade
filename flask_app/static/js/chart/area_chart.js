document.addEventListener('DOMContentLoaded', function() {
    // Confirmed payments data
    const totalConfirmDataElement = document.getElementById('total-confirm-data');
    const totalConfirmData = JSON.parse(totalConfirmDataElement.value || '[]');
  
    // Unconfirmed payments data
    const totalUnconfirmDataElement = document.getElementById('total-unconfirm-data');
    const totalUnconfirmData = JSON.parse(totalUnconfirmDataElement.value || '[]');
  
    // Check if data is valid
    if (!Array.isArray(totalConfirmData) || totalConfirmData.length === 0 ||
        !Array.isArray(totalUnconfirmData) || totalUnconfirmData.length === 0) {
      console.error('No data available for the chart.');
      return;
    }
  
    // Extract labels (e.g., months)
    const labels = totalConfirmData.map(item => item.month); // Assume both datasets have the same months
  
    // Extract data for confirmed and unconfirmed payments
    const confirmData = totalConfirmData.map(item => item.total_confirm);
    const unconfirmData = totalUnconfirmData.map(item => item.total_unconfirm);
  
    // Create the combined area chart
    const ctx = document.getElementById('combined-area-chart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          {
            label: 'Confirmed Payments',
            data: confirmData,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: true,
            pointRadius: 5,
            pointBackgroundColor: 'rgba(75, 192, 192, 1)',
            tension: 0.3 // Smoothing of the line
          },
          {
            label: 'Unconfirmed Payments',
            data: unconfirmData,
            backgroundColor: 'rgba(255, 99, 132, 0.2)', // Different color for unconfirmed
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 2,
            fill: true,
            pointRadius: 5,
            pointBackgroundColor: 'rgba(255, 99, 132, 1)',
            tension: 0.3 // Smoothing of the line
          }
        ]
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
  