"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu örneğimizde videodan araç tespiti nasıl yapılır onu göreceğiz
Daha detaylı bilgi için siteye girebilirsiniz
"""
import cv2

cam=cv2.VideoCapture("araba.mp4")	#burada videoyu seçtik(aynı path üzerinde olmalı)
arac_cascade=cv2.CascadeClassifier("cars.xml")

while True:
	_,cerceve=cam.read()
	gri=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
	araclar=arac_cascade.detectMultiScale(gri,1.1,3)
	#burada skala ve çerçeveyi ayarladık(buradaki "1.1,3" değerlerini videoya göre değiştirebilirsiniz)
	#yolun sağ kısmında arabaları genellikle algılamıyor"1.1,2" yaparsak orayı da algılar
	for(x,y,w,h) in araclar:
		cv2.rectangle(cerceve,(x,y),(x+w,y+h),(0,255,255),2)	#burada aracı bulduk
	
	cv2.imshow('araclar',cerceve)
	if cv2.waitKey(25) & 0xFF==ord('q'):	#videodan çıkış yapmamız için 'q'a basmalıyız
		break

cam.release()
cv2.destroyAllWindows()