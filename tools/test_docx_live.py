import docx
import base64
import json
import os
import io
from docx_injector import process_docx_signature

def run_docx_test():
    print("Iniciando prueba viva DOCX...")
    # Crear DOCX en blanco en memoria
    doc = docx.Document()
    doc.add_paragraph("Documento de prueba.")
    buffer = io.BytesIO()
    doc.save(buffer)
    docx_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    # Imagen de prueba (1x1 pixel rojo)
    img_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
    
    payload = {
        "document": {
            "filename": "test_base.docx",
            "mime_type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "content_base64": docx_b64
        },
        "signature_data": {
            "type": "image",
            "payload": f"data:image/png;base64,{img_b64}",
            "position": {"width": 100}
        }
    }
    
    os.makedirs(".tmp", exist_ok=True)
    json_path = ".tmp/test_docx_schema.json"
    with open(json_path, "w") as f:
        json.dump(payload, f)
        
    output_path = ".tmp/signed_test_output.docx"
    success = process_docx_signature(json_path, output_path)
    if success: print(f"✅ PRUEBA VIVA DOCX SUPERADA: {output_path}")

if __name__ == "__main__":
    run_docx_test()
