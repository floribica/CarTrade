document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the JSON data from the hidden input
    const totalClientDataElement = document.getElementById('total-client-data');
    const totalClientData = JSON.parse(totalClientDataElement.value || '[]');
  
    // Extract labels (months) and data (totals)
    const labels = totalClientData.map(item => item.month);
    const data = totalClientData.map(item => item.total_client);
  
    // Create the bar chart
    const ctx = document.getElementById('morris-bar-chart').getContext('2d');
    const myBarChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Total Clients',
          data: data,
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  });
  