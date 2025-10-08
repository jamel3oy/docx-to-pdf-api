from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import os
import tempfile
import shutil
from pathlib import Path
from docx2pdf import convert
import uuid
from typing import Optional

# Environment Configuration
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "uploads"))
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "outputs"))
API_TITLE = os.getenv("API_TITLE", "DOCX to PDF Converter")
API_DESCRIPTION = os.getenv("API_DESCRIPTION", "API สำหรับแปลงไฟล์ DOCX เป็น PDF")
API_VERSION = os.getenv("API_VERSION", "1.0.0")

app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION
)

# สร้างโฟลเดอร์สำหรับเก็บไฟล์ชั่วคราว
# UPLOAD_DIR = Path("uploads")
# OUTPUT_DIR = Path("outputs")

# สร้างโฟลเดอร์หากยังไม่มี
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

@app.get("/")
async def root():
    """หน้าแรกของ API"""
    return {
        "message": "DOCX to PDF Converter API",
        "endpoints": {
            "/convert": "POST - อัปโหลดไฟล์ DOCX และแปลงเป็น PDF",
            "/docs": "GET - เอกสาร API"
        }
    }

@app.post("/convert")
async def convert_docx_to_pdf(file: UploadFile = File(...)):
    """
    แปลงไฟล์ DOCX เป็น PDF
    
    Args:
        file: ไฟล์ DOCX ที่ต้องการแปลง
        
    Returns:
        FileResponse: ไฟล์ PDF ที่แปลงแล้ว
    """
    
    # ตรวจสอบประเภทไฟล์
    if not file.filename.lower().endswith('.docx'):
        raise HTTPException(
            status_code=400, 
            detail="กรุณาอัปโหลดไฟล์ .docx เท่านั้น"
        )
    
    # สร้าง unique filename
    file_id = str(uuid.uuid4())
    input_filename = f"{file_id}_{file.filename}"
    output_filename = f"{file_id}_{Path(file.filename).stem}.pdf"
    
    input_path = UPLOAD_DIR / input_filename
    output_path = OUTPUT_DIR / output_filename
    
    try:
        # บันทึกไฟล์ที่อัปโหลด
        with open(input_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # แปลงไฟล์ DOCX เป็น PDF
        convert(str(input_path), str(output_path))
        
        # ตรวจสอบว่าไฟล์ PDF ถูกสร้างสำเร็จ
        if not output_path.exists():
            raise HTTPException(
                status_code=500,
                detail="เกิดข้อผิดพลาดในการแปลงไฟล์"
            )
        
        # ส่งไฟล์ PDF กลับ
        return FileResponse(
            path=str(output_path),
            filename=f"{Path(file.filename).stem}.pdf",
            media_type="application/pdf"
        )
        
    except Exception as e:
        # ลบไฟล์ชั่วคราวหากเกิดข้อผิดพลาด
        if input_path.exists():
            input_path.unlink()
        if output_path.exists():
            output_path.unlink()
            
        raise HTTPException(
            status_code=500,
            detail=f"เกิดข้อผิดพลาดในการแปลงไฟล์: {str(e)}"
        )
    
    finally:
        # ลบไฟล์อินพุตหลังจากแปลงเสร็จ
        if input_path.exists():
            input_path.unlink()

@app.get("/health")
async def health_check():
    """ตรวจสอบสถานะของ API"""
    return {"status": "healthy", "message": "API ทำงานปกติ"}

@app.delete("/cleanup")
async def cleanup_files():
    """ลบไฟล์ทั้งหมดในโฟลเดอร์ uploads และ outputs"""
    try:
        # ลบไฟล์ในโฟลเดอร์ uploads
        for file_path in UPLOAD_DIR.glob("*"):
            if file_path.is_file():
                file_path.unlink()
        
        # ลบไฟล์ในโฟลเดอร์ outputs
        for file_path in OUTPUT_DIR.glob("*"):
            if file_path.is_file():
                file_path.unlink()
                
        return {"message": "ลบไฟล์ทั้งหมดเรียบร้อยแล้ว"}
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"เกิดข้อผิดพลาดในการลบไฟล์: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)