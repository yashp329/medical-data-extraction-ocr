<p align="center">
  <img src="Medical Data Extractor.png" alt="Medical Data Extraction Demo" width="700"/>
</p>

# 🏥 Medical Data Extraction using OCR & FastAPI

This project focuses on extracting **meaningful structured information** from medical documents such as **prescriptions** and **patient records**.  
The system leverages **OCR (pytesseract)** for text extraction, a **Python-based backend** for processing, and exposes functionality via a **FastAPI server**.  
The extracted data is tested, validated, and made ready for downstream applications such as hospital management, insurance claims, and research datasets.

---
## 📖 Project Overview  

- 📄 Handles medical documents like **prescriptions** and **patient details**.  
- 🔍 Extracts text using **pytesseract OCR**.  
- 🖥️ Backend & workflow built in **Python** with **OOP principles**.  
- ⚡ **FastAPI** used to serve REST APIs for extraction pipeline.  
- 🧪 **Pytest** implemented for unit testing of core functions.  
- 📬 **Postman** used for API testing and validation.  

---

## 🚀 Features  

- Preprocesses scanned documents for better OCR accuracy (noise removal, thresholding, resizing).  
- Extracts patient information, doctor details, medicines, and diagnoses.  
- Organizes output in **structured JSON/CSV** formats.  
- Modular design separating backend logic, API layer, and testing.  
- End-to-end tested workflow with **unit tests + API validation**.  

---

## 🛠️ Tools & Technologies  

- **Programming Language**: Python 3.x  
- **OCR Engine**: pytesseract  
- **Image Processing**: OpenCV  
- **Backend Framework**: FastAPI  
- **API Testing**: Postman  
- **Testing Framework**: Pytest  
- **Paradigm**: Object-Oriented Programming (OOP)  

---

## 📂 Project Structure  

