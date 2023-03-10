import requests
import streamlit as st
import os

st.set_page_config(page_title="Picture Demo")

DEFAULT_BACKEND_URL = "https://sign-game-server-yckhsn477a-uc.a.run.app"
BACKEND_URL = os.environ.get("BACKEND_URL", default=DEFAULT_BACKEND_URL)
BACKEND_API = f"{BACKEND_URL}/letter-prediction/frame"

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    with st.spinner("Wait for it..."):
        ### Get bytes from the file buffer
        img_bytes = img_file_buffer.getvalue()

        ### Make request to  API (stream=True to stream response as bytes)
        print(f"Making request to {BACKEND_API}")
        res = requests.post(BACKEND_API, files={'img': img_bytes})

        if res.status_code == 200:
            ### Display the image returned by the API
            prediction = res.json()['prediction']
            st.title(f"Predicted '{prediction.upper()}'")
        else:
            st.markdown("**Oops**, something went wrong 😓 Please try again.")
            print(res.status_code, res.content)
