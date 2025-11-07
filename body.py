import cv2
import pyttsx3
import time
import os

engine = pyttsx3.init()

def speak(message):
    engine.say(message)
    engine.runAndWait()

os.makedirs("screenshots", exist_ok=True)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

last_speak_time = 0
speak_cooldown = 3
entry_count = 0
detected_ids = set() 

def main():
    global last_speak_time, entry_count
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ دریافت فریم انجام نشد.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        current_time = time.time()
        num_people = len(faces)

        if num_people > 0 and (current_time - last_speak_time > speak_cooldown):
            speak(f"{num_people} people detected")
            entry_count += num_people
            last_speak_time = current_time

            # ذخیره لاگ و اسکرین‌شات
            entry_time = time.strftime("%H-%M-%S", time.localtime())
            cv2.imwrite(f"screenshots/entry_{entry_time}.jpg", frame)
            with open("log.csv", "a", encoding="utf-8") as f:
                f.write(f"{num_people} people at {entry_time}\n")

        # نمایش چهره‌ها
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # نمایش اطلاعات روی تصویر
        cv2.putText(frame, f"People detected: {num_people}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        cv2.putText(frame, f"Total entries: {entry_count}", (20, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 200), 2)

        cv2.imshow("People Detection", frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()