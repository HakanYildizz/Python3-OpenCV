"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu örneğimizde bir fotoğrafı alıp siyah beyaz bir görüntüye çevirip uzantısını nasıl değiştirebiliriz onu göreceğiz
Daha detaylı bilgi için siteye girebilirsiniz
"""
import cv2
import numpy as np
foto=cv2.imread('python.jpg',0)
cv2.imshow('Fotoğraf',foto)
a=cv2.waitKey(0) & 0xFF
if a==27:
    cv2.destroyAllWindows()
elif a==ord('p'):
    cv2.imwrite('pythongri.png',foto)
    cv2.destroyAllWindows()
