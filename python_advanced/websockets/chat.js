const socket = new WebSocket("ws://localhost:8000/ws");

const statusEl = document.getElementById("status");
const messages = document.getElementById("messages");
const form = document.getElementById("form");
const input = document.getElementById("input");

function setStatus(text, state) {
    statusEl.textContent = text;
    statusEl.className = `status ${state}`;
}

function addMessage(text, type) {
    const item = document.createElement("li");
    item.className = `message ${type}`;

    const time = document.createElement("span");
    time.className = "time";
    time.textContent = new Date().toLocaleTimeString();

    const body = document.createElement("span");
    body.textContent = text;

    item.append(time, body);
    messages.appendChild(item);
    messages.scrollTop = messages.scrollHeight;
}

socket.onopen = () => setStatus("Connected", "connected");
socket.onclose = () => setStatus("Connection lost", "disconnected");
socket.onerror = () => setStatus("Connection error", "disconnected");
socket.onmessage = (event) => addMessage(event.data, "received");

form.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = input.value;
    if (!text.trim() || socket.readyState !== WebSocket.OPEN) {
        return;
    }
    socket.send(text);
    addMessage(text, "sent");
    input.value = "";
    input.focus();
});
