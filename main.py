import streamlit as st
from PIL import Image
import numpy as np
import importlib.util
import os

# Function to load the extract_measurements function from extract_measurements.pyc
def load_extract_measurements():
    pyc_file = 'extract_measurements.pyc'
    spec = importlib.util.spec_from_file_location("extract_measurements", pyc_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.extract_measurements

extract_measurements = load_extract_measurements()

def main():
    st.title("Body Measurements Estimation")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    height = st.number_input("Enter your height in centimeters:", min_value=0)

    if uploaded_file is not None and height > 0:
        # Open the image file
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Convert image to the format required by the model
        image_np = np.array(image)

        # Process the image using your model
        measurements = extract_measurements(height, image_np)

        st.write("Estimated Body Measurements:")
        measurement_names = ["Height", "Waist", "Belly", "Chest", "Wrist", "Neck", "Arm Length", "Thigh", "Shoulder Width", "Hips", "Ankle"]
        for i, measurement in enumerate(measurements):
            st.write(f"{measurement_names[i]}: {measurement[0]:.2f} cm")

if __name__ == "__main__":
    main()
