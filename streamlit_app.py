import streamlit as st
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from PIL import Image
import tensorflow as tf

# Load the saved model
model = tf.keras.models.load_model('RSNA_VGG16.h5')

# Function to preprocess uploaded images
def preprocess_image(image):
    img = load_img(image, target_size=(224, 224))
    img = img_to_array(img)
    img = preprocess_input(img)
    return img

# Function to normalize and display an image
def display_image(image):
    image = image - np.min(image)  # Translate the min value to zero
    image = image / np.max(image)  # Scale the values between 0 and 1
    return image

# Streamlit app
def main():
    st.title("RSNA Prediction App")

    # Create a folder to store uploaded images
    UPLOAD_FOLDER = 'uploaded_images'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Upload four images
    uploaded_files = st.file_uploader("Upload four images", accept_multiple_files=True)

    if uploaded_files and len(uploaded_files) == 4:
        images = [np.array(Image.open(uploaded_file)) for uploaded_file in uploaded_files]

        # Display the uploaded images
        st.write("Uploaded Images:")
        cols = st.columns(4)
        for i, col in enumerate(cols):
            with col:
                st.image(display_image(images[i]), use_column_width=True)


    if uploaded_files:
        if len(uploaded_files) == 4:
            # Save uploaded images to UPLOAD_FOLDER
            uploaded_paths = []
            for uploaded_file in uploaded_files:
                file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
                with open(file_path, 'wb') as f:
                    f.write(uploaded_file.getvalue())
                uploaded_paths.append(file_path)

            st.success("Images uploaded successfully!")

            # Path to the uploaded images folder
            test_folder = "uploaded_images"

            # Get test image paths
            test_image_paths = [os.path.join(test_folder, f) for f in os.listdir(test_folder)]

            # Function to generate test data
            def generate_test_data(test_image_paths):
                while True:
                    batch_images = [[] for _ in range(4)]  # Initialize lists for each of the four image inputs
                    for i, img_path in enumerate(test_image_paths):
                        img = load_img(img_path, target_size=(224, 224))
                        img = img_to_array(img)
                        img = preprocess_input(img)
                        batch_images[i % 4].append(img)  # Append each image to its respective list

                        if (i + 1) % 4 == 0:  # Yield batches of four images
                            batch_images = [np.stack(images) for images in batch_images]
                            batch_images = [tf.convert_to_tensor(images, dtype=tf.float32) for images in batch_images]
                            yield tuple(batch_images)  # Yield a tuple of four tensors
                            batch_images = [[] for _ in range(4)]  # Reset for the next batch

            # Create a generator for test data
            test_data_generator = generate_test_data(test_image_paths)

            # Make predictions for each batch
            for batch_images in test_data_generator:
                prediction = model.predict(batch_images)
                st.write("Prediction:", prediction)
                break  # Break out of the loop after making predictions once


        else:
            st.error("Please upload exactly four images.")

if __name__ == "__main__":
    main()
