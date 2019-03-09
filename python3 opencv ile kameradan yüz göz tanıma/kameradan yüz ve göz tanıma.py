"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu örneğimizde kameradan yüz ve göz nasıl tanınır onu göreceğiz
Daha detaylı bilgi için siteye girebilirsiniz
"""
import cv2
face_cascade=cv2.CascadeClassifier("DataSet/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("DataSet/haarcascade_eye.xml")

cam=cv2.VideoCapture(0)

while True:
    _,goruntu = cam.read()
    gri = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gri,1.2,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(goruntu,(x,y),(x+w,y+h),(255,0,0),2)
        #burada yüzü bulduk
        roi_gri = gri[y:y+h,x:x+w]
        roi_renk = goruntu[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gri)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_renk,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            # burada gözü bulduk
    cv2.imshow('görüntü',goruntu)
    if cv2.waitKey(10) &0xFF==ord('q'):
        break
        #kameradan çıkış yapmamız için 'q'a basmalıyız
cam.release()
cv2.destroyAllWindows()

