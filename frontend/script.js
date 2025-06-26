window.onload = () => {
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class='bot-msg'>¡Hola! Soy un chatbot especializado en sitios turísticos de Cartagena, Colombia. Pregúntame por lugares turísticos y te daré detalles.</div>`;
};

function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    const chatBox = document.getElementById("chat-box");

    if (message === "") return;

    chatBox.innerHTML += `<div class='user-msg'>${message}</div>`;

    fetch("/chat", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div class='bot-msg'>${data.response}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    input.value = "";
}