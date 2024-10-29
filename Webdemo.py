import streamlit as st
import requests
from PIL import Image
import io


API_URL = "http://127.0.0.1:5200/ocr/"

st.title("OCR API Demo")
st.write("Upload an image and get text extracted using OCR.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    if st.button("Process Image"):
        with st.spinner("Processing..."):
            uploaded_file.seek(0)
            files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            response = requests.post(API_URL, files=files)
            if response.status_code == 200:
                result = response.json()
                st.write("### OCR Result")
                st.write(result) 
            else:
                st.error(f"Error: {response.status_code}")
                st.write(response.text)
