import threading
import cv2
from ultralytics import YOLO
import pandas















# Load the models
model1 = YOLO('yolov8n.pt')
filename = 1
video = cv2.VideoCapture(filename)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 750)
while True:
    ret, frame = video.read()  # Read the video frames

    # Exit the loop if no more frames in either video
    if not ret:
        break

    # Track objects in frames if available
    results = model1.track(frame, persist=True)

    '''
    for result in results:
        id = result.boxes
        print("ID PRINT")
        #print(id)
        print(result.probs)
    '''
    print(results[0].tojson())
    res_plotted = results[0].plot()

    #print(res_plotted)
    cv2.imshow(f"Tracking_Stream_{1}", res_plotted)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# Define the video files for the trackers
video_file1 = 2 # Path to video file, 0 for webcam, 1 for external camera
'''
# Create the tracker threads
tracker_thread1 = threading.Thread(target=run_tracker_in_thread, args=(video_file1, model1, 1), daemon=True)

# Start the tracker threads
tracker_thread1.start()

# Wait for the tracker threads to finish
tracker_thread1.join()
'''