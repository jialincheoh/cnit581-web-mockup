const apiKey = "";
const chatDisplay = document.getElementById("chat-display");
const generateBtn = document.getElementById("generate-btn");

let sloganIndex = 0;
const slogans = [
  "Slogan 1: Sip, Savor, and Celebrate!",
  "Slogan 2: Mixing Memories, One Cocktail at a Time.",
  "Slogan 3: Crafting Cheers, Stirring Stories.",
  "Slogan 4: Indulge in Liquid Luxury.",
  "Slogan 5: Taste the Spirit of Adventure.",
  "Slogan 6: Raise Your Glass to Unforgettable Moments.", 
  "Slogan 7: Shake, Stir, Sip, Repeat.",
  "Slogan 8: From Shaker to Sip, Pure Bliss.", 
  "Slogan 9: Where Every Sip Tells a Tale.", 
  "Slogan 10: Cocktails: Turning Ordinary Moments into Extraordinary Memories."
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