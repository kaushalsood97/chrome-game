import cv2
import numpy as np
import pyscreenshot as imagegrab
from matplotlib import pyplot as plt
import time
from pykeyboard import PyKeyboard
last_time=time.time()


def keyinput():
	k=PyKeyboard()
	print('key down')
	k.press_key(' ')
	time.sleep(0.10)
	k.release_key(' ')
	print('key up')

def roi(img,vertices):
	mask=np.zeros_like(img)
	cv2.fillPoly(mask,vertices,255)
	masked=cv2.bitwise_and(img, mask)
	return masked

def template1(img):
	template = cv2.imread('images/3.png',0)
	w, h = template.shape[::-1]
	res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
    		cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		if(pt[0]<300):
					keyinput()
					break


def template2(img):
	template = cv2.imread('images/1.png',0)
	w, h = template.shape[::-1]
	res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
    		cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		if(pt[0]<300):
					keyinput()
					break

def template3(img):
	template = cv2.imread('images/2.png',0)
	w, h = template.shape[::-1]
	res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
    		cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		if(pt[0]<300):
					keyinput()
					break



def process_img(img):
	imgx=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	vertices=np.array([[50,300],[50,100],[500,100],[500,300]])
	imgx=roi(imgx,[vertices])
	template1(imgx)
	template2(imgx)
	template3(imgx)
	return imgx




time.sleep(2)
while True:
	img=np.array(imagegrab.grab(bbox=(10,40,600,400)))
	img=process_img(img)
	cv2.imshow('window',img)
	print('loop took {} seconds'.format(time.time()-last_time))
	last_time=time.time()
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break


destroyAllWindows()
