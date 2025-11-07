👁️ Real-Time Face Detection with Voice Alerts
A Python-based real-time face detection system using OpenCV and pyttsx3 that detects people through your webcam, announces detections with voice, captures screenshots, and logs activity automatically.

🚀 Features


🧠 Face detection using OpenCV’s Haar Cascade model


🔊 Voice feedback using pyttsx3 (text-to-speech engine)


📸 Automatic screenshots saved to a /screenshots folder


🧾 CSV logging of detections with timestamps


💡 On-screen display showing live count and total entries



🖥️ Demo
When you run the program:


The webcam feed opens in a new window.


Detected faces are highlighted with green rectangles.


The number of people detected is spoken aloud (e.g., “2 people detected”).


A screenshot and log entry are created every time people are detected.



🧩 Requirements
Make sure you have Python 3.8+ installed, then install the dependencies:
pip install opencv-python pyttsx3


⚙️ How to Run


Clone this repository:
git clone https://github.com/your-username/face-detection-voice.git
cd face-detection-voice



Run the script:
python main.py



Exit the program:


Press ESC to close the camera window and stop the script.





📂 Output Files


/screenshots/ → Stores captured frames when faces are detected


log.csv → Logs entries like:
2 people at 14-32-07
1 people at 14-36-45




🧠 How It Works


The program opens your webcam using cv2.VideoCapture(0).


Each frame is converted to grayscale for faster processing.


Haar Cascade (haarcascade_frontalface_default.xml) detects faces.


If one or more faces are detected:


The system speaks the count aloud.


A screenshot and log entry are saved.




Bounding boxes and live stats are displayed on the video feed.



⚠️ Notes


Works best in good lighting conditions.


Adjust detection sensitivity by tuning parameters in:
faces = face_cascade.detectMultiScale(gray, 1.1, 4)



Voice feedback has a cooldown of 3 seconds to avoid spam.



🧑‍💻 Author
Parham Sarkeshikian
