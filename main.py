import os
import base64
import json
import tempfile
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tools.pdf_injector import process_pdf_signature
from tools.docx_injector import process_docx_signature
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Firma Multimodal API")

# Directorio temporal seguro para Vercel (/tmp)
TEMP_DIR = tempfile.gettempdir()

os.makedirs("frontend", exist_ok=True)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def read_root():
    return FileResponse("frontend/index.html")

@app.post("/api/sign")
async def sign_document(payload: dict):
    input_path = os.path.join(TEMP_DIR, "temp_input.json")
    
    with open(input_path, "w") as f:
        json.dump(payload, f)
        
    mime_type = payload.get("document", {}).get("mime_type", "")
    filename = payload.get("document", {}).get("filename", "signed_doc")
    
    out_path = os.path.join(TEMP_DIR, f"signed_{filename}")
    
    if "pdf" in mime_type:
        success = process_pdf_signature(input_path, out_path)
    elif "wordprocessingml" in mime_type or "doc" in mime_type:
        success = process_docx_signature(input_path, out_path)
    else:
        raise HTTPException(status_code=400, detail="Formato no soportado.")
        
    if not success:
        raise HTTPException(status_code=500, detail="Error interno procesando firma.")
        
    with open(out_path, "rb") as f:
        b64_output = base64.b64encode(f.read()).decode("utf-8")
        
    return {
        "status": "success",
        "output_document": {
            "filename": f"signed_{filename}",
            "mime_type": mime_type,
            "content_base64": b64_output
        }
    }
