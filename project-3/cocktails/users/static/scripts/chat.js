const apiKey = "";

const chatDisplay = document.getElementById("chat-display");

const userInput = document.getElementById("user-input");

const sendBtn = document.getElementById("send-btn");

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

function displayMessage(message) {
  const messageElement = document.createElement("div");
  messageElement.classList.add("message");
  messageElement.textContent = message;
  chatDisplay.appendChild(messageElement);
}

sendBtn.addEventListener("click", async () => {
  const userMessage = userInput.value.trim();
  if (userMessage !== "") {
    displayMessage(`You: ${userMessage}`);
    const botResponse = await sendMessage(userMessage);
    displayMessage(`ChatGPT: ${botResponse}`);
    userInput.value = ""; 
  }
});

displayMessage("ChatGPT: Message me to generate a slogan to sell your cocktail.");
