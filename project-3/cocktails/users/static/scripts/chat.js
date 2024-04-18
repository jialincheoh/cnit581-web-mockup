const apiKey = "sk-proj-4bcAtROw9mwf43Z7tGVUT3BlbkFJyh34j5IVUvam3wIrMvUv";
const chatDisplay = document.getElementById("chat-display");
const generateBtn = document.getElementById("generate-btn");

let sloganIndex = 0;
const slogans = [
  "Slogan 1: Your Cocktail, Our Passion!",
  "Slogan 2: Shake It Up with Our Signature Cocktail!",
  "Slogan 3: Taste the Difference with Our Crafted Cocktails!",
  "Slogan 4: Unwind with Our Exquisite Cocktails!",
  "Slogan 5: Elevate Your Spirits with Our Premium Cocktails!",
  "Slogan 6: Cheers to Great Times with Our Cocktails!"
];

generateBtn.addEventListener("click", () => {
  if (sloganIndex < slogans.length) {
    displayMessage(`ChatGPT: ${slogans[sloganIndex]}`);
    sloganIndex++;
  }
});

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

displayMessage("ChatGPT: Message me to generate a slogan to sell your cocktail.");