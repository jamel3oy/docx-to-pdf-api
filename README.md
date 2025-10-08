# 📄➡️📋 DOCX to PDF Converter API

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A powerful and easy-to-use FastAPI application for converting DOCX documents to PDF format with a clean REST API interface.

## ✨ Features

- 🚀 **Fast & Efficient** - Built with FastAPI for high performance
- 📤 **Simple Upload** - Easy file upload via REST API
- 🔄 **Automatic Conversion** - Seamless DOCX to PDF conversion using docx2pdf
- 🛡️ **File Validation** - Built-in file type checking and error handling
- 🧹 **Auto Cleanup** - Automatic temporary file management
- 📊 **Health Monitoring** - Health check and cleanup endpoints
- 📚 **Auto Documentation** - Interactive API docs with Swagger UI
- 🐳 **Docker Ready** - Containerized for easy deployment

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Microsoft Word or LibreOffice Writer (for document conversion)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/docx-to-pdf-api.git
cd docx-to-pdf-api
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
python main.py
```

The API will be available at: **http://localhost:8000**

## 📖 API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API information and available endpoints |
| `POST` | `/convert` | Upload DOCX file and convert to PDF |
| `GET` | `/health` | Health check status |
| `DELETE` | `/cleanup` | Clean up temporary files |

### Convert DOCX to PDF

**POST** `/convert`

Upload a DOCX file and receive a PDF file in response.

**Request:**
- Content-Type: `multipart/form-data`
- Body: `file` (DOCX file)

**Response:**
- Content-Type: `application/pdf`
- Body: Converted PDF file

## 🧪 Testing

### Using cURL
```bash
# Convert a DOCX file
curl -X POST "http://localhost:8000/convert" \
     -H "accept: application/pdf" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@example.docx" \
     --output converted.pdf

# Health check
curl -X GET "http://localhost:8000/health"
```

### Using Python
```python
import requests

# Convert DOCX to PDF
with open('document.docx', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/convert', files=files)
    
    if response.status_code == 200:
        with open('converted.pdf', 'wb') as pdf_file:
            pdf_file.write(response.content)
        print("✅ Conversion successful!")
    else:
        print(f"❌ Error: {response.text}")
```

### Using the Test Script
```bash
python test_api.py
```

## 🐳 Docker Deployment

### Build and Run with Docker
```bash
# Build the image
docker build -t docx-to-pdf-api .

# Run the container
docker run -p 8000:8000 docx-to-pdf-api
```

### Using Docker Compose
```bash
docker-compose up -d
```

## 📁 Project Structure

```
docxtopdf/
├── 📄 main.py              # FastAPI application
├── 📋 requirements.txt     # Python dependencies
├── 📖 README.md           # Project documentation
├── 🧪 test_api.py         # API testing script
├── ⚙️  .gitignore          # Git ignore rules
├── 📦 Dockerfile          # Docker configuration
├── 🐳 docker-compose.yml  # Docker Compose setup
├── 📂 uploads/            # Temporary upload directory
├── 📂 outputs/            # Temporary output directory
└── 🐍 venv/              # Virtual environment
```

## 🛠️ Technology Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs
- **[docx2pdf](https://github.com/AlJohri/docx2pdf)** - DOCX to PDF conversion library
- **[Uvicorn](https://www.uvicorn.org/)** - Lightning-fast ASGI server
- **[Python 3.8+](https://www.python.org/)** - Programming language

## 🔧 Configuration

### Environment Variables

You can configure the application using environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` | Server host |
| `PORT` | `8000` | Server port |
| `UPLOAD_DIR` | `uploads` | Directory for uploaded files |
| `OUTPUT_DIR` | `outputs` | Directory for converted files |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues & Bug Reports

If you encounter any issues or bugs, please report them on the [Issues](https://github.com/yourusername/docx-to-pdf-api/issues) page.

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

## 📧 Contact

Your Name - [@yourusername](https://github.com/yourusername)

Project Link: [https://github.com/yourusername/docx-to-pdf-api](https://github.com/yourusername/docx-to-pdf-api)

---

<div align="center">
  <sub>Built with ❤️ using FastAPI</sub>
</div>