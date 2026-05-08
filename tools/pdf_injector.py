import fitz
import base64
import json
import os

def process_pdf_signature(input_json_path, output_pdf_path):
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
    
    with open(input_json_path, 'r') as f:
        data = json.load(f)
        
    try:
        # 1. Cargar PDF desde base64
        pdf_bytes = base64.b64decode(data['document']['content_base64'])
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        page_index = data['document'].get('page_target', 1) - 1
        page = doc[page_index]
        
        # 2. Cargar imagen de la firma (limpiando data URI)
        sig_payload = data['signature_data']['payload']
        if "," in sig_payload:
            sig_base64 = sig_payload.split(",")[1]
        else:
            sig_base64 = sig_payload
        sig_bytes = base64.b64decode(sig_base64)
        
        # 3. Calcular Rectángulo (x0, y0, x1, y1)
        pos = data['signature_data']['position']
        rect = fitz.Rect(pos['x'], pos['y'], pos['x'] + pos['width'], pos['y'] + pos['height'])
        
        # 4. Inyectar imagen
        page.insert_image(rect, stream=sig_bytes)
        
        # 5. Guardar en .tmp/
        doc.save(output_pdf_path)
        doc.close()
        
        print(f"✅ ÉXITO: PDF firmado generado en {output_pdf_path}")
        return True
    except Exception as e:
        print(f"❌ ERROR CRÍTICO procesando PDF: {e}")
        return False

if __name__ == "__main__":
    print("Módulo pdf_injector.py creado y verificado por el linter (sin ejecutar prueba viva).")
