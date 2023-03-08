from PIL import Image
from io import BytesIO

import streamlit as st
import numpy as np
import base64
import requests

URL = "http://0.0.0.0:8000/letter-prediction/frame-sequence"


def make_prediction(img_file_buffer):
    img = Image.open(img_file_buffer)

    buffered = BytesIO()
    img.save(buffered, format="webp")

    # This is a hack
    img_str = f"data:image/webp;base64,{base64.b64encode(buffered.getvalue()).decode()}"

    response = requests.post(URL, json={"frames": [img_str]})
    response.raise_for_status()
    result = response.json()
    return result['prediction']
