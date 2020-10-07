#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from pspnet import PSPNet
from PIL import Image

import time
pspnet = PSPNet()

while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
       
        start = time.process_time()
        #中间写上代码块 
        r_image = pspnet.detect_image(image)
        end = time.process_time()
        print('Running time: %s Seconds'%(end-start))
       
        r_image.show()
