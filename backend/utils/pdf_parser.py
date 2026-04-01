from pypdf import PdfReader
import io

def extract_pdf_text(file):
    contents = file.file.read()
    pdf_stream = io.BytesIO(contents)

    reader = PdfReader(pdf_stream)

    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text