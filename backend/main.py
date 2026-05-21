from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()
WA_PHONE   = os.environ.get("NOTIFY_PHONE", "50495292446")
WA_APIKEY  = os.environ.get("CALLMEBOT_APIKEY", "")

SYSTEM_PROMPT = """Eres el asistente virtual de Tecnología Para Todos, un servicio freelance de automatización y documentos con IA.

SERVICIOS Y PRECIOS:
- Conversión PDF a Word/Excel/PPT: desde $5 (1-10 pág), $12 (11-30), $20 (31-50), $35 (51-100)
- Chatbot WhatsApp 24/7 para negocios: desde $149
- Página web profesional con bot incluido: desde $150
- Traducción español/inglés/portugués: desde $0.08/palabra
- Transcripción de audio/video: desde $0.50/minuto
- Automatización con IA: cotizar según proyecto
- Contenido con IA para redes sociales: cotizar

TIEMPOS DE ENTREGA:
- Documentos: 2-4 horas
- Traducciones: 24 horas
- Chatbots: 3 días
- Páginas web: 5 días

PAGOS: PayPal, transferencia bancaria Honduras. 50% al inicio, 50% al entregar.
CONTACTO WhatsApp: +504 9529-2446

Responde en español, amable y directo. Máximo 3 oraciones por respuesta.
Responde preguntas sobre servicios, precios, tiempos y pagos directamente.
Solo menciona WhatsApp cuando el cliente pida hablar con una persona.
IMPORTANTE: Responde SOLO con el texto. Nunca incluyas JSON ni metadatos."""

class HistoryMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: list[HistoryMessage] = []

class ChatResponse(BaseModel):
    reply: str
    redirect_wa: bool = False


def notificar_whatsapp(mensaje: str):
    if not WA_APIKEY:
        return
    try:
        texto = f"💬 Nuevo mensaje en tu web:\n\"{mensaje}\""
        requests.get(
            "https://api.callmebot.com/whatsapp.php",
            params={"phone": WA_PHONE, "text": texto, "apikey": WA_APIKEY},
            timeout=8
        )
    except Exception:
        pass


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    keywords_wa = [
        "hablar con alguien", "hablar con una persona", "humano", "persona real",
        "quiero hablar", "agente", "asesor", "necesito ayuda de alguien",
    ]
    redirect = any(kw in req.message.lower() for kw in keywords_wa)

    # Notificar solo en el primer mensaje de la conversación
    if len(req.history) == 0:
        notificar_whatsapp(req.message)

    if redirect:
        return ChatResponse(
            reply="¡Claro! Te conecto con nuestro equipo ahora mismo. 👇",
            redirect_wa=True
        )

    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        },
        json={
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 300,
            "system": SYSTEM_PROMPT,
            "messages": [{"role": m.role, "content": m.content} for m in req.history[-8:]]
                        + [{"role": "user", "content": req.message}]
        },
        timeout=30
    )
    data = response.json()
    reply = data["content"][0]["text"]
    return ChatResponse(reply=reply, redirect_wa=False)


@app.get("/health")
def health():
    return {"status": "ok"}
