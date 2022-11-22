import easyocr as ocr  # OCR
import streamlit as st  # Web App
from PIL import Image  # Image Processing
import numpy as np  # Image Processing

st.header("OCR - Optical Character Recognition")
st.caption("Created by the Okinawan Genealogical Society of Hawaii")
add_selectbox = st.selectbox('Select language in Image File',('Japanese', 'Portuguese', 'Spanish'))

lang = 'ja'
if (add_selectbox == 'Japanese'): 
    lang = 'ja'
elif (add_selectbox == 'Portuguese'): 
    lang = 'pt'
elif (add_selectbox == 'Spanish'): 
    lang = 'es'
    
image = st.file_uploader(label="Upload your Image File", type=['png', 'jpg', 'jpeg'])

@st.cache
def load_model():
    rdr = ocr.Reader([lang, 'en'])
    return rdr

reader = load_model()  

if image is not None:
    input_image = Image.open(image)  # read image

    with st.spinner("Processing ..."):
        result = reader.readtext(np.array(input_image))
        st.success("Results",icon="✅")
        for (bbox, text, prob) in result:
            st.write(text)
            
    st.success("Image File")
    st.image(input_image)           # display image

