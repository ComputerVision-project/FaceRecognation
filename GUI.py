import tkinter as tk
from tkinter import filedialog
import main

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if file_path:
        # Call a function from main to process the image
        main.process_image(file_path)

def open_webcam():
    # Call a function from main to start webcam processing
    main.process_camera()

def run_gui():
    root = tk.Tk()
    root.title("Face Recognition Attendance System")

    btn_open_image = tk.Button(root, text="Upload and Process Image", command=open_image)
    btn_open_image.pack(pady=10)

    btn_open_webcam = tk.Button(root, text="Start Webcam", command=open_webcam)
    btn_open_webcam.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
