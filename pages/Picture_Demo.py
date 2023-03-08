from api import make_prediction

import streamlit as st

st.set_page_config(page_title="Picture Demo")

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    prediction = make_prediction(img_file_buffer)
    st.title(f"Predicted '{prediction.upper()}'")
