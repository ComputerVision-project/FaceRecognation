import cv2
import pickle
import numpy as np
import face_recognition
import firebase_admin
from firebase_admin import credentials, db, storage
import os
import GUI
import csv
from datetime import datetime, timedelta

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://facerecognition-159b3-default-rtdb.firebaseio.com/",
        'storageBucket': "facerecognition-159b3.appspot.com"
    })

# Load the encoding file that has encodings and student IDs
with open('Encodingfile.p', 'rb') as file:
    encodelistknown, studIds = pickle.load(file)

# Function to resize an image
def resize_image(img, target_size):
    return cv2.resize(img, target_size)

# Process an uploaded image
def process_image(file_path):
    # Load the encoding file
    with open('Encodingfile.p', 'rb') as file:
        encodelistknown, studIds = pickle.load(file)

    # Read the image
    img = cv2.imread(file_path)
    img_small = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

    attendance_list = []

    # Detect faces and encode them
    face_locations = face_recognition.face_locations(img_small)
    encode_img = face_recognition.face_encodings(img_small, face_locations)

    for encodeface, faceloc in zip(encode_img, face_locations):
        matches = face_recognition.compare_faces(encodelistknown, encodeface)
        facedistance = face_recognition.face_distance(encodelistknown, encodeface)
        matchIndex = np.argmin(facedistance)

        if matches[matchIndex]:
            student_id = studIds[matchIndex]
            student_info = db.reference(f'Students/{student_id}').get()

            # Draw a rectangle around the face and write the name
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, student_info['name'], (x1, y2 + 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            # Add student info to the attendance list
            attendance_list.append([student_id, student_info['name'], student_info['email'], datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    # Write attendance to CSV file
    with open('attendance.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Email", "Date"])
        writer.writerows(attendance_list)

    # Display the image
    cv2.imshow("Processed Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_camera():
    bucket = storage.bucket()  # Reference to the storage service

    # Setup webcam
    video = cv2.VideoCapture(0)
    video.set(3, 765)
    video.set(4, 432)

    # Read the background image and mode images
    Background = cv2.imread('Resources/Background-01.png')
    folderMode = 'Resources/Modes'
    img_mode_path = os.listdir(folderMode)
    img_mode_list = [cv2.imread(os.path.join(folderMode, path)) for path in os.listdir(folderMode)]

    # Load the encoding file that has ids
    encodelistknown, studIds = pickle.load(open("Encodingfile.p", "rb"))

    modetype = 0
    counter = 0

    while True:
        is_capture, frame = video.read()
        if not is_capture:
            break

        frame_small = cv2.resize(frame, (765 ,432))
        frame_small = cv2.cvtColor(frame_small, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(frame_small)
        encode_frame = face_recognition.face_encodings(frame_small, face_locations)

        if not face_locations:
            modetype = 0

        Background[200:200 + 432, 55:55 + 765] = frame_small
        Background[140:140 + 420, 970:970 + 230] = img_mode_list[modetype]


        for encodeface, faceloc in zip(encode_frame, face_locations):
            matches = face_recognition.compare_faces(encodelistknown, encodeface)
            face_distance = face_recognition.face_distance(encodelistknown, encodeface)
            match_index = np.argmin(face_distance)

            if matches[match_index]:
                student_id = studIds[match_index]
                student_info = db.reference(f'Students/{student_id}').get()

                if student_info:
                    y1, x2, y2, x1 = faceloc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, student_info['name'], (x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
                    modetype = 1
                    # Retrieve student's image from Firebase Storage
                    blob = bucket.blob(f'Datasets/{student_id}.png')
                    img_data = blob.download_as_string()
                    img_array = np.frombuffer(img_data, np.uint8)
                    imgStudent = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgStudent = resize_image(imgStudent, (200, 200))

                    # Place student's image and details on the Background
                    Background[140:140 + 200, 982:982 + 200] = imgStudent
                    cv2.putText(Background, student_info['name'], (1046, 440),
                                cv2.FONT_HERSHEY_COMPLEX, 0.3, (255, 0, 0), 1)
                    cv2.putText(Background, student_info['id'], (1050, 517),
                                cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 0, 0), 1)

                    # Change the mode based on the recognized face
                    counter += 1

        cv2.imshow("Attendance system", Background)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    GUI.run_gui()  # Start the GUI

