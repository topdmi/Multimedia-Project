#Script per stimare un'immagine attraverso metriche oggettive

from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import cv2
import math

def mse(imageA, imageB):
	MSE = np.mean((imageA - imageB) ** 2) 
	# return MSE
	return MSE

def psnr(imageA, imageB):
    MSE = np.mean((imageA - imageB) ** 2)
    if MSE == 0:
    	return 100
    PIXEL_MAX = 255.0
    # return PSNR
    return 20 * math.log10(PIXEL_MAX / math.sqrt(MSE))

def compare_images(imageA, imageB, title):
	
	m = mse(imageA, imageB)
	p = psnr(imageA, imageB)
	s = ssim(imageA, imageB, multichannel=True)

	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f,   PSNR: %.2f,   SSIM: %.2f" % (m, p, s))

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA)

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB)

	# show the images
	plt.show()

left = cv2.imread('im1.png') #insert image 
left = cv2.cvtColor(left, cv2.COLOR_BGR2RGB)

img_paths = glob('*.png')
count = 0 
for path in img_paths:
	text = "Test "
	text2 = "Original vs "
	count += 1
	right = cv2.imread(path)
	right = cv2.cvtColor(right, cv2.COLOR_BGR2RGB)
	title = (text + str(count) + ": " + text2 + path)
	# compare the images
	compare_images(left, right, title)

