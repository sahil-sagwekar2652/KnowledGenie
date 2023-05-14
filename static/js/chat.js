
const chat = document.querySelector('.chat')
const inputText = document.getElementById("input-text");
const createPElementsButton = document.getElementById("create-p-elements");

createPElementsButton.addEventListener("click", () => {
  // Get the text from the input text field
  const text = inputText.value;

  // Create a new paragraph element for each line of text
  for (const line of text.split('\n')) {
    const pElement = document.createElement("p");
    pElement.textContent = line;
    pElement.className +="received"
    chat.appendChild(pElement);
  }
});