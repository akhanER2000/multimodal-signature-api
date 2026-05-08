# SOP: Router / API (Layer 2)
El backend expone un endpoint POST en FastAPI. Recibe el Input Schema. Evalúa `mime_type`:
- Si es `application/pdf` -> llama a `process_pdf_signature`
- Si es Word -> llama a `process_docx_signature`
Devuelve el Output Schema codificando el archivo de `.tmp/` en Base64.
