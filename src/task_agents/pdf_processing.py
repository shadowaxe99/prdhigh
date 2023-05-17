```python
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_processing(task_data):
    task_type = task_data.get('task_type')
    file_path = task_data.get('file_path')

    if task_type == 'upload':
        return upload_pdf(file_path)
    else:
        return {"status": "error", "message": "Invalid task type for PDF processing"}

def upload_pdf(file_path):
    if not os.path.exists(file_path):
        return {"status": "error", "message": "File does not exist"}

    try:
        pdf = PdfFileReader(file_path)
        num_pages = pdf.getNumPages()
        document_info = pdf.getDocumentInfo()

        return {
            "status": "success",
            "message": "PDF uploaded successfully",
            "data": {
                "num_pages": num_pages,
                "title": document_info.title,
                "author": document_info.author,
                "subject": document_info.subject,
                "producer": document_info.producer,
                "created_date": document_info.created
            }
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
```