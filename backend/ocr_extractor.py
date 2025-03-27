import pytesseract
from pdf2image import convert_from_path

def extract_text_from_attachment(pdf_path):
    images = convert_from_path(pdf_path, poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin")
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text
if __name__ == "__main__":
    ans = extract_text_from_attachment("../data/attachments/hi.pdf")
    print(ans)
