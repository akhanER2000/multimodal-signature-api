# 🔎 Archivo de Descubrimientos y Restricciones (Research)

## 1. Manipulación de PDF (Backend)
*   **Librería Seleccionada:** `PyMuPDF` (también conocida como `fitz`).
*   **Razón:** Permite inserción determinista de imágenes y texto usando coordenadas absolutas `(x, y)` manteniendo la estructura y metadata del PDF intacta.
*   **Restricción:** Requiere manejar el sistema de coordenadas de PDF (el origen `[0,0]` suele estar en la esquina inferior izquierda o superior izquierda dependiendo de la rotación de la página). El Frontend deberá normalizar las coordenadas antes de enviar el Payload.

## 2. Manipulación de DOCX (Backend)
*   **Librería Seleccionada:** `python-docx`.
*   **Razón:** Es el estándar determinista para manipular archivos Word en Python.
*   **Restricción Crítica (¡Atención Arquitectura!):** A diferencia de un PDF, un DOCX no utiliza coordenadas absolutas (X, Y). Es un flujo de texto. 
*   **Solución (SOP):** Para DOCX, la firma no se inyectará en `x, y`. Se insertará al final del documento, en un marcador específico (bookmark), o en un párrafo predefinido. Esto requerirá una validación en el código: si `mime_type == "docx"`, ignorar `position` y usar inserción por flujo.

## 3. Interfaz Multimodal (Frontend)
*   **Librería Seleccionada (Canvas):** `signature_pad` (Vanilla JS) o `Fabric.js`.
*   **Razón:** Genera directamente el Base64 (`data:image/png;base64...`) que nuestro backend espera recibir en el Input Schema. Elimina la necesidad de procesar trazos vectoriales en el servidor.
