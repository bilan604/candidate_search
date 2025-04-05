import fitz  # PyMuPDF
import pytesseract
# This is where the tesseract.exe executable downloaded locally is
# must be done because it can't find it otherwise. Executable downloaded from online.
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\tesseract'

from PIL import Image


import os


def example():
    import fitz  # PyMuPDF
    import pytesseract
    # This is where the tesseract.exe executable downloaded locally is
    # must be done because it can't find it otherwise. Executable downloaded from online.
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\tesseract'

    from PIL import Image


    # Open the PDF file
    pdf_path = 'resumes/Caesar-工作3年-【脉脉招聘】.pdf'
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        
        # Convert the pixmap to an image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Perform OCR on the image
        text = pytesseract.image_to_string(img, lang='chi_sim')  # 'chi_sim' for Simplified Chinese
        print(text)


def extract_text_from_pdf(pdf_path: str) -> str:
    # Open the PDF file
    ### Add condition for mac?    
    
    pdf_document = fitz.open(pdf_path)

    # This is a list of pages, containing strings
    texts = []

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        
        # Convert the pixmap to an image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Perform OCR on the image
        text = pytesseract.image_to_string(img, lang='chi_sim')  # 'chi_sim' for Simplified Chinese
        texts.append(text)

    return "".join(texts)



