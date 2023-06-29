import numpy as np
import cv2
 

# capture = cv2.VideoCapture(0)

# while (capture.isOpened()):
#     ret, frame = capture.read()
#     if (ret == True):
#         #Aplicar blur a frame
#         gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         gauss = cv2.GaussianBlur(gris, (5,5), 0)

#         blur = cv2.blur(frame, (5, 5))
#         #Aplicar Canny a frame
#         canny = cv2.Canny(gauss, 50, 150)

#         (contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         print("He encontrado {} objetos".format(len(contornos)))
#         cv2.drawContours(frame,contornos,-1,(0,0,255), 2)
#        #Mostrar Ventanas
#         cv2.imshow("suavizado", gauss)
#         cv2.imshow("canny", canny)
#         cv2.imshow("contornos", frame)


#         if (cv2.waitKey(1) == ord('s')):
#             break
#     else:
#         break

# capture.release()
# cv2.destroyAllWindows()
