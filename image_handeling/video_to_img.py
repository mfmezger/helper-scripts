from pathlib import Path

import cv2

name = "a27ce183-8fcc-4ce0-9fea-52b70a2b49e2.mp4"
vidcap = cv2.VideoCapture(name)
Path("output").mkdir(parents=True, exist_ok=True)
success, image = vidcap.read()
count = 0
n = name.split(".")[0]
if count < 50:
    while success:
        cv2.imwrite(f"output/{n}_{count}.jpg", image)  # save frame as JPEG file
        success, image = vidcap.read()
        print("Read a new frame: ", success)
        count += 1
