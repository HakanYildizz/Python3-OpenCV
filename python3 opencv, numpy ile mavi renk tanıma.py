"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu örneğimizde kamerada mavi renk nasıl tanınır onu göreceğiz
Daha detaylı bilgi için siteye girebilirsiniz
"""
import cv2
import numpy as np

video=cv2.VideoCapture(0) 								#video kaydı yaptık

while(True):											#videoyu sonsuz donguye aldık	
	_, frame=video.read()								#videoyu cerceve cerceve almasını istedik
	pixel=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)		#hsv kullnarak piksel piksel ayrıştırırız bu sayede mavinin tonlarını bulabiliriz
	altmavi=np.array([110,50,50])						#alt limit burda mavinin alt limitini belirttik
	ustmavi=np.array([130,255,255])						#üst limit burda mavinin üst limitini belirttik

	mask=cv2.inRange(pixel,altmavi,ustmavi)				#pixelrangede alt üst limitleri veririz
	a=cv2.bitwise_and(frame,frame,mask=mask)			#bitwise ile siyah ekran uzerinden mavi görüntüyü arayıp o kısmı beyazlaştırır

	cv2.imshow("Mavi Renk Tanima",mask)					#başlık ve değişken belirttik

	key=cv2.waitKey(5)& 0xFF							#64 bit cihazlarda 0xFF kullanabiliriz
	
	if key==27:											#esc nin ascii kdo değeri burada esce basınca sonsuz döngüden çıkmamızı sağlar
		break
cv2.destroyAllWindows()


