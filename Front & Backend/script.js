document.getElementById("send-message").addEventListener("click", async function () {
  const query = document.getElementById("chat-query").value.trim();
  if (query === "") {
    // alert("Please enter a stock question!"); if desired
    return;
  }

  // Display user message
  const chatMessages = document.getElementById("chat-messages");
  const userMessage = document.createElement("div");
  userMessage.classList.add("user");
  userMessage.textContent = query;
  chatMessages.appendChild(userMessage);

  // Display bot's "thinking" message
  const botMessage = document.createElement("div");
  botMessage.classList.add("bot");
  botMessage.textContent = "Fetching data...";
  chatMessages.appendChild(botMessage);

  // Scroll to the bottom
  chatMessages.scrollTop = chatMessages.scrollHeight;

  try {
    // Extract ticker from the query (e.g., last word for now)
    const ticker = query.split(" ").pop().toUpperCase();

    // Make a request to the Flask backend
    const response = await fetch("http://127.0.0.1:5000/stock", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ticker }),
    });

    const data = await response.json();
    if (response.ok) {
      botMessage.textContent = `Stock: ${data.name} (${data.ticker})\nPrice: ${data.current_price} ${data.currency}`;
    } else {
      botMessage.textContent = `Error: ${data.error}`;
    }
  } catch (error) {
    botMessage.textContent = "An error occurred while fetching the data.";
  }

  // Clear the input
  document.getElementById("chat-query").value = "";
});
