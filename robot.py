#import RPGPIO as gpio
import cognitive_face as MCF  # @Microsoft 认知服务
import requests
from PIL import Image,ImageMorph  # 图像处理
from picamera import PiCamera
camera = PiCamera()
# 初始化第三方库
Cj = ImageMorph.LutBuilder()
camera.capture('test.jpg')
camera.capture('test1.jpg')
Ae = ImageMorph.MorphOp.match(Cj,'test1.jpg')
print (Ae)
#key = input('Please enter your key')
#KEY = '%s' % key
#MCF.Key.set(KEY)
#BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
#MCF.BaseUrl.set(BASE_URL)
# Microsoft 认知服务初始化


#def facecdetect():
    #camera.resolution = (1024, 768)
    #camera.capture('test.jpg')
    #faces = MCF.face.detect('test.jpg')
    #rect = faces['faceRectangle']
    #left = rect['left']
    #top = rect['top']
    #bottom = left + rect['height']
    #right = top + rect['width']
    #return ((left, top), (bottom, right))


#while 0 == 0:
    #try:
        #ImageMorph.MorphOp.match(test.jpg)
    #finally:
        #pass
