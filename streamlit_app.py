import streamlit as st
from PIL import Image
import os

img_file_buffer = st.camera_input("Imagem enquadrando seu rosto")
if img_file_buffer:
    st.image(img_file_buffer)
    
