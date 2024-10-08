# Breast Cancer Detection Using VGG-16 AI Model

## Project Overview

### Introduction
This project focuses on developing a robust AI model to assist radiographers in detecting breast cancer more efficiently using mammographic images. The solution leverages the VGG-16 model known for its effective feature extraction capabilities in image processing.

### Problem Statement
Breast cancer remains a major global health issue. With the increasing number of cases and the high demand on radiographers, there's a critical need for more efficient diagnostic processes. Our project addresses this by implementing a model that reduces the radiographers' workload and potentially increases detection accuracy.

### Solution Approach
We selected the VGG-16 model for its proficiency in handling image data. The project includes a Streamlit application that demonstrates the model's real-time prediction capabilities, aiming to provide a practical tool for clinical use.

![VGG16](https://github.com/user-attachments/assets/c4829ab3-15c0-4d27-a44e-dcb9fb52759f)


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
```bash
git clone https://github.com/zapod838/breast-cancer-detection-via-vgg16.git
cd breast-cancer-detection-via-vgg16
```
2. **Install Dependencies**:
Ensure that Python 3.8 or higher is installed on your machine. Then install the required Python packages:
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit Application**:
Start the Streamlit web application by running:
```bash
streamlit run streamlit_app.py
```
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

## Application UI

### Features:
- **Model Selection**: Users can choose which model's information to display, providing flexibility and insights into different model performances.
- **Real-Time Prediction**: The application processes uploaded mammographic images in real-time, displaying predictions on the likelihood of breast cancer presence.

## Future Development Plans

As we continue to improve and expand our breast cancer detection application, our agenda includes the following milestones:

- **Model Enhancement**: Test and fine-tune advanced models including InceptionV3, EfficientNet, and Vision Transformers (ViT) to improve accuracy and efficiency.

- **Application Development**: Expand the front-end using ReactPy to enhance user interaction. Develop a more robust back-end using FastAPI to handle requests more efficiently.

- **Cloud Implementation**: Implement the application on cloud platforms such as AWS and Google Cloud to ensure scalability and accessibility.

These steps are aimed at refining our application to meet the needs of clinical settings more effectively and to ensure it remains at the cutting edge of technology.

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
