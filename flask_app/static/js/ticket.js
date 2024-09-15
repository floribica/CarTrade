// Get the current date
var today = new Date();

// Create an array of month names
var months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
];

// Extract the month, day, and year
var month = months[today.getMonth()]; // Get month name
var day = today.getDate(); // Get day of the month
var year = today.getFullYear(); // Get full year

// Format the date as "Month Day, Year"
var formattedDate = month + " " + day + ", " + year;

// Display the formatted date in the HTML element with id "current-date"
document.getElementById("current-date").textContent = formattedDate;

// invoice.js

// Get the total amount from the backend-rendered HTML
const totalAmount = parseFloat(document.getElementById("total-amount").innerText);

// Define the tax rate
const taxRate = 0.20;

// Calculate tax and total (total is unchanged from backend)
const tax = totalAmount * taxRate;
const subTotal = totalAmount - tax;
console.log(subTotal);
console.log(tax);

// Update the HTML elements with the calculated values
document.getElementById("display-subtotal").innerText = `$${subTotal.toFixed(2)}`;
document.getElementById("display-tax").innerText = `$${tax.toFixed(2)}`;
document.getElementById("display-total").innerText = `$${totalAmount.toFixed(2)}`;
