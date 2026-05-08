import docx
import base64
import json
import os
import io

def process_docx_signature(input_json_path, output_docx_path):
    output_dir = os.path.dirname(output_docx_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(input_json_path, 'r') as f:
        data = json.load(f)
        
    try:
        docx_bytes = base64.b64decode(data['document']['content_base64'])
        doc_stream = io.BytesIO(docx_bytes)
        doc = docx.Document(doc_stream)
        
        signatures = data.get('signature_data', [])
        
        for sig_item in signatures:
            sig_payload = sig_item['payload']
            if "," in sig_payload:
                sig_base64 = sig_payload.split(",")[1]
            else:
                sig_base64 = sig_payload
            sig_bytes = base64.b64decode(sig_base64)
            img_stream = io.BytesIO(sig_bytes)
            
            # Ancho estandar asumido de 600 puntos para Word
            pos = sig_item['position']
            width_pt = pos.get('w_pct', 0.25) * 600 
            
            paragraph = doc.add_paragraph()
            paragraph.alignment = 1  # Centrado
            run = paragraph.add_run()
            run.add_picture(img_stream, width=docx.shared.Pt(width_pt))
            
        doc.save(output_docx_path)
        return True
    except Exception as e:
        print(f"ERROR procesando DOCX: {e}")
        return False
