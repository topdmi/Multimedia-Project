#Script per stimare un'immagine attraverso metriche soggettive

import numpy as np
import cv2 
from matplotlib import pyplot as plt
from glob import glob
from PIL import Image

def compare_images(imageA, imageB, title):

		# setup the figure
		fig = plt.figure(title)

		# show first image
		ax = fig.add_subplot(1, 2, 1)
		plt.imshow(imageA)

		# show the second image
		ax = fig.add_subplot(1, 2, 2)
		plt.imshow(imageB)

		# show the images
		plt.show()

# choose first image 
left = cv2.imread('im1.png') #insert image 
left = cv2.cvtColor(left, cv2.COLOR_BGR2RGB)

# choose path of second image 
img_paths = glob('*.png')
count = 0 
for path in img_paths:
	text = "Test "
	count += 1
	right = cv2.imread(path)
	right = cv2.cvtColor(right, cv2.COLOR_BGR2RGB)
	title = (text + str(count))
	# compare the images
	compare_images(left, right, title)

