# 🏛️ Firma-multimodal | Proyecto B.L.A.S.T.

Un sistema robusto y determinista para la inyección de firmas digitales (trazos, texto o imágenes) en documentos PDF y DOCX, diseñado bajo la arquitectura **B.L.A.S.T.** y optimizado para entornos Serverless.

## 🚀 Características Principales

- **Multimodalidad:** Permite capturar firmas mediante dibujo táctil/mouse (Canvas), generación por tipografía cursiva o carga de imágenes locales.
- **Soporte PDF (PyMuPDF):** Inyección precisa basada en coordenadas absolutas (x, y) manteniendo la integridad de los metadatos.
- **Soporte DOCX (python-docx):** Inyección por flujo de texto (centrado al final del documento) para evitar la corrupción del esquema XML de Word.
- **Arquitectura Layered:** Separación clara entre motores de inyección (Capa 3), Router API (Capa 2) y Frontend UI (Capa 1).
- **Producción Ready:** Configuración lista para despliegue en Vercel (Serverless) y soporte para contenedores Docker.

## 🛠️ Stack Tecnológico

- **Backend:** Python 3.10+, FastAPI, Uvicorn.
- **Manipulación Documental:** PyMuPDF (fitz), python-docx.
- **Frontend:** Vanilla JS, SignaturePad, HTML5 Canvas.
- **Infraestructura:** Vercel (Python Runtime), Docker.

## 📦 Estructura del Proyecto

```text
├── architecture/       # Especificaciones SOP y reglas de negocio
├── frontend/           # Interfaz de usuario estática
├── tools/              # Motores de inyección y scripts de prueba
├── .tmp/               # Almacenamiento temporal de artefactos (Local)
├── main.py             # Router FastAPI (Entry point)
├── vercel.json         # Configuración Serverless
└── requirements.txt    # Dependencias de Python
```

## 💻 Instalación Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/akhanER2000/multimodal-signature-api.git
   cd multimodal-signature-api
   ```

2. **Configurar el Entorno Virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Instalar Dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el Servidor de Desarrollo:**
   ```bash
   uvicorn main:app --reload
   ```
   Accede a: `http://127.0.0.1:8000`

## 🧪 Pruebas de Handshake

Para verificar que el entorno tiene los motores de inyección correctamente configurados, puedes ejecutar:
```bash
python tools/handshake.py
```

## 📜 Licencia

Proyecto desarrollado bajo el protocolo B.L.A.S.T. para gestión de documentos multimodales.
