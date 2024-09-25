document.addEventListener('DOMContentLoaded', function() {
    // Select all tables
    const tables = document.querySelectorAll('table');

    tables.forEach(table => {
        let totalAmount = 0;
        let totalCommission = 0;

        // Select all amount and commission cells in the current table
        const amountCells = table.querySelectorAll('.amount');
        const commissionCells = table.querySelectorAll('.commission');

        // Calculate total amounts for the current table
        amountCells.forEach(cell => {
            const amount = parseFloat(cell.textContent.replace('$', '').replace(',', ''));
            totalAmount += amount;
        });

        commissionCells.forEach(cell => {
            const commission = parseFloat(cell.textContent.replace('$', '').replace(',', ''));
            totalCommission += commission;
        });

        // Update the total values in the table footer
        table.querySelector('#totalAmount').innerHTML = `<strong>$${totalAmount.toFixed(2)}</strong>`;
        table.querySelector('#totalCommission').innerHTML = `<strong>$${totalCommission.toFixed(2)}</strong>`;
    });
});
