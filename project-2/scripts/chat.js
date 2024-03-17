// API Key
const apiKey = "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";

// Chat display
const chatDisplay = document.getElementById("chat-display");

// User input
const userInput = document.getElementById("user-input");

// Send button
const sendBtn = document.getElementById("send-btn");

// Send message to API
async function sendMessage(message) {
  try {
    const response = await axios.post(
      "https://api.openai.com/v1/chat/completions",
      {
        model: "gpt-3.5-turbo",
        messages: [
          {
            role: "user",
            content: message,
          },
        ],
      },
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${apiKey}`,
        },
      }
    );
    return response.data.choices[0].text.trim();
  } catch (error) {
    console.error("Error:", error);
    return "Sorry, something went wrong.";
  }
}

// Display message in chat
function displayMessage(message) {
  const messageElement = document.createElement("div");
  messageElement.classList.add("message");
  messageElement.textContent = message;
  chatDisplay.appendChild(messageElement);
}

// Send button click event
sendBtn.addEventListener("click", async () => {
  const userMessage = userInput.value.trim();
  if (userMessage !== "") {
    displayMessage(`You: ${userMessage}`);
    const botResponse = await sendMessage(userMessage);
    displayMessage(`ChatGPT: ${botResponse}`);
    userInput.value = ""; // Clear input field
  }
});

// Initial welcome message
displayMessage("ChatGPT: Hello! How can I assist you today?");
