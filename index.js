const chatBox = document.getElementById("chatBox");

function addMessage(text, type) {
  const msg = document.createElement("div");
  msg.classList.add("message", type);
  msg.innerText = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function showTyping() {
  const typing = document.createElement("div");
  typing.classList.add("message", "bot");
  typing.id = "typing";

  typing.innerHTML = `
    <div class="typing">
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
  `;

  chatBox.appendChild(typing);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTyping() {
  const typing = document.getElementById("typing");
  if (typing) typing.remove();
}

function botReply(userText) {
  const replies = [
    "Interesting question!",
    "I'm thinking about that...",
    "Here's what I found!",
    "Let me explain that simply."
  ];
  return replies[Math.floor(Math.random() * replies.length)];
}

function sendMessage() {
  const input = document.getElementById("userInput");
  const text = input.value.trim();
  if (!text) return;

  addMessage(text, "user");
  input.value = "";

  showTyping();

  setTimeout(() => {
    removeTyping();
    addMessage(botReply(text), "bot");
  }, 1000);
}

/* Enter key support */
document.getElementById("userInput")
  .addEventListener("keypress", function(e) {
    if (e.key === "Enter") sendMessage();
  });
