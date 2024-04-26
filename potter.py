import cv2
import numpy as np

# HARRY POTER GÖRÜNMEZLİK PELERİN UYGULAMASI
# bu tip uygulamalarda yeşil rengin kullanılma sebebi insan vücudunda bulunmamasıdır

cam = cv2.VideoCapture(0)
#EŞİKLEME
lower = np.array([0, 0, 0])
upper = np.array([180, 255, 30])

#iilk değer karenin okunup okunmadığını kontrol eder
#ikinci değer ise okunan karenin kednisi
_,background = cam.read()
while(cam.isOpened()):
    _, frame = cam.read()  # kamera açıksa oku

     #GÖRÜNTÜ HSV RENK UZAYINA ÇEVRİLİYOR
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower,upper) # belirli bir renk aralığında renkleri tespit etme

    
    mask_not = cv2.bitwise_not(mask)# maskeyi maskenin içine attık
    bg = cv2.bitwise_and(background,background,mask = mask)
    fg = cv2.bitwise_and(frame,frame,mask = mask_not)
    çikti = cv2.addWeighted(bg,1,fg,1,0)
    # görüntüyü göster
    cv2.imshow("orjinal", frame) 
   
    cv2.imshow("çikti", çikti)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cam.release()#yenile
cv2.destroyAllWindows()


