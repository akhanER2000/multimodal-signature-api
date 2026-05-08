# SOP: Inyección de Firmas en PDF
**Herramienta:** PyMuPDF (fitz)
**Regla de Negocio:** El sistema recibe un JSON con el PDF en Base64 y la firma en Base64 (data URI). 
**Flujo:**
1. Decodificar el PDF en memoria (stream).
2. Decodificar la imagen de la firma, limpiando el encabezado `data:image/...`.
3. Calcular el `fitz.Rect` usando las coordenadas absolutas enviadas por el frontend.
4. Insertar la imagen en la página objetivo.
5. Guardar el nuevo documento obligatoriamente en la carpeta `.tmp/` sin sobrescribir el original.
