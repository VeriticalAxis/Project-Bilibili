import cv2
import numpy as np
def play(path):
    #path = "D:\\8.11.mp4"
    mountains_video = cv2.VideoCapture(path)

    while True:
        ret, frame = mountains_video.read()
        if not ret:break
        cv2.imshow("frame", frame)
        key=cv2.waitKey(25)
        if key == 10 :
            
            break
    
    mountains_video.release()
    cv2.destroyAllWindows()
