document.addEventListener('DOMContentLoaded', function() {
    // Get the data from hidden inputs
    const totalConfirmElement = document.getElementById('total-confirm');
    const totalConfirmData = JSON.parse(totalConfirmElement.value || '[]');
    const totalClientElement = document.getElementById('total-client');
    const totalClientData = JSON.parse(totalClientElement.value || '[]');

    // Check if data is valid
    if (!Array.isArray(totalConfirmData) || totalConfirmData.length === 0 || 
        !Array.isArray(totalClientData) || totalClientData.length === 0) {
        console.error('No data available for the donut chart.');
        return;
    }

    // Extract totals from the data
    const confirmedPayments = totalConfirmData.reduce((acc, item) => acc + (item.total_confirm || 0), 0); // Sum of total_confirm
    const totalClients = totalClientData.reduce((acc, item) => acc + (item.total_client || 0), 0); // Sum of total_client

    // Create the donut chart
    const ctx = document.getElementById('donut-chart').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut', // Donut chart
        data: {
            labels: ['Confirmed Payments', 'Total Clients'],
            datasets: [{
                label: 'Payment vs Clients Data',
                data: [confirmedPayments, totalClients],
                backgroundColor: [
                    'rgba(85, 107, 47, 0.6)', // Olive Green for confirmed payments
                    'rgba(30, 144, 255, 0.6)'  // Dodger Blue for total clients
                ],
                borderColor: [
                    'rgba(85, 107, 47, 1)', // Olive Green border
                    'rgba(30, 144, 255, 1)'  // Dodger Blue border
                ],
                borderWidth: 2 // Increase border width for visibility
            }]
        },
        options: {
            responsive: true,
            cutout: '60%', // Adjust cutout percentage for space from border
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            const value = tooltipItem.raw;
                            return `${tooltipItem.label}: ${value}`;
                        }
                    }
                }
            }
        }
    });
});
