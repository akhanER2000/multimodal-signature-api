# tools/handshake.py
import sys

def verify_link():
    print("Iniciando Protocolo de Verificación (Handshake)...")
    try:
        import fitz  # Importando PyMuPDF
        print("[OK] PyMuPDF (fitz) cargado correctamente.")
        
        import docx  # Importando python-docx
        print("[OK] python-docx cargado correctamente.")
        
        print("\nSTATUS: LINK ESTABLECIDO. El entorno está listo para la Fase 3.")
    except ImportError as e:
        print(f"\n[ERROR] FATAL ERROR: Fallo en el Handshake. No se pudo cargar una dependencia.")
        print(f"Detalles: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verify_link()
