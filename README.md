# DOCX to PDF Converter API

FastAPI application สำหรับแปลงไฟล์ DOCX เป็น PDF

## Features

- ✅ Upload ไฟล์ DOCX และแปลงเป็น PDF
- ✅ ตรวจสอบประเภทไฟล์
- ✅ สร้าง unique filename เพื่อป้องกันการชนกัน
- ✅ ลบไฟล์ชั่วคราวอัตโนมัติ
- ✅ Error handling ที่ครบถ้วน
- ✅ Health check endpoint
- ✅ Cleanup endpoint สำหรับลบไฟล์ทั้งหมด

## Installation

1. สร้าง virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# หรือ
venv\Scripts\activate     # Windows
```

2. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. เริ่มต้น server:
```bash
python main.py
```
หรือ
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. เปิดเบราว์เซอร์ไปที่: http://localhost:8000

## API Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: GET
- **Description**: ข้อมูลพื้นฐานของ API

### 2. Convert DOCX to PDF
- **URL**: `/convert`
- **Method**: POST
- **Description**: อัปโหลดไฟล์ DOCX และแปลงเป็น PDF
- **Parameters**: 
  - `file`: ไฟล์ DOCX (multipart/form-data)
- **Response**: ไฟล์ PDF ที่แปลงแล้ว

### 3. Health Check
- **URL**: `/health`
- **Method**: GET
- **Description**: ตรวจสอบสถานะของ API

### 4. Cleanup Files
- **URL**: `/cleanup`
- **Method**: DELETE
- **Description**: ลบไฟล์ทั้งหมดในโฟลเดอร์ uploads และ outputs

## การทดสอบด้วย curl

```bash
# อัปโหลดและแปลงไฟล์
curl -X POST "http://localhost:8000/convert" \
     -H "accept: application/pdf" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@example.docx" \
     --output converted.pdf

# ตรวจสอบสถานะ
curl -X GET "http://localhost:8000/health"

# ลบไฟล์ทั้งหมด
curl -X DELETE "http://localhost:8000/cleanup"
```

## การทดสอบด้วย Python

```python
import requests

# อัปโหลดและแปลงไฟล์
with open('example.docx', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/convert', files=files)
    
    if response.status_code == 200:
        # บันทึกไฟล์ PDF
        with open('converted.pdf', 'wb') as pdf_file:
            pdf_file.write(response.content)
        print("แปลงไฟล์สำเร็จ!")
    else:
        print(f"เกิดข้อผิดพลาด: {response.text}")
```

## API Documentation

เมื่อ server ทำงานแล้ว สามารถดู API documentation ได้ที่:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## โครงสร้างโปรเจค

```
docxtopdf/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── README.md           # เอกสารนี้
├── uploads/            # โฟลเดอร์สำหรับไฟล์ที่อัปโหลด (ชั่วคราว)
├── outputs/            # โฟลเดอร์สำหรับไฟล์ PDF ที่แปลงแล้ว (ชั่วคราว)
└── venv/              # Virtual environment
```

## ข้อกำหนดระบบ

- Python 3.7+
- Microsoft Word หรือ LibreOffice Writer (สำหรับการแปลงไฟล์)

## หมายเหตุ

- ไฟล์ที่อัปโหลดจะถูกลบทิ้งอัตโนมัติหลังจากการแปลง
- รองรับเฉพาะไฟล์ .docx เท่านั้น
- ไฟล์ PDF ที่แปลงแล้วจะถูกส่งกลับทันทีและถูกลบออกจาก server