import cv2
import imutils
import numpy as np 

# Cargamos la imagen
original = cv2.imread("IMG_4266.jpg")

scale_percent = 10 # percent of original size
width = int(original.shape[1] * scale_percent / 100)
height = int(original.shape[0] * scale_percent / 100)
dim = (width, height)

resize=cv2.resize(original, dim,interpolation=cv2.INTER_AREA)
cv2.imshow("original", resize)

# Convertimos a escala de grises
gris = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
 
# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gris, (5,5), 0)
 
cv2.imshow("suavizado", gauss)

# Detectamos los bordes con Canny
canny = cv2.Canny(gauss, 50, 100)
 
cv2.imshow("canny", canny)

# Buscamos los contornos
(contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contornos:
        epsilon = 0.01*cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,epsilon,True)
        area=cv2.contourArea(c)
        if area>2000:
            #print(len(approx))
            x,y,w,h = cv2.boundingRect(approx)

            if len(approx)==3:
                cv2.putText(resize,'Triangulo', (x,y-5),1,1,(0,255,0),1)

            if len(approx)==4:
                aspect_ratio = float(w)/h
                print('aspect_ratio= ', aspect_ratio)
                if aspect_ratio == 1:
                    cv2.putText(resize,'Cuadrado', (x,y-5),1,1,(0,255,0),1)

                else:
                    cv2.putText(resize,'Rectangulo', (x,y-5),1,1,(0,255,0),1)

            if len(approx)==5:
                cv2.putText(resize,'Pentagono', (x,y-5),1,1,(0,255,0),1)

            if len(approx)==6:
                cv2.putText(resize,'Hexagono', (x,y-5),1,1,(0,255,0),1)

            if len(approx)>10:
                cv2.putText(resize,'Circulo', (x,y-5),1,1,(255,0,0),1)
        else:
            epsilon = 0.09*cv2.arcLength(c,True)
            approx = cv2.approxPolyDP(c,epsilon,True)

# Mostramos el número de monedas por consola
print("He encontrado {} objetos".format(len(contornos)))
cv2.drawContours(resize,contornos,-1,(0,0,255), 2)
cv2.imshow("contornos", resize)

cv2.waitKey(0)


