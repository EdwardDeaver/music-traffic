import cv2
from ultralytics import YOLO
import json

import pathlib
print(pathlib.Path(__file__).parent.resolve())
import time

import rtmidi
import time
import multiprocessing as mp


import pika

import random
import socket
from websockets.sync.client import connect


import receive
import asyncio




## Video by Mike Bird: https://www.pexels.com/video/different-kinds-of-vehicles-on-the-freeway-2053100/

## Create hashmap based on trackID as key value and then push the new values to that of the objects

import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)

import threading
import queue

q = queue.Queue()

def worker():
    while True:
        asyncio.run(receive.main())





def myModelControl():
    with connect("ws://localhost:8767") as websocket:

        model1 = YOLO('yolov8n.pt')
        filename = str(pathlib.Path(__file__).parent.resolve())+ "/videos/2053100-hd_1280_720_60fps.mp4"
        #filename = 1
        video = cv2.VideoCapture(filename)
        video.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
        video.set(cv2.CAP_PROP_FRAME_HEIGHT, 750)

        #threading.Thread(target=worker, daemon=True).start()
        #threading.Thread(target=test, args=(arg1,), kwargs={'arg2':arg2}).start()

        while True:
            ret, frame = video.read()  # Read the video frames

            # Exit the loop if no more frames in either video
            if not ret:
                break
            # Track objects in frames if available
            results = model1.track(frame, conf=0.4, tracker="bytetrack.yaml", persist=True)
  
            #print(results[0].tojson())
            if(len(results)>1):
                #print(results[0].tojson())
                q.put(results[0].tojson())
                #channel.basic_publish(exchange='', routing_key='hello', body=results[0].tojson())
                #message, address = server_socket.recvfrom(1024)
                #server_socket.sendto(results[0].tojson(), address)
                #print(" [x] Sent 'Hello World!'")
                websocket.send(results[0].tojson())

            else:
                #print(results[0].tojson())

                if(len(results[0])>0):
                    q.put(results[0].tojson())
                #channel.basic_publish(exchange='', routing_key='hello', body=results[0].tojson())
                #message, address = server_socket.recvfrom(1024)
                #server_socket.sendto(results[0].tojson(), address)
                #print(" [x] Sent 'Hello World!'")
                    websocket.send(results[0].tojson())


            res_plotted = results[0].plot()


            #print(res_plotted)
            #cv2.imshow(f"Tracking_Stream_{1}", res_plotted)

            #key = cv2.waitKey(1)
            #if key == ord('q'):
            #   break
            #print(IDObjects.keys())
if __name__ == '__main__':
    print('Starting video stream')
    worker_process = mp.Process(target=worker, args=())
    worker_process.start()
    time.sleep(10)
    capture_process = mp.Process(target=myModelControl, args=())
    capture_process.start()



'''
import cv2
from ultralytics import YOLO
import json

import pathlib
print(pathlib.Path(__file__).parent.resolve())
import time

import rtmidi
import time
import multiprocessing as mp



import asyncio


from websockets.sync.client import connect







## Video by Mike Bird: https://www.pexels.com/video/different-kinds-of-vehicles-on-the-freeway-2053100/

## Create hashmap based on trackID as key value and then push the new values to that of the objects














async def myModelControl():
    with connect("ws://localhost:8765") as websocket:
        model1 = YOLO('yolov8n.pt')
        filename = str(pathlib.Path(__file__).parent.resolve())+ "/videos/2053100-hd_1280_720_60fps.mp4"
        #filename = 1
        video = cv2.VideoCapture(filename)
        video.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
        video.set(cv2.CAP_PROP_FRAME_HEIGHT, 750)

        #threading.Thread(target=worker, daemon=True).start()
        #threading.Thread(target=test, args=(arg1,), kwargs={'arg2':arg2}).start()

        while True:
            ret, frame = video.read()  # Read the video frames

            # Exit the loop if no more frames in either video
            if not ret:
                break
            # Track objects in frames if available
            results = model1.track(frame, persist=True)
            #print(results[0].tojson())
            if(len(results)>1):
                #q.put(results[0].tojson())
                #message, address = server_socket.recvfrom(1024)
                #server_socket.sendto(results[0].tojson(), address)
                websocket.send("Hello world!")

            else:
                #q.put(results[0].tojson())
                #message, address = server_socket.recvfrom(1024)
                #server_socket.sendto(results[0].tojson(), address)
                websocket.send(results[0].tojson())


            res_plotted = results[0].plot()


            #print(res_plotted)
            #cv2.imshow(f"Tracking_Stream_{1}", res_plotted)

            #key = cv2.waitKey(1)
            #if key == ord('q'):
            #   break
            #print(IDObjects.keys())
if __name__ == '__main__':
    print('Starting video stream')
    asyncio.run(myModelControl())



'''