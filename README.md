# Breast Cancer Detection Using VGG-16 AI Model

This repository hosts the project for the "Breast Cancer Detection Using VGG-16 AI Model" developed as part of the IS 6611 course on Applied Research in Business Analytics. Our team aimed to enhance the accuracy and efficiency of breast cancer detection in clinical settings using advanced machine learning techniques.

## Project Overview

### Introduction
This project focuses on developing a robust AI model to assist radiographers in detecting breast cancer more efficiently using mammographic images. The solution leverages the VGG-16 model known for its effective feature extraction capabilities in image processing.

### Problem Statement
Breast cancer remains a major global health issue. With the increasing number of cases and the high demand on radiographers, there's a critical need for more efficient diagnostic processes. Our project addresses this by implementing a model that reduces the radiographers' workload and potentially increases detection accuracy.

### Solution Approach
We selected the VGG-16 model for its proficiency in handling image data. The project includes a Streamlit application that demonstrates the model's real-time prediction capabilities, aiming to provide a practical tool for clinical use.

## Repository Contents

- `rsna-vgg16.ipynb`: Jupyter notebook detailing the VGG-16 model training and evaluation.
- `streamlit_app.py`: Streamlit application for demonstrating the model in action.
- `model_test.ipynb`: Notebook for additional tests on the model.
- `model_1_summary.txt`: Summary of the model's performance metrics.
- `Sample_Output.png`, `trained_model_output.png`: Visual outputs from the model.
- `config.json`: Configuration settings for model deployment.

## Technologies Used

- **Python**: For overall programming and model development.
- **TensorFlow and Keras**: For building and training the AI model.
- **Streamlit**: To create the interactive web application showcasing our model.
- **MLflow**: For tracking experiments to manage and compare models.
- **Docker**: Used for containerizing the application to ensure consistency across different platforms.

## Setup and Installation

To set up the project and run it locally, follow these steps:

1. **Clone the Repository**:
git clone https://github.com/zapod838/breast-cancer-detection-via-vgg16.git
cd breast-cancer-detection-via-vgg16

3. **Install Dependencies**:
Ensure that Python 3.8 or higher is installed on your machine. Then install the required Python packages:
pip install -r requirements.txt

5. **Run the Streamlit Application**:
Start the Streamlit web application by running: streamlit run streamlit_app.py

This will launch the Streamlit application in your default web browser, usually accessible via `http://localhost:8501`.

## How to Use

To use the Streamlit application for breast cancer detection:

1. **Navigate to the Application**:
Open your web browser and go to `http://localhost:8501` to view the application.

2. **Upload Images**:
Use the upload interface to select and upload mammographic images directly from your computer. The application accepts images in formats such as PNG or JPEG.

3. **View Predictions**:
Once the images are uploaded, the application will automatically process the images through the trained VGG-16 model. The predictions regarding the presence of cancerous features in the images will be displayed on the screen.

4. **Interact with Additional Features**:
Explore other functionalities provided by the application, such as adjusting model parameters or viewing different visualization layers of the model to understand how the model is interpreting the input images.

These instructions provide users with clear guidance on how to set up the project and effectively use the application to make breast cancer predictions using your AI model. Adjust the repository URL and any specific instructions according to your actual setup and application features.

## Contributors

- Eoin Holly
- Karan Shankar
- Manish Kamble
- Rashmi Singh
- Sanyam Singh Chauhan
- Shabbir Motorwala

## Acknowledgments

Acknowledgments to instructors, data sources, and any third-party code or tools used.

## License

Information on the repository licensing - typically how others can use the code or contribute to it.


## Next in the agenda.
- Test and finetune different models such as InceptionV3, EfficientNet and Vision Transformers (ViT)
- For application development: Frontend(Reactpy), backened(FastAPI)
- Implementing AWS, Google Cloud Platforms for hosting project

## Application UI
![image](https://github.com/zapod838/RSNA_BC_Detection/assets/45763055/9ac385e2-38a0-4d71-8996-ee50654438f8)

![image](https://github.com/zapod838/RSNA_BC_Detection/assets/45763055/95743ffe-f461-4f40-bbee-407081bf9839)

![image](https://github.com/zapod838/RSNA_BC_Detection/assets/45763055/2720d559-fd52-4092-ae18-17147ad2416d)

