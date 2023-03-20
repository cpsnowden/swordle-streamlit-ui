import requests
import streamlit as st
import os

st.set_page_config(page_title="Picture Demo", layout="wide")

DEFAULT_BACKEND_URL = "https://sign-game-server-yckhsn477a-uc.a.run.app"
BACKEND_URL = os.environ.get("BACKEND_URL", default=DEFAULT_BACKEND_URL)
BACKEND_API = f"{BACKEND_URL}/letter-prediction/frame"

col1, col2 = st.columns(2)
with col1:
    st.image(
        "https://adayinourshoes.com/wp-content/uploads/Sign-Language-Alphabet-PDF.png"
    )

with col2:
    img_file_buffer = st.camera_input("Take a photo of yourself making a sign")

    if img_file_buffer is not None:
        with st.spinner("Wait for it..."):
            ### Get bytes from the file buffer
            img_bytes = img_file_buffer.getvalue()

            ### Make request to  API
            print(f"Making request to {BACKEND_API}")
            res = requests.post(BACKEND_API, files={'img': img_bytes})

            if res.status_code == 200:
                json = res.json()

                prediction_status = json["predictionStatus"]
                if prediction_status == "success":
                    prediction = json['prediction']
                    st.text(f"Predicted '{prediction.upper()}'")
                elif prediction_status == "no_hand_detected":
                    st.text(
                        "Cound not detect hand, ensure your hand is in the picture"
                    )
            else:
                st.markdown(
                    "**Oops**, something went wrong 😓 Please try again.")
                print(res.status_code, res.content)
