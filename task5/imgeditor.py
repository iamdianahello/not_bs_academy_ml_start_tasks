from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw, ImageFont
import cv2
import numpy as np

img = cv2.imread('squadron.jpeg',0)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imwrite('erosion.jpeg', erosion)

dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imwrite('dilation.jpeg', dilation)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imwrite('opening.jpeg', opening)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('closing.jpeg', closing)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imwrite('gradient.jpeg', gradient)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imwrite('tophat.jpeg', tophat)

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imwrite('blackhat.jpeg', blackhat)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
cv2.imwrite('laplacian.jpeg', laplacian)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
cv2.imwrite('sobelx.jpeg', sobelx)

image_with_text = Image.open('squadron.jpeg')
idraw = ImageDraw.Draw(image_with_text)
idraw.text((50, 50), 'test test test')
image_with_text.save('image_with_text.jpeg')

image_restangle = Image.open('squadron.jpeg')
idraw = ImageDraw.Draw(image_restangle)
idraw.rectangle((10, 90, 200, 200), fill='black')
image_restangle.save('image_restangle.jpeg')

image_180 = Image.open('squadron.jpeg')
rotated = image_180.rotate(180)
rotated.save('image_180.jpeg')

Image.open('squadron.jpeg').convert('CMYK').save('cmyk.tif')
