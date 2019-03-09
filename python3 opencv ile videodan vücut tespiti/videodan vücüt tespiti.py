"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu örneğimizde videodan vücut tespiti nasıl yapılır onu göreceğiz
Daha detaylı bilgi için siteye girebilirsiniz
"""
import cv2
import numpy as np

cam=cv2.VideoCapture("video.mp4")	#burada videoyu seçtik(aynı path üzerinde olmalı)
insan_cascade=cv2.CascadeClassifier("haarcascade_fullbody.xml")

while True:
	_,cerceve=cam.read()
	gri=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
	insan=insan_cascade.detectMultiScale(gri,1.1,3)
	#burada skala ve çerçeveyi ayarladık(buradaki "1.1,3" değerlerini videoya göre değiştirebilirsiniz)

	for(x,y,w,h) in insan:
		cv2.rectangle(cerceve,(x,y),(x+w,y+h),(0,0,255),2)	#burada vücudu bulduk
	cv2.imshow('insanlar',cerceve)
	if cv2.waitKey(25) & 0xFF==ord('q'):	#kameradan çıkış yapmamız için 'q'a basmalıyız
		break

cam.release()
cv2.destroyAllWindows()