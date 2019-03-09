"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu örneğimizde bir videoda hareket nasıl algılanır onu göreceğiz
Daha detaylı bilgi için siteye girebilirsiniz
"""
import cv2
import numpy as np

video=cv2.VideoCapture("test.mp4") 					#alacagımız video ve uzantısını buradan belirliyoruz

degisim=cv2.createBackgroundSubtractorMOG2()		#burda videoda değişen kısımları bu değişkene atıyoruz

while(True):
	ret,frame=video.read()							#ret görüntüden true yada false değer döndürür 

	if ret:
		degisimmask=degisim.apply(frame)
		cv2.imshow("Hareket Algılama",degisimmask)

		if cv2.waitKey(1) & 0xFF==27:				#video uzunlugu kadar parametre girin(waitkeye) 0xFFde esc in ascii kodu
			break
video.release()
cv2.destroyAllWindows()

