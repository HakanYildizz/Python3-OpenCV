"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu örneğimizde fotoğraftan yüz ve göz nasıl tanınır onu göreceğiz
Daha detaylı bilgi için siteye girebilirsiniz
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

face=cv2.CascadeClassifier("DataSet/haarcascade_frontalface_default.xml")
eye=cv2.CascadeClassifier("DataSet/haarcascade_eye.xml")
foto=cv2.imread("test.jpg")
gri=cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

faces=face.detectMultiScale(gri,1.3,5)

for(x,y,w,h) in faces:
	cv2.rectangle(foto,(x,y),(x+w,y+h),(255,0,0),2)
	gray=gri[y:y+h, x:x+w]
	color=foto[y:y+h, x:x+w]
	#bu işlemleri yüz bulmak için yaptık

	eyes=eye.detectMultiScale(gray)

	for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		#bu işlemi de göz bulmak iiçin yaptık

cv2.imshow("Yuz ve Goz Tanima",foto)
cv2.waitKey(0)
cv2.destroyAllWindows()
