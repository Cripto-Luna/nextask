# Tecnología Para Todos — Configuración del proyecto

## Descripción
Sitio web de servicios freelance con bot de atención 24/7 automatizado.
Nombre: Tecnología Para Todos (mismo nombre que el canal de YouTube)
URL: https://cripto-luna.github.io/Tecnologia-para-Todos

## Canal de YouTube
- URL: https://www.youtube.com/@TECNOLOGIAPARATODOS-e8w
- Estrategia: poner link de la página en descripción de cada video para conseguir clientes orgánicos

## Servicios y precios (investigados en Fiverr 2026)
- Conversión de documentos PDF a Word/Excel/PPT:
  * 1-10 páginas: $5
  * 11-30 páginas: $12
  * 31-50 páginas: $20
  * 51-100 páginas: $35
  * Más de 100 páginas: cotizar
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

## Arquitectura del sitio
- Frontend: GitHub Pages → https://github.com/Cripto-Luna/Tecnologia-para-Todos
- Backend: Railway (FastAPI + Python) → https://web-production-be310.up.railway.app
- Bot: API de Anthropic (claude-haiku-4-5-20251001), usa `requests` directo a la API
- API Key: guardada en Railway como variable ANTHROPIC_API_KEY (sin espacios ni saltos de línea)
- Para forzar redeploy en Railway: cambiar variable TEMP a cualquier valor nuevo

## Estructura de la página (secciones en orden)
1. **Navbar** — Logo centrado (LOGO.png, 130px), badge "Tecnología Para Todos" debajo, nav links a la derecha
2. **Hero** — Título, descripción, botones Cotizar/Ver servicios, stats 24/7 · USD · IA
3. **Cómo funciona** — 3 pasos: Escríbenos → Recibimos tu proyecto → Entregamos
4. **Servicios** — 7 tarjetas: Documentos, Chatbot, Traducción, Transcripción, Automatización, Páginas Web, Contenido IA
5. **Precios** — 4 tarjetas: Documentos $5, Chatbot $149, Página Web $150, Traducción $0.08/palabra
6. **Testimonios** — 3 reseñas de ejemplo (María González, Carlos Mendoza, Ana Reyes)
7. **Formulario de reseña** — Nombre, negocio, estrellas, texto → envía por WhatsApp al dueño
8. **CTA/Contacto** — Botón asistente, email, PayPal, banco local, link YouTube
9. **Footer** — Logo, descripción, link YouTube, copyright

## Chat widget
- Botones rápidos: 📄 Convertir PDF · 🤖 Chatbot WhatsApp · 🌐 Traducción · 🖥️ Página Web
- WhatsApp solo aparece si el cliente pide hablar con una persona humana

## Filosofía del bot
- El bot responde TODO automáticamente (precios, info, tiempos de entrega, formas de pago)
- NUNCA redirige a WhatsApp para cotizaciones estándar — las maneja directamente
- WhatsApp solo aparece como enlace cuando el cliente pide hablar con una persona
- Interferencia humana mínima — todo automatizado

## Archivos clave
- `index.html` — landing page completa
- `styles.css` — tema oscuro, color principal #6366f1 (púrpura), hero padding-top: 14rem
- `script.js` — lógica del chatbot widget + formulario de reseñas (WhatsApp pre-fill)
- `LOGO.png` — logo descargado del canal de YouTube
- `backend/main.py` — FastAPI endpoint /chat con precios por volumen
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
- HTML/CSS/JS puro (mismo estilo que Tecnología Para Todos)
- GitHub Pages (hosting gratis)
- Se puede incluir chatbot (mismo sistema) como extra

## Proceso para crear chatbot a un cliente

### Tipos de chatbot que podemos ofrecer:
- **Básico** ($149): Responde preguntas, da precios, info del negocio
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
- El hero necesita padding-top: 14rem porque el navbar es alto (logo 130px + badge)
- clip-path: inset(0 0 16% 0) en .logo-img recorta el texto "TECNOLOGIA" del logo
- El bot debe tener instrucción explícita de NO redirigir a WhatsApp para cotizaciones estándar
