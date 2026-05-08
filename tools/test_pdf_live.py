import fitz
import base64
import json
import os
from pdf_injector import process_pdf_signature

def run_live_test():
    print("Iniciando generación de artefactos de prueba...")
    
    # 1. Crear PDF de prueba en memoria
    doc = fitz.open()
    doc.new_page()
    pdf_bytes = doc.write()
    doc.close()
    pdf_b64 = base64.b64encode(pdf_bytes).decode('utf-8')
    
    # 2. Imagen de prueba (1x1 pixel rojo PNG en base64)
    img_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
    
    # 3. Construir JSON conforme al Input Schema
    payload = {
        "document": {
            "filename": "test_base.pdf",
            "mime_type": "application/pdf",
            "content_base64": pdf_b64,
            "page_target": 1
        },
        "signature_data": {
            "type": "image",
            "payload": f"data:image/png;base64,{img_b64}",
            "position": {
                "x": 100,
                "y": 100,
                "width": 50,
                "height": 50
            }
        }
    }
    
    os.makedirs(".tmp", exist_ok=True)
    json_path = ".tmp/test_input_schema.json"
    
    with open(json_path, "w") as f:
        json.dump(payload, f)
        
    output_path = ".tmp/signed_test_output.pdf"
    
    # 4. Disparar herramienta
    print("Ejecutando inyección PDF...")
    success = process_pdf_signature(json_path, output_path)
    
    if success and os.path.exists(output_path):
        print(f"✅ PRUEBA VIVA SUPERADA. Archivo final generado exitosamente en: {output_path}")
    else:
        print("❌ FALLO EN LA PRUEBA VIVA.")

if __name__ == "__main__":
    run_live_test()
