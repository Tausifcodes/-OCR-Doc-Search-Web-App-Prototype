import streamlit as st
from PIL import Image
import numpy as np
import re  # re module for regex operations
from ocr_utils import extract_text  

# Streamlit UI
st.title("OCR Application: Hindi and English Text Extraction")

# File uploader for image
uploaded_image = st.file_uploader("Upload an Image", type=['png', 'jpg', 'jpeg'])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Converting the image to a numpy array
    image_np = np.array(image)

    # Extracting and displaying the text
    extracted_text = extract_text(image_np)  # Calling the imported function
    st.write("**Extracted Text:**")
    
    # Search functionality
    search_term = st.text_input("Enter keyword to search:")
    
    if search_term:
        # Highlighting the search term in the extracted text using regex
        highlighted_text = re.sub(f"({re.escape(search_term)})", r"<mark>\1</mark>", extracted_text, flags=re.IGNORECASE)
        
        # Displaying the highlighted text
        st.markdown(highlighted_text, unsafe_allow_html=True)  # Use markdown to display highlighted text
        
        # Show success or error message
        if search_term.lower() in extracted_text.lower():
            st.success(f"'{search_term}' found in text!")
        else:
            st.error(f"'{search_term}' not found.")
    else:
        # Displaying the extracted text if no search term is entered
        st.write(extracted_text)
