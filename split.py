import cv2
import os
from predictFun import predictMask 
from pspnet import PSPNet
from PIL import Image
pspnet = PSPNet()
#要提取视频的文件名，隐藏后缀
sourceFileName='test1'
#在这里把后缀接上
video_path = os.path.join("", "", sourceFileName+'.mp4')
times=0
#提取视频的频率，每25帧提取一个
frameFrequency = 200
#输出图片到当前目录vedio文件夹下
outPutDirName='vedio/'+sourceFileName+'/'
if not os.path.exists(outPutDirName):
    #如果文件目录不存在则创建目录
    os.makedirs(outPutDirName) 
camera = cv2.VideoCapture(video_path)
while True:
    times+=1
    res, image = camera.read()
    if not res:
        print('not res , not image')
        break
    if times%frameFrequency==0:
        #r_image = pspnet.detect_image(image) 
        path = outPutDirName + str(times)+'.jpg'
        cv2.imwrite(path, image)
        predictMask(path)
        
        print(path)

print('图片提取结束')
camera.release()
