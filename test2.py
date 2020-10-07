import cv2
import os
from predictFun import predictMask 
from pspnet import PSPNet
from PIL import Image

predictMask('street.jpg')
print("yes")