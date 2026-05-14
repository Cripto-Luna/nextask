# NexTask — Configuración del proyecto

## Descripción
Sitio web de servicios freelance con bot de atención 24/7 automatizado.
URL: https://cripto-luna.github.io/nextask

## Servicios y precios
- Conversión de documentos (PDF → Word/Excel/PPT): desde $5
- Chatbot WhatsApp 24/7 para negocios: desde $99
- Traducción español/inglés/portugués: desde $0.08/palabra
- Transcripción de audio/video: precio por proyecto
- Automatización de procesos con IA: precio por proyecto
- Contenido con IA para redes sociales: precio por proyecto
- Diseño y desarrollo de páginas web: desde $150

## Contacto
- WhatsApp: +504 9529-2446
- Correo: 21dinamica@gmail.com
- Formas de pago: PayPal (internacional) · Transferencia bancaria local (Honduras)
- Entrega: 24-48h según el proyecto. Pagos en USD.

## Arquitectura
- Frontend: GitHub Pages → https://github.com/Cripto-Luna/nextask
- Backend: Railway (FastAPI + Python) → https://web-production-be310.up.railway.app
- Bot: API de Anthropic (claude-haiku-4-5-20251001), usa `requests` directo a la API
- API Key: guardada en Railway como variable ANTHROPIC_API_KEY

## Filosofía del bot
- El bot responde TODO automáticamente (precios, info, tiempos de entrega)
- WhatsApp solo aparece como enlace cuando el cliente pide hablar con una persona
- Todos los botones de la página abren el chatbot (no WhatsApp directo)
- Interferencia humana mínima — todo automatizado

## Archivos clave
- `index.html` — landing page completa
- `styles.css` — tema oscuro, color principal #6366f1 (púrpura)
- `script.js` — lógica del chatbot widget
- `backend/main.py` — FastAPI endpoint /chat
- `backend/requirements.txt` — fastapi, uvicorn, requests, pydantic, python-dotenv
- `backend/Procfile` — `web: uvicorn main:app --host 0.0.0.0 --port $PORT`
