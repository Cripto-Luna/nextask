# NexTask — Configuración del proyecto

## Descripción
Sitio web de servicios freelance con bot de atención 24/7 automatizado.
URL: https://cripto-luna.github.io/nextask

## Servicios y precios (investigados en Fiverr 2026)
- Conversión de documentos (PDF → Word/Excel/PPT): desde $5
- Chatbot web 24/7 para negocios: desde $149
- Traducción español/inglés/portugués: desde $0.08/palabra
- Transcripción de audio/video: desde $0.50/minuto
- Automatización de procesos con IA: precio por proyecto
- Contenido con IA para redes sociales: precio por proyecto
- Diseño y desarrollo de páginas web: desde $150

## Contacto
- WhatsApp: +504 9529-2446
- Correo: 21dinamica@gmail.com
- PayPal: https://paypal.me/lunaproducts62
- Transferencia bancaria local (Honduras)
- Pago: 50% al inicio, 50% al entregar
- Entrega: 24-48h documentos, 3-5 días páginas web. Pagos en USD.

## Arquitectura del sitio NexTask
- Frontend: GitHub Pages → https://github.com/Cripto-Luna/nextask
- Backend: Railway (FastAPI + Python) → https://web-production-be310.up.railway.app
- Bot: API de Anthropic (claude-haiku-4-5-20251001), usa `requests` directo a la API
- API Key: guardada en Railway como variable ANTHROPIC_API_KEY (sin espacios ni saltos de línea)
- Para forzar redeploy en Railway: cambiar variable TEMP a cualquier valor nuevo

## Filosofía del bot
- El bot responde TODO automáticamente (precios, info, tiempos de entrega, formas de pago)
- WhatsApp solo aparece como enlace cuando el cliente pide hablar con una persona
- Todos los botones de la página abren el chatbot (no WhatsApp directo)
- Interferencia humana mínima — todo automatizado

## Archivos clave NexTask
- `index.html` — landing page completa
- `styles.css` — tema oscuro, color principal #6366f1 (púrpura)
- `script.js` — lógica del chatbot widget
- `backend/main.py` — FastAPI endpoint /chat
- `backend/requirements.txt` — fastapi, uvicorn, requests, pydantic, python-dotenv
- `backend/Procfile` — `web: uvicorn main:app --host 0.0.0.0 --port $PORT`

## Proceso para crear página web a un cliente

### Lo que necesitas pedir al cliente:
1. Nombre del negocio y logo (si tienen)
2. Colores preferidos (opcional)
3. Secciones que quieren (servicios, precios, galería, contacto, etc.)
4. Textos e info del negocio (si no tienen, se redactan con IA)
5. Fotos (si no tienen, usamos imágenes de stock gratuitas)
6. Correo y número de contacto

### Proceso técnico:
1. Cliente da la info → se pega en Claude Code
2. Claude genera index.html + styles.css + script.js completos
3. Se crea un repo en GitHub para ese cliente (bajo cuenta Cripto-Luna)
4. Se sube el código → página en vivo en cripto-luna.github.io/nombre-cliente
5. Se manda link al cliente para revisión (hasta 2 rondas de ajustes)
6. Si quiere dominio propio (sunegocio.com): ~$12/año en Namecheap, costo del cliente

### Stack para páginas de clientes:
- HTML/CSS/JS puro (mismo estilo que NexTask)
- GitHub Pages (hosting gratis)
- Se puede incluir chatbot (mismo sistema que NexTask) como extra

## Proceso para crear chatbot a un cliente

### Tipos de chatbot que podemos ofrecer:
- **Básico** ($149): Responde preguntas, da precios, info del negocio — igual que NexTask
- **Medio** ($250+): Agenda citas, consulta inventario via Google Sheets
- **Avanzado** ($400+): Integración con WhatsApp Business API oficial (Meta)

### Proceso técnico chatbot básico:
1. Cliente da info del negocio (servicios, precios, horarios, contacto)
2. Claude genera el system prompt y el backend FastAPI
3. Se despliega en Railway (cuenta del cliente o la nuestra)
4. Se embebe en su página web existente o se crea página nueva
5. Tiempo de entrega: 1-2 días

### Costo real del chatbot para nosotros:
- API Anthropic (claude-haiku): ~$1-2/mes por cliente con uso normal
- Railway hosting: gratis hasta $5/mes de créditos
- Margen real: casi 100% de ganancia

## Lecciones aprendidas (errores a evitar)
- La API key de Anthropic en Railway NO debe tener espacios ni saltos de línea al final
- Cuando Railway no auto-despliega: cambiar variable TEMP a nuevo valor para forzar deploy
- El frontend (GitHub Pages) y backend (Railway) son repositorios separados
- Usar `requests` directo a la API de Anthropic (no el SDK) para evitar problemas de compatibilidad con Python 3.13
