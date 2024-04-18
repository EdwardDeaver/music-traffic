import threading
import cv2
from ultralytics import YOLO
from threading import Thread
from time import sleep
import threading
import queue
import json

import pathlib
print(pathlib.Path(__file__).parent.resolve())

q = queue.Queue()


## Video by Mike Bird: https://www.pexels.com/video/different-kinds-of-vehicles-on-the-freeway-2053100/

## Create hashmap based on trackID as key value and then push the new values to that of the objects



## When playing notes take current notes and trackID == IntromentID and if current is not in new mute that one. 
def worker():

    IDObjects = {}
    print("WORKER")
    while True:
        item = q.get()
        item = json.loads(item)
        print("ITEM")
        print(item)
        for i in item:
            print( i["name"])
            IDObjects[str(i["track_id"])] = {"name": i["name"], "box": i["box"]}
        print("END ITEM")
        print(IDObjects)
        q.task_done()

















model1 = YOLO('yolov8n.pt')
#filename = str(pathlib.Path(__file__).parent.resolve())+ "/videos/2053100-hd_1280_720_60fps.mp4"
filename = 1
video = cv2.VideoCapture(filename)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 750)

threading.Thread(target=worker, daemon=True).start()

while True:
    ret, frame = video.read()  # Read the video frames

    # Exit the loop if no more frames in either video
    if not ret:
        break
    # Track objects in frames if available
    results = model1.track(frame, persist=True)
    print(results[0].tojson())
    if(len(results)>1):
        q.put(results[0].tojson())
    else:
        q.put(results[0].tojson())
    res_plotted = results[0].plot()


    #print(res_plotted)
    #cv2.imshow(f"Tracking_Stream_{1}", res_plotted)

    #key = cv2.waitKey(1)
    #if key == ord('q'):
    #   break
    #print(IDObjects.keys())


