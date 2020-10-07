from pspnet import PSPNet
from PIL import Image
import cv2
import time

# #def process(sourcepath, storepath, name):
#     pspnet = PSPNet()
    
#     img = sourcepath
#     image = Image.open(img)
#     print('Open Error! Try again!')
#     start = time.process_time()
#     #中间写上代码块 
#     r_image = pspnet.detect_image(image)
#     end = time.process_time()
#     print('Running time: %s Seconds'%(end-start))
    
#     cv2.imwrite(storepath+'\\'+name, r_image)
        
def predictMask(path):
    pspnet = PSPNet()
    image = Image.open(path)
    start = time.process_time()
    r_image = pspnet.detect_image(image)
    end = time.process_time()
    print('Running time: %s Seconds'%(end-start))
    r_image.save(path)
