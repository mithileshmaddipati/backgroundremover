import streamlit as st
from rembg import remove
from PIL import Image


st.title("Image Masking AI Tool")

# File uploader widget
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Original Image", use_column_width=True)
    if st.button("Remove Background"):
        try:
            # Open the uploaded image
            image = Image.open(uploaded_file)
            # Remove background
            output = remove(image)
            # Display the processed image
            st.image(output, caption="Processed Image", use_column_width=True)

        except Exception as e:
            st.error(f"Error: {e}") 