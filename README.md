# AdVision

# 🎯 Real-Time Targeted Advertisement System  
### Using Age, Gender & Emotion Detection

---

## 📌 Project Overview
This project is a **real-time targeted advertisement system** that analyzes a user’s **age, gender, and emotion** from a live camera feed and displays **relevant advertisements** accordingly.

The system uses **deep learning models** trained on facial image datasets and integrates them into a **web-based application**.

---

## 🚀 Features
- Real-time **face detection** using webcam  
- **Age group prediction**  
- **Gender classification**  
- **Emotion recognition**  
- Dynamic **targeted advertisement display**  
- Web-based interface with:
  - Camera feed on the **left**
  - Advertisement panel on the **right**

---

## 🧠 Technologies Used
- Python  
- TensorFlow / Keras  
- OpenCV  
- Flask  
- HTML & CSS  
- Jupyter Notebook  

---

## 📂 Project Structure

```text
project/
│
├── notebooks/
│   ├── age_model_training.ipynb
│   ├── gender_model_training.ipynb
│   └── emotion_model_training.ipynb
│
├── app.py
│
├── ads/
│   ├── male_20_30.jpg
│   ├── female_25_32.jpg
│   └── default.jpg
│
├── templates/
│   └── index.html
│
└── README.md
```
---

📊 Datasets Used

UTKFace Dataset – for age and gender prediction
FER2013 Dataset – for emotion recognition

Note: Due to size limitations, datasets are not included in this repository.

---

🧪 Model Training

The deep learning models were trained using Jupyter Notebook (.ipynb) files.

Each notebook contains:
- Data loading
- Image preprocessing
- Model architecture
- Training and evaluation

Note: Trained .h5 model files are not uploaded due to GitHub file size restrictions.

---

▶️ How to Run the Application

1️⃣ Install dependencies
pip install flask opencv-python tensorflow numpy

2️⃣ Run the web application
python app.py

3️⃣ Open in browser
http://127.0.0.1:5000

---

🎯 Advertisement Logic

Ads are selected based on:
- Age group
- Gender
- Emotion

Examples:
Male, Age 20–30, Happy → Fitness / Lifestyle Ads
Female, Age 25–32, Sad → Entertainment / Wellness Ads

---

🔒 Privacy & Ethics
- No data is stored
- Processing is real time
- Educational use only

🎓 Academic Use
- Computer Vision
- Deep Learning
- Real-Time Systems
- Recommendation Concepts
  
---

✨ Future Enhancements
- Cloud deployment
- Multiple face support
- Better ad logic
