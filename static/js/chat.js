const chat = document.querySelector('.chat')
const inputText = document.getElementById("input-text");
const createPElementsButton = document.getElementById("create-p-elements");

createPElementsButton.addEventListener("click", () => {
  // Get the text from the input text field
  const text = inputText.value;

  // Create a new paragraph element for each line of text
  for (const line of text.split('\n')) {
    const divElement = document.createElement("div");
    const pElement = document.createElement("p");
    pElement.textContent = line;
    divElement.className = "message received";
    divElement.appendChild(pElement);
    chat.appendChild(divElement);
  }
});


const form = document.querySelector('#create-p-elements');
// select the div element with class "chat"
const chatDiv = document.querySelector('.chat');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const query = document.querySelector('#input-text').value;
  const response = await fetch('/process', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ query })
  });
  const { answer } = await response.json();

  // create a new HTML element and set its content
  const newElement = document.createElement('div');
  newElement.className = 'message sent';
  const pElement = document.createElement('p');
  pElement.textContent = answer;
  newElement.appendChild(pElement);

  // append the new element to the chat div
  chatDiv.appendChild(newElement);

});