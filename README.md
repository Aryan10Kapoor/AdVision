# AdVision

🎯 Real-Time Targeted Advertisement System
Using Age, Gender & Emotion Detection
📌 Project Overview

This project is a real-time targeted advertisement system that analyzes a user’s age, gender, and emotion from a live camera feed and displays relevant advertisements accordingly.

The system uses deep learning models trained on face images and integrates them into a web-based application.

🚀 Features

Real-time face detection using webcam

Age group prediction

Gender classification

Emotion recognition

Dynamic targeted advertisement display

Web-based interface with:

Camera feed on the left

Advertisement panel on the right

🧠 Technologies Used

Python

TensorFlow / Keras

OpenCV

Flask (for web application)

HTML & CSS

Jupyter Notebook

📂 Project Structure
project/
│
├── notebooks/
│   ├── age_model_training.ipynb
│   ├── gender_model_training.ipynb
│   ├── emotion_model_training.ipynb
│
├── app.py
├── ads/
│   ├── male_20_30.jpg
│   ├── female_25_32.jpg
│   ├── default.jpg
│
├── templates/
│   └── index.html
│
└── README.md

📊 Datasets Used

UTKFace Dataset – for age and gender prediction

FER2013 Dataset – for emotion recognition

Note: Due to size limitations, datasets are not included in this repository.

🧪 Model Training

The deep learning models were trained using Jupyter Notebook (.ipynb) files, which are included in this repository.

Each notebook contains:

Data loading

Preprocessing

Model architecture

Training process

Evaluation

Trained .h5 model files are not uploaded due to GitHub file size restrictions.

▶️ How to Run the Application
1️⃣ Install dependencies
pip install flask opencv-python tensorflow numpy

2️⃣ Run the web application
python app.py

3️⃣ Open in browser
http://127.0.0.1:5000

🎯 Advertisement Logic

Advertisements are selected using rule-based logic based on:

Predicted age group

Predicted gender

Predicted emotion

Example:

Male, Age 20–30, Happy → Fitness / Lifestyle Ads

Female, Age 25–32, Sad → Entertainment / Wellness Ads

🔒 Privacy & Ethics

No images or video data are stored

Processing happens in real time

The system is intended for educational purposes only

🎓 Academic Use

This project was developed as part of an academic / college project to demonstrate:

Computer vision

Deep learning

Real-time systems

Personalized recommendation concepts

✨ Future Enhancements

Deploy on cloud

Add multiple face support

Improve ad recommendation logic

Store analytics dashboards

Replace rule-based ads with ML-based recommendation
