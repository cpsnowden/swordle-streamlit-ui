import requests
import streamlit as st

st.set_page_config(page_title="Picture Demo")

# Env?
# URL = "http://0.0.0.0:8000/letter-prediction/frame"
URL = "https://sign-game-server-yckhsn477a-uc.a.run.app/letter-prediction/frame"

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    with st.spinner("Wait for it..."):
        ### Get bytes from the file buffer
        img_bytes = img_file_buffer.getvalue()

        ### Make request to  API (stream=True to stream response as bytes)
        res = requests.post(URL, files={'img': img_bytes})

        if res.status_code == 200:
            ### Display the image returned by the API
            prediction = res.json()['prediction']
            st.title(f"Predicted '{prediction.upper()}'")
        else:
            st.markdown("**Oops**, something went wrong 😓 Please try again.")
            print(res.status_code, res.content)
