import numpy as np
import cv2


Recorte = cv2.imread("gisverde.png")
img_gray= cv2.cvtColor(Recorte, cv2.COLOR_BGR2GRAY)
img_gray=255-img_gray
cv2.imshow("Recortte",img_gray)
cv2.waitKey()

_, thresh0= cv2.threshold(img_gray,0,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
nuvCont= cv2.findContours(thresh0, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) [-2]
nuvCont=sorted(nuvCont,key=cv2.contourArea)

cv2.imshow("Theshold",thresh0)
cv2.waitKey()
for a in nuvCont:
    if cv2.contourArea(a)>100:
        break

mask01= np.ones(Recorte.shape[:2],np.uint8)*255
cv2.drawContours(mask01,[a], 0, 255,0)
#cv2.bitwise_not(mask01)


cv2.imshow("contorno",mask01)
cv2.waitKey()

NuevoRecorte= cv2.bitwise_and(Recorte,Recorte,mask=mask01)
cv2.imshow("Recorte Nuevo",NuevoRecorte)
cv2.waitKey()


#NuevoRecorte=cv2.cvtColor(NuevoRecorte, cv2.COLOR_GRAY2BGR)

#cv2.imshow("sa",NuevoRecorte)
#cv2.waitKey()