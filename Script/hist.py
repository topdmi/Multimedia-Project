#Script per calcolare l'istogramma di un'immagine 

import cv2
import numpy as np
from glob import glob
from matplotlib import pyplot as plt

img = cv2.imread('im1.png', -1) #insert image
#cv2.imshow('im25.png',img)

color = ('b','g','r')
for channel,col in enumerate(color):
    histr = cv2.calcHist([img],[channel],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title('Histogram for color scale picture')
plt.show()

'''
gray_img = cv2.imread('Jarvis26.png', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('im26.png',gray_img)

hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histogram for gray scale picture')
plt.show()
'''