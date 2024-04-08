import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance


def blur_image(image, blur):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(gray_image, (blur, blur), 0)
    return blurred_image



def image_uploader(img):
    try:
        pilimage = Image.open(img)
        st.text("Original Image")
        return st.image(pilimage)
    except:
        return None

def convert_rgb(imag):
    return pilimage.convert('RGB')
st.write('Image Processing App')
image_file = st.file_uploader("Upload Image", type=['jpeg', 'png', 'jpeg'])

pilimage = image_uploader(image_file)

if image_file is not None:
    enhance_type = st.sidebar.selectbox('Enhance Type', ['Original', 'Gray-Scale', 'Contrast', 'Blur'])
    if enhance_type == "Gray-Scale":
        if st.button('Process'):
            pilimage = Image.open(image_file)
            our_img = np.array(convert_rgb(pilimage))
            img1 = cv2.cvtColor(our_img, 1)
            gray_image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            st.write('Gray-Scale Image')
            st.image(gray_image)
    elif enhance_type == 'Contrast':
        c_rate = st.sidebar.slider('Contrast', 1, 10)
        if st.button('Process'):
            image = Image.open(image_file)
            enhance = ImageEnhance.Contrast(image)
            img_output = enhance.enhance(c_rate)
            st.image(img_output)
    elif enhance_type == 'Blur':
        b_rate = st.sidebar.slider('Blur', 1, 11, step = 2)
        if st.button('Process'):
            pilimage = Image.open(image_file)
            our_img = np.array(convert_rgb(pilimage))
            blur_img = blur_image(our_img, b_rate)
            st.write('Blurred Image')
            st.image(blur_img, caption=f'Blurred Image (Blur Radius: {b_rate})', use_column_width=True)

            




