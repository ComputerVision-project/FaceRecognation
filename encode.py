import os
import cv2
import face_recognition
import pickle

def find_encodings_in_video(video_path):
    cap = cv2.VideoCapture(video_path)
    encode_list = []
    frame_rate = 1
    frame_count = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame_count += 1
        if frame_count % (frame_rate * int(cap.get(cv2.CAP_PROP_FPS))) == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(frame)
            if face_locations:
                encode = face_recognition.face_encodings(frame, face_locations)[0]
                encode_list.append(encode)

    cap.release()
    return encode_list

def process_videos(folder_path):
    videos = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
    all_encodings = []
    student_ids = []

    if not videos:
        print("No video files found in the directory.")
        return all_encodings, student_ids

    for video in videos:
        video_path = os.path.join(folder_path, video)
        print(f"Processing video: {video_path}")
        encodings = find_encodings_in_video(video_path)
        if encodings:
            all_encodings.extend(encodings)
            student_id = os.path.splitext(video)[0]
            student_ids.extend([student_id] * len(encodings))
        else:
            print(f"No encodings found in {video}")

    return all_encodings, student_ids

video_folder_path = 'Datasets'
encodings, student_ids = process_videos(video_folder_path)

if encodings and student_ids:
    with open('Encodingfile.p', 'wb') as file:
        pickle.dump((encodings, student_ids), file)
    print("Encodingfile.p created successfully.")
else:
    print("No encodings or student IDs to save.")

