#!/usr/bin/env python3
"""
ไฟล์ตัวอย่างสำหรับทดสอบ DOCX to PDF API
"""

import requests
import os
from pathlib import Path

# URL ของ API
API_URL = "http://localhost:8000"

def test_health_check():
    """ทดสอบ health check endpoint"""
    try:
        response = requests.get(f"{API_URL}/health")
        print(f"Health Check: {response.json()}")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print("❌ ไม่สามารถเชื่อมต่อกับ API ได้ กรุณาเริ่ม server ก่อน")
        return False

def test_convert_docx(docx_file_path: str):
    """ทดสอบการแปลงไฟล์ DOCX เป็น PDF"""
    if not os.path.exists(docx_file_path):
        print(f"❌ ไฟล์ {docx_file_path} ไม่พบ")
        return False
    
    try:
        with open(docx_file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(f"{API_URL}/convert", files=files)
            
        if response.status_code == 200:
            # บันทึกไฟล์ PDF
            output_filename = f"converted_{Path(docx_file_path).stem}.pdf"
            with open(output_filename, 'wb') as pdf_file:
                pdf_file.write(response.content)
            print(f"✅ แปลงไฟล์สำเร็จ! บันทึกเป็น: {output_filename}")
            return True
        else:
            print(f"❌ เกิดข้อผิดพลาด: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {str(e)}")
        return False

def test_cleanup():
    """ทดสอบการลบไฟล์ทั้งหมด"""
    try:
        response = requests.delete(f"{API_URL}/cleanup")
        print(f"Cleanup: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดในการ cleanup: {str(e)}")
        return False

def main():
    """ฟังก์ชันหลักสำหรับทดสอบ"""
    print("🚀 เริ่มทดสอบ DOCX to PDF API")
    print("=" * 50)
    
    # ทดสอบ health check
    print("1. ทดสอบ Health Check...")
    if not test_health_check():
        print("❌ กรุณาเริ่ม API server ก่อน: python main.py")
        return
    
    # ทดสอบการแปลงไฟล์ (ต้องมีไฟล์ DOCX สำหรับทดสอบ)
    print("\n2. ทดสอบการแปลงไฟล์...")
    docx_file = "example.docx"  # เปลี่ยนเป็นไฟล์ที่มีจริง
    
    if os.path.exists(docx_file):
        test_convert_docx(docx_file)
    else:
        print(f"⚠️  ไม่พบไฟล์ {docx_file} สำหรับทดสอบ")
        print("   กรุณาวางไฟล์ DOCX ชื่อ 'example.docx' ในโฟลเดอร์นี้")
    
    # ทดสอบ cleanup
    print("\n3. ทดสอบ Cleanup...")
    test_cleanup()
    
    print("\n✅ การทดสอบเสร็จสิ้น")

if __name__ == "__main__":
    main()