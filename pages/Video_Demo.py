import streamlit as st
from streamlit_webrtc import webrtc_streamer
import threading

st.set_page_config(page_title="Video Demo")

ctx = webrtc_streamer(key="example", media_stream_constraints={"video": True})
