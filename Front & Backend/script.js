// Dark Mode Logic: Move outside the send-message event listener
const toggleTheme = document.getElementById("theme-toggle");
toggleTheme.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});

// Event Listener for Sending Messages
document.getElementById("send-message").addEventListener("click", async function () {
  const query = document.getElementById("chat-query").value.trim();
  if (query === "") {
    alert("Please enter a stock question!");
    return;
  }

  // Display user message
  const chatMessages = document.getElementById("chat-messages");
  const userMessage = document.createElement("div");
  userMessage.classList.add("user");
  userMessage.textContent = query;
  chatMessages.appendChild(userMessage);

  // Display spinner
  const spinner = document.getElementById("loading-spinner");
  spinner.style.display = "block";

  try {
    // Make the request to your backend
    const ticker = query.split(" ").pop().toUpperCase();
    const response = await fetch("http://127.0.0.1:5000/stock", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ticker }),
    });

    const data = await response.json();

    // Hide spinner after fetching
    spinner.style.display = "none";

    // Defensive check for backend response
    const botMessage = document.createElement("div");
    botMessage.classList.add("bot");
if (response.ok && data.name && data.ticker) {
    botMessage.textContent = `Stock: ${data.name} (${data.ticker})\nPrice: ${data.current_price} ${data.currency}`;
} else {
    botMessage.textContent = `Sorry, I couldn't find information for the ticker "${ticker}".`;
}

    chatMessages.appendChild(botMessage);
  } catch (error) {
    spinner.style.display = "none"; // Hide spinner if an error occurs
    const botMessage = document.createElement("div");
    botMessage.classList.add("bot");
    botMessage.textContent = "An error occurred while fetching the data.";
    chatMessages.appendChild(botMessage);
  }

  // Scroll to the bottom and clear input
  chatMessages.scrollTop = chatMessages.scrollHeight;
  document.getElementById("chat-query").value = "";
});
