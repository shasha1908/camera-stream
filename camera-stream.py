#python code to live stream using an Android phone, OpenCV and Python
#Author:Shashwat Bhatt

import requests
import cv2
import numpy as np

url = "http://192.168.0.2:8080/shot.jpg"

while True:

    img_response = requests.get(url)
    img_arr = np.array(bytearray(img_response.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)

    cv2.imshow("Android Camera", img)

    if cv2.waitKey(1) == 27:
        break