import fitz
import base64
import json
import os

def process_pdf_signature(input_json_path, output_pdf_path):
    output_dir = os.path.dirname(output_pdf_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(input_json_path, 'r') as f:
        data = json.load(f)
        
    try:
        pdf_bytes = base64.b64decode(data['document']['content_base64'])
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        page_index = data['document'].get('page_target', 1) - 1
        page = doc[page_index]
        
        # Dimensiones absolutas de la pagina objetivo
        page_width = page.rect.width
        page_height = page.rect.height
        
        # signature_data es un ARRAY (Lista)
        signatures = data.get('signature_data', [])
        
        for sig_item in signatures:
            sig_payload = sig_item['payload']
            if "," in sig_payload:
                sig_base64 = sig_payload.split(",")[1]
            else:
                sig_base64 = sig_payload
            sig_bytes = base64.b64decode(sig_base64)
            
            pos = sig_item['position']
            
            # Convertir porcentajes a coordenadas absolutas del PDF
            x0 = pos['x_pct'] * page_width
            y0 = pos['y_pct'] * page_height
            x1 = x0 + (pos['w_pct'] * page_width)
            y1 = y0 + (pos['h_pct'] * page_height)
            
            rect = fitz.Rect(x0, y0, x1, y1)
            page.insert_image(rect, stream=sig_bytes)
            
        doc.save(output_pdf_path)
        doc.close()
        return True
    except Exception as e:
        print(f"ERROR procesando PDF: {e}")
        return False
