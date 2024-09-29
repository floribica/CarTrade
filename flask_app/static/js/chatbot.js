const socket = io();
const chatbot = $("#chatbot");
const toggleButton = $("#toggle-button");
let inactivityTimeout;

// Function to hide the chatbot
function hideChatbot() {
  chatbot.css("left", "-320px");
}

// Function to show the chatbot
function showChatbot() {
  chatbot.css("left", "0px");
  resetInactivityTimer();
}

// Function to send a message
function sendMessage() {
  const msg = $("#myMessage").val();
  if (msg.trim()) {
    $("#messages").append($("<li>").text(msg).addClass("user-message"));
    $("#myMessage").val("");
    socket.send(msg);
    $("#messages").scrollTop($("#messages")[0].scrollHeight); // Auto-scroll to the bottom
  }
}

// Listen for messages from the server
socket.on("message", function (msg) {
  $("#messages").append($("<li>").text(msg).addClass("bot-message"));
  $("#messages").scrollTop($("#messages")[0].scrollHeight); // Auto-scroll to the bottom
});

// Toggle chatbot visibility
toggleButton.click(function () {
  if (chatbot.css("left") === "0px") {
    hideChatbot();
  } else {
    showChatbot();
  }
});

// Reset inactivity timer
function resetInactivityTimer() {
  clearTimeout(inactivityTimeout);
  inactivityTimeout = setTimeout(hideChatbot, 5000); // Hide after 5 seconds of inactivity
}

// Event listeners to reset the timer on user interaction
$(document).on("mousemove click keypress", resetInactivityTimer);

// Hide the chatbot if clicked outside
$(document).click(function (event) {
  if (!$(event.target).closest("#chatbot, #toggle-button").length) {
    hideChatbot();
  }
});

function checkEnter(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
}