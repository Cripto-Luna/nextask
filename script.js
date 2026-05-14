const BACKEND_URL = "https://web-production-be310.up.railway.app";
const WA_NUMBER = "50495292446";

function openChat() {
    document.getElementById('chatWidget').classList.add('open');
    document.getElementById('chatInput').focus();
}

function toggleChat() {
    const widget = document.getElementById('chatWidget');
    widget.classList.toggle('open');
}

function quickMsg(text) {
    document.getElementById('chatInput').value = text;
    sendMessage();
}

function handleKey(e) {
    if (e.key === 'Enter') sendMessage();
}

async function sendMessage() {
    const input = document.getElementById('chatInput');
    const text = input.value.trim();
    if (!text) return;

    addMsg(text, 'user');
    input.value = '';

    const typingId = addMsg('Escribiendo...', 'bot typing');

    try {
        const res = await fetch(`${BACKEND_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });
        const data = await res.json();
        removeMsg(typingId);
        addMsg(data.reply, 'bot');

        if (data.redirect_wa) {
            setTimeout(() => {
                const waText = encodeURIComponent(`Hola, vengo del sitio web. ${text}`);
                addMsg(`<a href="https://wa.me/${WA_NUMBER}?text=${waText}" target="_blank" style="color:#818cf8">👉 Cotizar por WhatsApp</a>`, 'bot');
            }, 800);
        }
    } catch {
        removeMsg(typingId);
        addMsg('Hubo un error. Escríbenos directamente por <a href="https://wa.me/' + WA_NUMBER + '" target="_blank" style="color:#818cf8">WhatsApp</a>.', 'bot');
    }
}

function addMsg(text, cls) {
    const messages = document.getElementById('chatMessages');
    const div = document.createElement('div');
    div.className = `msg ${cls}`;
    div.innerHTML = text;
    const id = 'msg_' + Date.now();
    div.id = id;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
    return id;
}

function removeMsg(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
}
