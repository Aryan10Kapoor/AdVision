from flask import Flask, render_template, Response
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

app = Flask(__name__)

# ---------------- LOAD MODELS ----------------
age_model = load_model("age_model.h5")
gender_model = load_model("gender_model.h5")
emotion_model = load_model("emotion_model.h5")

# ---------------- FACE DETECTOR ----------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------------- LABELS ----------------
age_groups = ["0_2","4_6","8_13","15_20","20_30","35_45","48_55","60_100"]
emotion_labels = ["Angry","Disgust","Fear","Happy","Sad","Surprise","Neutral"]

# ---------------- ADS ----------------
ADS_PATH = "ads"
DEFAULT_AD = os.path.join(ADS_PATH, "default.jpg")
current_ad_path = DEFAULT_AD

camera = cv2.VideoCapture(0)

# ---------------- SELECT AD ----------------
def select_ad(age_idx, gender):
    ad_name = f"{gender.lower()}_{age_groups[age_idx]}.jpg"
    ad_path = os.path.join(ADS_PATH, ad_name)
    return ad_path if os.path.exists(ad_path) else DEFAULT_AD

# ---------------- VIDEO STREAM ----------------
def generate_video():
    global current_ad_path

    while True:
        success, frame = camera.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]

            # Age & Gender
            ag = cv2.resize(face, (128,128)) / 255.0
            ag = ag.reshape(1,128,128,3)

            age_idx = np.argmax(age_model.predict(ag, verbose=0))
            gender = "Male" if gender_model.predict(ag, verbose=0)[0][0] < 0.5 else "Female"

            # Emotion
            em = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            em = cv2.resize(em, (48,48)) / 255.0
            em = em.reshape(1,48,48,1)
            emotion = emotion_labels[np.argmax(emotion_model.predict(em, verbose=0))]

            # Draw info
            label = f"{gender}, {age_groups[age_idx]}, {emotion}"
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(frame, label, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

            # Update ad
            current_ad_path = select_ad(age_idx, gender)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# ---------------- ROUTES ----------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/ad_feed')
def ad_feed():
    with open(current_ad_path, 'rb') as f:
        return Response(
            f.read(),
            mimetype='image/jpeg',
            headers={"Cache-Control": "no-cache, no-store, must-revalidate"}
        )

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
