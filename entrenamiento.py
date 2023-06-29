import numpy as np
import cv2
from tensorflow.keras.utils import load_img, img_to_array
#from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import sys

longitud, altura = 50, 50
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)


# direccion = "D:/dence/OneDrive/2023 Egresado/Tesis/Proyecto/Imagenes/validacion"
# dire_img= os.listdir (direccion)
# print("Nombres: ", dire_img)

# cap= cv2.VideoCapture(0)

# clase_piezacorr = np.solutions.corre

# piezzcorr= clase_piezacorr.Corre()


      
def predict(file):
  
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("pred: Esta en Buen estado")
  elif answer == 1:
    print("pred: Esta en Mal estado")


  return answer
      
  

#predict('malo.png')