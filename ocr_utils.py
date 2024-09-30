import easyocr

def extract_text(image):
    # Initialize the reader for Hindi and English
    reader = easyocr.Reader(['en', 'hi'])
    # Perform OCR on the image
    results = reader.readtext(image, detail=0, paragraph=True)
    return " ".join(results)
