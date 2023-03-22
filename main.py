import cv2
from ultralytics import YOLO
from tkinter import filedialog, Tk, Button, Label, Toplevel, Entry
import os
import sys

def browse_file():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("All files", "*.*"),))
    if filename:
        r1=model.predict(source=filename, show=True)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def open_camera():
    r2=model.predict(source=0, show=True)
    
def browse_url():
    url_window = Toplevel()
    url_window.title("Enter URL")
    url_window.geometry("300x100")

    # Input Field
    input_url = Entry(url_window, width=30)
    input_url.pack(pady=10)
    # Start Button
    url_button = Button(url_window, text="Start Inference", command=lambda: start_inference(input_url.get()))
    url_button.pack()

def start_inference(url):
    if url:
        r3=model.predict(source=url, show=True)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Create the GUI window
root = Tk()
root.title("Jeremy FYP")
root.geometry("300x180")

# Buttons
browse_button = Button(root, text="Browse", command=browse_file)
camera_button = Button(root, text="Camera", command=open_camera)
address_button = Button(root, text="Enter URL", command=browse_url)

# Buttons Arrangement
browse_button.pack(pady=10)
camera_button.pack(pady=10)
address_button.pack(pady=10)

# Load the model
model = YOLO(resource_path("jeremylite.pt"))

text_label = Label(root, text="STOP : Hold and Release Q at any instance")
text_label.place(relx=1.0, rely=0.9, anchor="se")

text_label = Label(root, text="EMAIL : jeremychoyjm@student.usm.my")
text_label.place(relx=1.0, rely=1.0, anchor="se")

root.mainloop()

