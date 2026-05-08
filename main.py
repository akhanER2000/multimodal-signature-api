import os
import base64
import json
import tempfile
import traceback
from fastapi import FastAPI
from tools.pdf_injector import process_pdf_signature
from tools.docx_injector import process_docx_signature
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Firma Multimodal API")
TEMP_DIR = tempfile.gettempdir()

os.makedirs("frontend", exist_ok=True)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def read_root():
    return FileResponse("frontend/index.html")

@app.post("/api/sign")
async def sign_document(payload: dict):
    try:
        input_path = os.path.join(TEMP_DIR, "temp_input.json")
        with open(input_path, "w", encoding="utf-8") as f:
            json.dump(payload, f)

        mime = payload.get("document", {}).get("mime_type", "")
        fname = payload.get("document", {}).get("filename", "doc")
        out_path = os.path.join(TEMP_DIR, f"signed_{fname}")

        if "pdf" in mime:
            ok = process_pdf_signature(input_path, out_path)
        elif "doc" in mime or fname.endswith(".docx"):
            ok = process_docx_signature(input_path, out_path)
        else:
            return {"status":"error","message":"Formato no soportado","output_document":None,"error_details":mime}

        if not ok:
            return {"status":"error","message":"Error procesando firma","output_document":None,"error_details":"injector returned False"}

        with open(out_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")

        return {"status":"success","message":"Firma inyectada correctamente","output_document":{"filename":f"signed_{fname}","mime_type":mime,"content_base64":b64},"error_details":None}
    except Exception as e:
        traceback.print_exc()
        return {"status":"error","message":"Error interno","output_document":None,"error_details":str(e)}
