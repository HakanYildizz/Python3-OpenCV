"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu örneğimizde kameraya nasıl erişilir onu göreceğiz
Daha detaylı bilgi için siteye girebilirsiniz
"""
import cv2
import numpy as np
video = cv2.VideoCapture(0)
while(True):
    ret ,frame=video.read()
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame',gri)
    if cv2.waitKey(1) & 0xFF ==ord ('c'):
    	break
video.release()
cv2.destroyAllWindows()