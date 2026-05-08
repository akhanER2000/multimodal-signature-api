# 🏛️ Proyecto: Firma-multimodal | Constitución B.L.A.S.T.

## 1. Discovery (Visión Fundamental)
*   **North Star:** Un sistema robusto y determinista para inyectar firmas (trazos, texto o imágenes) en documentos PDF y DOCX sin corromper la metadata o formato original.
*   **Integraciones / Dependencias Base:** Python (para manipulación de PDF/DOCX en el backend), Entorno Virtual aislado, HTML/CSS/JS (Frontend/Canvas).
*   **Source of Truth:** Los documentos originales cargados por el usuario. El sistema NUNCA sobrescribe el original, siempre genera un nuevo artefacto en `.tmp/` hasta su exportación final.
*   **Delivery Payload:** Un documento firmado codificado en Base64 o como un stream de archivo binario listo para descarga.
*   **Behavioral Rules:** Todo procesamiento de archivos debe ocurrir en la capa `tools/`. Si un documento está corrupto o protegido con contraseña, el sistema debe fallar elegantemente y devolver un error específico en el Output Schema.

---

## 2. Esquemas de Datos (Data-First Rule)
*INVARIANTE:* Ningún script de `tools/` puede procesar datos que no cumplan estrictamente con este contrato JSON.

### 📥 Input Schema (Lo que envía el Frontend al Backend)
```json
{
  "document": {
    "filename": "contrato_base.pdf",
    "mime_type": "application/pdf",
    "content_base64": "JVBERi0xLjcKCjEgMCBvYmog...",
    "page_target": 1
  },
  "signature_data": {
    "type": "canvas",  // Opciones: "canvas" (dibujo), "text" (texto generado), "image" (imagen subida)
    "payload": "data:image/png;base64,iVBORw0K...", // Imagen final a inyectar (generada por canvas, tipografía o subida)
    "position": {
      "x": 150.5,
      "y": 600.0,
      "width": 200,
      "height": 75
    }
  }
}
```

### 📤 Output Schema (Lo que el Backend devuelve al Frontend)
```json
{
  "status": "success", // Opciones: "success", "error"
  "message": "Firma procesada e inyectada correctamente.",
  "output_document": {
    "filename": "contrato_base_signed.pdf",
    "mime_type": "application/pdf",
    "content_base64": "JVBERi0xLjcKCjQgMCBvYmog..."
  },
  "error_details": null // Contendrá detalles técnicos si status == "error"
}
```
