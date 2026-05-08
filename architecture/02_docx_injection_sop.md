# SOP: Inyección de Firmas en DOCX
**Herramienta:** python-docx
**Regla de Negocio:** El sistema recibe un JSON con el DOCX en Base64 y la firma en Base64.
**Restricción Arquitectónica:** A diferencia de un PDF, DOCX gestiona el contenido como un flujo. Las coordenadas `(x, y)` del Input Schema serán ignoradas para evitar corromper la estructura XML del documento.
**Flujo:**
1. Decodificar el DOCX en memoria (`io.BytesIO`).
2. Decodificar la imagen de la firma.
3. Crear un nuevo párrafo al final del documento con alineación centrada.
4. Insertar la imagen en el párrafo, utilizando el atributo `width` del JSON (transformado a Puntos - Pt) para dimensionar.
5. Guardar el nuevo documento en `.tmp/`.
