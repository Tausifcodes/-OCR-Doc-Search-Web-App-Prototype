# OCR Web Application

This is a web-based prototype that demonstrates Optical Character Recognition (OCR) capabilities for extracting text from images in both Hindi and English. The application allows users to upload an image, processes it to extract text, and provides a search functionality to find specific keywords within the extracted text.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Application Locally](#running-the-application-locally)
- [Deployment](#deployment)
- [Usage](#usage)
- [Error Handling](#error-handling)

## Technologies Used
- **Python**: Programming language for backend logic.
- **Streamlit**: Framework for building web applications.
- **EasyOCR**: Library for optical character recognition.
- **Pillow (PIL)**: Image processing library.
- **NumPy**: Library for numerical operations.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

Create a Python virtual environment:

Ensure you have Python 3.7 or higher installed.
Use the following command to create a virtual environment:
python -m venv ocr-env

Activate the virtual environment:
.\ocr-env\Scripts\activate

Install required packages: Use pip to install the necessary libraries:
pip install streamlit easyocr pillow numpy

## Running the Application Locally

Running the Application Locally
Ensure that your virtual environment is activated.
Navigate to the directory containing the app.py file:
cd <path-to-your-app>

Run the Streamlit application:
streamlit run app.py

Open a web browser and go to http://localhost:8501 to access the application.

## Deployment     Live link :  https://ayhfa5nbvs6huvc4rsesme.streamlit.app/

To deploy the application, you can use platforms like Heroku, Streamlit Sharing, or any cloud service that supports Python web applications. Here's a brief overview of deploying to Streamlit Sharing:

Prepare your repository:

Ensure all your code is in a single GitHub repository.
Include a requirements.txt file with all your dependencies. You can generate it with:
pip freeze > requirements.txt

Deploy on Streamlit Sharing:

Go to Streamlit Sharing.
Sign in with your GitHub account and connect your repository.
Select the repository containing your application and deploy it.

Access your live app:

Once deployed, Streamlit Sharing will provide you with a live URL to access your application.

## Usage

Upload an Image: Click on the "Upload an Image" button and select an image containing Hindi or English text.
View Extracted Text: The application will display the extracted text from the uploaded image.
Search for Keywords: Enter a keyword in the search box to find its occurrence in the extracted text. The matched keywords will be highlighted.

## Error Handling
If you encounter any issues while running the application, check the following:

Ensure all dependencies are installed correctly.
If the OCR function throws an error related to easyocr, ensure that the easyocr package is correctly installed and imported.
For any runtime errors, check the console output for traceback information to identify the source of the error.

![Screenshot 2024-09-30 180909](https://github.com/user-attachments/assets/b56735d6-5b3b-4c06-83e6-2b6e2fa55cdb)

![Screenshot 2024-09-30 180838](https://github.com/user-attachments/assets/cf0a8426-6c04-46a0-b1e4-3046c6a03dba)

![Screenshot 2024-09-30 180815](https://github.com/user-attachments/assets/9f86984c-26f0-4b14-944e-885761083334)
