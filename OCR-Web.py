import easyocr as ocr  # OCR
import streamlit as st  # Web App
from PIL import Image  # Image Processing
import numpy as np  # Image Processing
import cv2

col1, col2 = st.columns(2)

st.sidebar.header("Image to Text Conversion")
st.sidebar.caption("Created by the Okinawan Genealogical Society of Hawaii")
add_selectbox = st.sidebar.selectbox('Step 1: Select language in Image File',('Japanese', 'Portuguese', 'Spanish'))

#st.sidebar.header("")

lang = 'ja'
if (st.sidebar.add_selectbox == 'Japanese'): 
    lang = 'ja'
elif (st.sidebar.add_selectbox == 'Portuguese'): 
    lang = 'pt'
elif (st.sidebar.add_selectbox == 'Spanish'): 
    lang = 'es'
    
image = st.sidebar.file_uploader(label="Step 2: Upload your Image File", type=['png', 'jpg', 'jpeg'])

@st.cache
def load_model():
    rdr = ocr.Reader([lang, 'en'])
    return rdr

reader = load_model()  

if image is not None:
    input_image = Image.open(image)  # read image
    input_image = np.array(input_image)
    #st.sidebar.image(input_image)           # display image
    
    dimensions = input_image.shape
    fld = "Image Size " + str(dimensions)
    st.sidebar.write(fld)

    with st.spinner("Processing ..."):
        result = reader.readtext(input_image, width_ths=2, height_ths=0)
        cnt = 0
        tot = 0
        for (bbox, text, prob) in result:
            cnt = cnt + 1
            tot = tot + prob
        tot = tot / cnt   
        
        if (tot >= .75):
            col1.success("OCR Results", icon="👍")
        else:
            col1.success("OCR Results", icon="👎")
        cnt = 0
        for (bbox, text, prob) in result:
            cnt = cnt + 1
            fld =str(cnt) + ' ' + text
            col1.write(fld)
            (tl, tr, br, bl) = bbox
            tl = (int(tl[0]), int(tl[1]))
            tr = (int(tr[0]), int(tr[1]))
            br = (int(br[0]), int(br[1]))
            bl = (int(bl[0]), int(bl[1]))

            input_image = cv2.rectangle(input_image, tl, br, (0, 255, 0), 1)
            input_image = cv2.putText(input_image, str(cnt), tr, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
            
    col2.success("Processed Image File", icon="👇")

    col2.image(input_image)           # display image
