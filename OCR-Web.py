import easyocr as ocr  # OCR
import streamlit as st  # Web App
from PIL import Image  # Image Processing
import numpy as np  # Image Processing

st.title("Kanji Optical Character Recognition")

add_selectbox = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

image = st.file_uploader(label="Upload your Kanji Image file", type=['png', 'jpg', 'jpeg'])

@st.cache
def load_model():
    rdr = ocr.Reader(['ja', 'en'])
    return rdr

reader = load_model()  # load model

if image is not None:
    input_image = Image.open(image)  # read image

    with st.spinner("Processing ..."):
        result = reader.readtext(np.array(input_image))
        st.success("Results")
        for (bbox, text, prob) in result:
            st.write(text)
            
    st.success("Image")
    st.image(input_image)  # display image

    st.success("Done!")
else:
    st.write("Upload an Image")

