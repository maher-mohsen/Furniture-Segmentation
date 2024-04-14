import streamlit as st
import torch
from PIL import Image
import numpy as np
from ultralytics import YOLO
import os
# Load YOLOv8 model
# Make sure to replace 'yolov8' with the specific model if you're using a different variant
def load_image(image_file):
    img = Image.open(image_file)
    return img

HOME = os.getcwd()
model = YOLO(f"{HOME}/yolov8x-seg.pt")


def inference(img):
    results = model.predict(source=img, conf=0.25)
    im_array = results[0].plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    print(type(im))
    return im




st.set_page_config(page_title="Furniture Segmentation App", page_icon=":camera:")
st.title("Welcome to Furniture Segmentation App")
st.markdown("""
Gradio demo for [Furniture Seg](https://github.com/maher-mohsen/Furniture-Segmentation)
 To use it, simply upload your image

""")

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
st.markdown(
        """
        #### By Eng.Maher Mohsen
        
        """
    )
if image_file is not None:
    image = load_image(image_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    output_image = inference(image)
    st.image(output_image, use_column_width=True)
