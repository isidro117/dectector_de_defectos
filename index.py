from tkinter import *
from PIL import Image,ImageTk
import cv2
import os
import imutils
import json
from pathlib import *
import numpy as np 
# from dectarorObjetos import *
import uuid
from tensorflow.keras.utils import load_img, img_to_array
from keras.models import load_model
# from entrenamiento import *
# from tensorflow.keras.utils import load_img, img_to_array
# from keras.models import load_model





class aMiMenu(Frame):
    cap = None    
    def __init__(self, master=None):
        super().__init__(master,width=380,height=480)
        self.master=master
        self.pack()
        self.MiVentana()
    def Video_RGB(self):
        global cap
        cap=cv2.VideoCapture("rtsp://admin:Chiloscamara02@192.168.0.109:554/video")
        # cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.visualizar()

    def detener(self):
        global cap
        cap.release()

    def visualizar(self):
        global cap   
        if cap is not None:
            ret, frame = cap.read()
            if ret == True:
                frame = imutils.resize(frame, width=320)
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)
                self.lblVideo.configure(image=img)
                self.lblVideo.image = img
                self.lblVideo.after(10, self.visualizar)
            else:
                self.lblVideo.image = ""
                cap.release()

    def MiVentana(self):

        self.Indexx=LabelFrame(self,text= "Princiapal")
        self.Indexx.place(x=0,y=0,width=380,height=480)

        self.lblVideo = Label(self.Indexx)
        self.lblVideo.place(x=10,y=10,width=340,height=200)

        self.ProsAjuste=LabelFrame(self,text="Panel de Procesamiento")
        self.ProsAjuste.place(x=10,y=220,width=340,height=120)

        self.Pavanzado=Button(self.ProsAjuste,text="Avanzado",command=cMiMenu.Abrir)
        self.Pavanzado.place(x=0,y=5,width=75,height=25)

        self.Pmedio=Button(self.ProsAjuste,text="Basico",command=dMiMenu.Abrir)
        self.Pmedio.place(x=85,y=5,width=75,height=25)

        self.Pbasico=Button(self.ProsAjuste,text="DetenerCAM",command=self.detener)
        self.Pbasico.place(x=170,y=5,width=75,height=25)

        self.PersAjuste=LabelFrame(self,text="Ajuste de salidas")
        self.PersAjuste.place(x=10,y=345,width=340,height=120)
    
        self.Salida0=Button(self.PersAjuste,text="SalidaD0",command=eMiMenu.Abrir)
        self.Salida0.place(x=0,y=5,width=75,height=25)

        self.Pmedio=Button(self.PersAjuste,text="SalidaD1")
        self.Pmedio.place(x=85,y=5,width=75,height=25)

        self.Pbasico=Button(self.PersAjuste,text="SalidaD2")
        self.Pbasico.place(x=170,y=5,width=75,height=25)

        self.Pdetener=Button(self.PersAjuste,text="Personalizada")
        self.Pdetener.place(x=255,y=5,width=75,height=25)
class bMiMenu(Frame):

    def __init__(self, master=None):
        super().__init__(master,width=260,height=240)
        self.master=master
        self.pack()
        self.OpAvanz() 

    def Abrir ():
        ventana_nueva=Toplevel()
        ventana_nueva.wm_title("Opcciones Avanzadas")
        aplicacion01=bMiMenu(ventana_nueva)
        aMiMenu.detener(aplicacion00)

    def OpAvanz(self):

        self.Indexx=LabelFrame(self,text= "Princiapal")
        self.Indexx.place(x=0,y=0,width=380,height=240)


        self.MisOpcciones={
            'Identificacion de Color':0,
            'Deteccion de Agujeros':0,
            'Seleccion de tamaño':0,
            'Forma (Figura)':0,
            'Area y Perimetro':0
        }
        for clave in self.MisOpcciones:
            self.MisOpcciones[clave]=IntVar()
            Micheckbutom=Checkbutton(self.Indexx,text=clave,variable=self.MisOpcciones[clave])
            Micheckbutom.pack(side="top",anchor=NW )
        

        
        self.BontonAcp=Button(self.Indexx,text="Aceptar",command=self.Consultar)
        self.BontonAcp.place(x=0,y=180,width=100,height=30)
        self.BontonCanc=Button(self.Indexx,text="Cancelar")
        self.BontonCanc.place(x=110,y=180,width=100,height=30)

      
    def Consultar(self):
        for clave, value in self.MisOpcciones.items():
            state = value.get()
            if state != 0:
                print(clave)
                self.MisOpcciones[clave].set(0)
                cMiMenu.Abrir()
class cMiMenu(Frame):
    cap=None
    def __init__(self, master=None):
        super().__init__(master,width=1080,height=720)
        self.master=master
        self.pack()
        self.ParametrosS()
        self.MenuPros()

    def Video_RGB(self):
        global cap
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.visualizar()

    def visualizar(self):
        global cap
        if cap is not None:
            ret, self.frame = cap.read()
            if ret == True:
                self.frame = imutils.resize(self.frame, width=320)
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                
                im = Image.fromarray(self.frame)
                img = ImageTk.PhotoImage(image=im)
                self.lblVideoPre.configure(image=img)
                self.lblVideoPre.image = img
                self.lblVideoPre.after(10, self.visualizar)   
            else:
                self.lblVideoPre.image = ""
                cap.release()
    def Abrir ():
        ventana_nueva2=Toplevel()
        ventana_nueva2.wm_title("Opcciones Avanzadas Selccionadas")
        aplicacion02=cMiMenu(ventana_nueva2)
        cMiMenu.Video_RGB(aplicacion02)
    def perimetro(self):
        global alto,ancho,rect,angulo
        #contornos=self.OObtener_contorno()
        #detector=cMiMenu()
        #detector=DectectorFondohomo()

     
        contornos=self.OObtener_contorno(self.frame)
        #contornos=detector.deteccion_objeto(self.frame)    

        parametro= cv2.aruco.DetectorParameters()
        diccionario= cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50);


        coneres, _, _ = cv2.aruco.detectMarkers(self.frame, diccionario, parameters=parametro)

        if coneres:
            int_coneres= np.int0(coneres)
            cv2.polylines(self.frame, int_coneres, True, (0,255,0),5)
            
            perimetro_aruco= cv2.arcLength(coneres[0], True)
            

            pix_cm_= perimetro_aruco/16

            
            for c in contornos:
                rect=cv2.minAreaRect(c)
                (x,y),(w,h), angulo=rect

                ancho = w/pix_cm_

                alto = h/pix_cm_

                
                cv2.circle(self.frame, (int(x),int(y)),5,(255,0,0),-1)

                box= cv2.boxPoints(rect)
                box =np.int0(box)

                cv2.polylines(self.frame, [box], True, (0,0,255),2)

                cv2.putText(self.frame, "Alto {} cm".format(round(alto,1)), (int(x-100),int(y-20)),cv2.FONT_HERSHEY_PLAIN, 1, (100,200,0),2)
                cv2.putText(self.frame, "Ancho {} cm".format(round(ancho,1)), (int(x-100),int(y+15)),cv2.FONT_HERSHEY_PLAIN, 1, (100,200,0),2)
                #cv2.putText(self.frame, "Angulo {} °".format(round(angulo,1)), (int(x-100),int(y+25)),cv2.FONT_HERSHEY_PLAIN, 1, (100,200,0),2)

                # epsilon = inCon4*cv2.arcLength(c,True)
                # approx = cv2.approxPolyDP(c,epsilon,True)

        im = Image.fromarray(self.frame)
        img = ImageTk.PhotoImage(image=im)
        self.lblVideoPre1.configure(image=img)
        self.lblVideoPre1.image = img
        self.lblVideoPre1.after(10,self.perimetro)
    def OObtener_contorno(self,captura):
        global inCon0,inCon1,inCon2,inCon3,inCon4
        
        #cv2.aruco.Dictionary(cv2.aruco.DICT_5X5_100)
        
        #detector = DectectorFondohomo()

    
        inCon0=self.SkerA1.get()
        inCon1=self.SkerA2.get()
        inCon2=self.SkerA3.get()
        inCon3=self.SkerA4.get()
        inCon4=self.SkerA5.get()

        gris=cv2.cvtColor(captura,cv2.COLOR_BGR2GRAY)
        gauss = cv2.GaussianBlur(gris, (inCon0,inCon1), 0)
        #blur = cv2.blur(gris, (3, 3))
        #Aplicar Canny a frame
        canny = cv2.Canny(gauss, inCon2, inCon3)
        canny  = cv2.dilate(canny, None, iterations=1)
        canny = cv2.erode(canny, None, iterations=1)
        #contornos= cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        contornos, _  = cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        objetos_contorno=[]

        for cnt in contornos:
            area=cv2.contourArea(cnt)
            # epsilon = inCon4*cv2.arcLength(cnt,True)
            # approx = cv2.approxPolyDP(cnt,epsilon,True)
            if area>200:
                objetos_contorno.append(cnt)
    
        return objetos_contorno      
    
    def ExtraerColor(self):
        global slider1a,slider1b,slider2a,slider2b,slider3a,slider3b,cap,mask,contornosw

        #Slider De H
        slider1a = self.slider01.get()
        slider1b = self.slider02.get()

        #sliders de S
        slider2a=self.slider03.get()
        slider2b=self.slider04.get()

        #slider de V
        slider3a=self.slider05.get()
        slider3b=self.slider06.get()
         

        hsv = cv2.cvtColor(self.frame, cv2.COLOR_RGB2HSV)
        
        # Establecemos el rango minimo y maximo para la codificacion HSV
        color_oscuro = np.array([slider1b, slider2b, slider3b])
        color_brilla = np.array([slider1a, slider2a, slider3a])

        # Detectamos los pixeles que esten dentro de los rangos
        mascara = cv2.inRange(hsv, color_oscuro, color_brilla)
        
        

        # Mascara
        mask = cv2.bitwise_and(self.frame,self.frame, mask=mascara)

        mask = imutils.resize(mask, width=320)        
        
        contornosw=self.OObtener_contorno(mask)
        
        for c in contornosw:
            rect0=cv2.minAreaRect(c)
            (x,y),(w,h), angulo=rect0
                    
            #cv2.circle(mask, (int(x),int(y)),5,(0,255,0),-1)

            box= cv2.boxPoints(rect0)
            box =np.int0(box)

            #cv2.polylines(mask, [box], True, (255,0,0),2)
    
    

        #Convertimos el video
        im2 = Image.fromarray(mask)
        img2 = ImageTk.PhotoImage(image=im2)

        #Mostramos en el GUI
        self.lblVideoPre1.configure(image=img2)
        self.lblVideoPre1.image = img2
        self.lblVideoPre1.after(10,self.ExtraerColor)

    def ParametrosS(self):
        
        self.Idgeneral=LabelFrame(self,text="General")
        self.Idgeneral.place(x=0,y=0,width=1080,height=720)   
        # #COLOR
        self.IdColor=LabelFrame(self.Idgeneral,text="Identificador de colores")
        
        self.lblH=Label(self.IdColor,text="Parametro H")
        self.lblH.place(x=0,y=10,width=100,height=50)

        self.slider01=Scale(self.IdColor,from_= 0, to=179,orient=HORIZONTAL)
        self.slider01.place(x=100,y=0,width=100,height=50)
        self.slider02=Scale(self.IdColor,from_= 0,to=179,orient=HORIZONTAL)
        self.slider02.place(x=200,y=0,width=100,height=50)

        self.lblS=Label(self.IdColor,text="Parametro de S")
        self.lblS.place(x=0,y=60,width=100,height=50)

        self.slider03=Scale(self.IdColor,from_=0,to=255,orient=HORIZONTAL)
        self.slider03.place(x=100,y=60,width=100,height=50)
        self.slider04=Scale(self.IdColor,from_=0,to= 255,orient=HORIZONTAL)
        self.slider04.place(x=200,y=60,width=100,height=50)



        self.lblV=Label(self.IdColor,text="Parametro de V")
        self.lblV.place(x=0,y=120,width=100,height=50)

        self.slider05=Scale(self.IdColor,from_=0,to=255,orient=HORIZONTAL)
        self.slider05.place(x=100,y=120,width=100,height=50)
        self.slider06=Scale(self.IdColor,from_=0,to= 255,orient=HORIZONTAL)
        self.slider06.place(x=200,y=120,width=100,height=50)

        self.btnaceptar=Button(self.IdColor,text="Aceptar",command=self.ExtraerColor)
        self.btnaceptar.place(x=10,y=170,width=100,height=30)

        self.btnenviar=Button(self.IdColor,text="Enviar",command=self.Enviar_datos_ExColor)
        self.btnenviar.place(x=115,y=170,width=100,height=30)

        self.btncargar=Button(self.IdColor,text="Cargar",command=self.Cargar_Ajustes)
        self.btncargar.place(x=220,y=170,width=60,height=30)

        self.ExtraContorno=LabelFrame(self.Idgeneral,text="Parametros de la Extraccion de contorno")
        
        self.lblKerA1=Label(self.ExtraContorno,text="Columna").place(x=0,y=0,width=50,height=30)
        self.SkerA1=Scale(self.ExtraContorno,from_=3, to=11,orient=HORIZONTAL)
        self.SkerA1.place(x=60,y=0,width=50,height=50)
    
        self.lblKerA2=Label(self.ExtraContorno,text="Fila").place(x=110,y=0,width=50,height=30)
        self.SkerA2=Scale(self.ExtraContorno,from_=3, to=11,orient=HORIZONTAL)
        self.SkerA2.place(x=150,y=0,width=50,height=50)

        self.lblkerA3=Label(self.ExtraContorno,text="Umbral L").place(x=0,y=60,width=60,height=30)
        self.SkerA3=Scale(self.ExtraContorno,from_=50,to=200,orient=HORIZONTAL)
        self.SkerA3.place(x=60,y=60,width=50,height=50)

        self.lblkerA4=Label(self.ExtraContorno,text="Umbral S").place(x=110,y=60,width=60,height=30)
        self.SkerA4=Scale(self.ExtraContorno,from_=50,to=200,orient=HORIZONTAL)
        self.SkerA4.place(x=170,y=60,width=50,height=50)
         
        self.lblkerA5=Label(self.ExtraContorno,text="Epsilon").place(x=220,y=60,width=50,height=30)
        self.SkerA5=Scale(self.ExtraContorno,from_=0.01, to=1.00, digits = 3, resolution = 0.01,orient=HORIZONTAL)
        self.SkerA5.place(x=275,y=60,width=50,height=50)

        self.btnaceptar0=Button(self.ExtraContorno,text="Aceptar",command=self.perimetro)
        self.btnaceptar0.place(x=30,y=130,width=100,height=30)

        self.btnenviar0=Button(self.ExtraContorno,text="Enviar",command=self.Enviar_datos_ExCont)
        self.btnenviar0.place(x=140,y=130,width=100,height=30)

        self.btncargar0=Button(self.ExtraContorno,text="Cargar",command=self.Cargar_Ajustes0)
        self.btncargar0.place(x=245,y=130,width=60,height=30)
        
        self.lblVideoPre=Label(self.Idgeneral)
        self.lblVideoPre.place(x=355,y=10,width=320,height=200)

        self.lblVideoPre1=Label(self.Idgeneral)
        self.lblVideoPre1.place(x=355,y=220,width=320,height=200)

        self.DetAgujero=LabelFrame(self.Idgeneral,text="Ajueste de deteccion de color")
        
        self.btnverificarSColor=Button(self.DetAgujero,text="iniciar Verificar",command=self.Recibir_ColorSelecionado)
        self.btnverificarSColor.place(x=0,y=10,width=100,height=30)

        self.checkbtna0=Checkbutton(self.DetAgujero,text="Img Correcta",variable=checkbtn01).place(x=0,y=40,width=100,height=40)
        
        

        

        self.FormaFig=LabelFrame(self.Idgeneral,text="Ajuestes de deteccion de Figura")
        

        self.btnguardaralto=Button(self.FormaFig,text="Guardar",command=self.Guardar_1)
        self.btnguardaralto.place(x=0,y=10, width=50,height=30)

        self.btnrecibiralto=Button(self.FormaFig,text="Recibir",command=self.Recibir_altoandancho)
        self.btnrecibiralto.place(x=0,y=50, width=50,height=30)

        self.btnverificar=Button(self.FormaFig,text="iniciar Verificar",command=self.comprobacion_capturacion)
        self.btnverificar.place(x=0,y=90,width=100,height=30)
    def Recibir_ColorSelecionado(self):
        
        KERNEL_SIZE = 20
        conversion=cv2.cvtColor(mask,cv2.COLOR_BGR2RGB)
        
        imgray = cv2.cvtColor(conversion,cv2.COLOR_RGB2GRAY)
      
        ret, thresh = cv2.threshold(imgray, 64, 255, 0)

        kernel = np.ones((KERNEL_SIZE, KERNEL_SIZE), np.uint8)
        img_e = cv2.dilate(thresh, kernel, iterations=1)
        (contours,_) = cv2.findContours(img_e, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        max_countour = max(contours, key = cv2.contourArea)         
        
        cropped =self.crop_min_rect(conversion,max_countour)
        
        #Recorte00= cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
        
        RecoGray= cv2.cvtColor(cropped, cv2.COLOR_RGB2GRAY)
        #RecoGray=RecoGray*255
        
        _, thresh0= cv2.threshold(RecoGray,0,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        nuvCont= cv2.findContours(thresh0, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) [-2]
        nuvCont=sorted(nuvCont,key=cv2.contourArea)
      
        for a in nuvCont:
            if cv2.contourArea(a)>100:
                break
        mask01= np.ones(cropped.shape[:2],np.uint8)*255
        
        cv2.drawContours(mask01,[a], -1, 255,-1)
        
        NuevoRecorte= cv2.bitwise_and(cropped,cropped,mask=mask01)
        
        if (checkbtn01.get()==1):
            cv2.imwrite(imagenesCorr + "/" +str(uuid.uuid4())+".png", NuevoRecorte)
            print("Imagen salvada Correctamente")
        else: 
            cv2.imwrite(imagenesIncorr + "/" +str(uuid.uuid4())+".png", NuevoRecorte)
            print("Imagen salvada Correctamente++")
      
    def crop_min_rect(self,img,contorno):
        
        rect1= cv2.minAreaRect(contorno)
        box1 = cv2.boxPoints(rect1)
        box1 = np.int0(box1)

        w, h = (int(n) for n in  rect1[1])
        xs, ys = zip(*box1)
        x1, y1 = min(xs), min(ys)
        x2, y2 = max(xs), max(ys)
        center = int((x1 + x2) / 2), int((y1 + y2) / 2)
        size = int((x2 - x1)), int((y2 - y1))

        rotated = False
        angle = rect1[2]

        if angle < -45:
            angle += 90
            rotated = True

        rot_m = cv2.getRotationMatrix2D((size[0] / 2, size[1] / 2), angle, 1.0)
        cropped = cv2.warpAffine(cv2.getRectSubPix(img, size, center), rot_m, size)

        cw = w if not rotated else h
        ch = h if not rotated else w

        img_crop = cv2.getRectSubPix(cropped, (cw, ch), (size[0] / 2, size[1] / 2))
        
        return img_crop
        
        
    def Recibir_altoandancho(self):
        global altonuevo,anchonuevo
        altonuevo=round(ancho,1)
        anchonuevo=round(alto,1)


        self.labalto=Label(self.FormaFig,text="Ancho:"+str(anchonuevo)).place(x=70,y=0,width=80,height=30)
        
        self.lancho=Label(self.FormaFig,text="Alto:"+str(altonuevo)).place(x=70,y=50,width=80,height=30)

        self.langulo=Label(self.FormaFig,text="Angulo:"+str(angulo)).place(x=100,y=90,width=80,height=30)
                       
    def comprobacion_capturacion(self):

        toleranciamas=0.3
        toleranciamenos=0.3
      

       
        self.cargar_automatic()

        altotolerance00 = altoalmacen-toleranciamenos
        altotolerance01 = altoalmacen+toleranciamas
        anchotolerance00 = anchoalmacen-toleranciamenos
        anchotolerance01 = anchoalmacen+toleranciamas 

       
        
        
        if  altotolerance00<altonuevo<altotolerance01 and anchotolerance00<anchonuevo<anchotolerance01 and angulo == 90:
            #Capturar imagen sin los contornos, con referencia correcta
            #nombre_foto= str(uuid.uuid4())+".png"
            caja=cv2.boxPoints(rect)
            caja=np.int0(caja)
            a=caja[0][0]
            b=caja[1][0]
            c=caja[1][1]
            d=caja[2][1]
            # print(a[1])
            # # print(b)
            # print(caja)
            # print(angulo)
            cropped=self.frame[c:d,a:b]
            Recorte= cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
            
            # # #print(type(box))
            cv2.imwrite(imagenesCorr + "/" +str(uuid.uuid4())+".png", Recorte)

            #cv2.imwrite(nombre_foto,self.frame)

            # print("estas aqui")
            print("Imagen salvada Correctamente")
            # print(anchoalmacen)
        elif altotolerance00<anchonuevo<altotolerance01 and anchotolerance00<altonuevo<anchotolerance01 and angulo == 90:
            #Capturar imagen sin los contornos, con referencia incorrecta
            caja=cv2.boxPoints(rect)
            caja=np.int0(caja)
            a=caja[0][0]
            b=caja[1][0]
            c=caja[1][1]
            d=caja[2][1]
        
            # print(angulo)
            # print(b)
            # print(c)
            cropped=self.frame[c:d,a:b]
            Recorte= cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
            
            # #print(type(box))
            cv2.imwrite(imagenesCorr + "/" +str(uuid.uuid4())+".png", Recorte)
            
            # print("estas aqui")
            print("Imagen salvada Correctamente")

        elif angulo == 90:
            
            caja=cv2.boxPoints(rect)
            caja=np.int0(caja)
            a=caja[0][0]
            b=caja[1][0]
            c=caja[1][1]
            d=caja[2][1]
        
            #print(angulo)
            # print(b)
            # print(c)
            cropped=self.frame[c:d,a:b]
            Recorte= cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
            
            # #print(type(box))
            cv2.imwrite(imagenesIncorr + "/" +str(uuid.uuid4())+".png", Recorte)
            
            # print("estas aqui")
            print("Imagen salvada Correctamente+")
        else:
            print("Error")
            #cv2.imwrite(nombre_foto,self.frame)

        
    def MenuPros(self):
        BarraMenu=Menu(self.master)
        self.master.config(menu=BarraMenu)

        ExTColor = Menu(BarraMenu)
        ExTColor.add_command(label="Abrir Camara",command=self.AbrirCamara)
        ExTColor.add_command(label="Extraer Color",command=self.color)
        ExTColor.add_command(label="Calcular Objeto",command=self.perimeter)
        BarraMenu.add_cascade(label="Procesamientos", menu=ExTColor)
    def Enviar_datos_ExCont(self):
        global KerC,KerR,ThrL,ThrU,Eps

        KerC=self.SkerA1.get()
        KerR=self.SkerA2.get()
        ThrL=self.SkerA3.get()
        ThrU=self.SkerA4.get()
        Eps=self.SkerA5.get()

        self.prametros0=LabelFrame(self.Idgeneral,text="Parametros elegidos")
        self.prametros0.place(x=880,y=10,width=190,height=400)

        self.sub1prametros0= Label(self.prametros0,text="Nucleo C :"+str(KerC)).place(x=0,y=0,width=100,height=30)
        self.sub1prametros1= Label(self.prametros0,text="Nucleo R :"+str(KerR)).place(x=0,y=35,width=100,height=30)
        self.sub1prametros2 = Label(self.prametros0,text="Lower Theshold: "+str(ThrL)).place(x=0,y=70,width=140,height=30)
        self.sub1prametros3 = Label(self.prametros0,text="Upper Theshold: "+str(ThrU)).place(x=0,y=105,width=140,height=30)
        self.sub1prametros4=Label(self.prametros0,text="Epsilon"+str(Eps)).place(x=0,y=135,width=135,height=30)

        self.btnSave=Button(self.prametros0,text="Guardar",command=self.Guardar_0).place(x=10,y=350,width=100,height=30)

    def Enviar_datos_ExColor(self):
        global CbrilloH,CoscuroH,CbrilloS,CoscuroS,CbrilloV,CoscuroV
        CbrilloH=self.slider01.get()
        CoscuroH=self.slider02.get()
        CbrilloS=self.slider03.get()
        CoscuroS=self.slider04.get()
        CbrilloV=self.slider05.get()
        CoscuroV=self.slider06.get()

        
        self.prametros0=LabelFrame(self.Idgeneral,text="Parametros elegidos")
        self.prametros0.place(x=880,y=10,width=190,height=400)
        self.subprametros0=Label(self.prametros0,text="Color Brillo H:"+str(CbrilloH)).place(x=0,y=0,width=100,height=30)
        self.subprametros1=Label(self.prametros0,text="Color Oscuro H:"+str(CoscuroH)).place(x=0,y=35,width=100,height=30)
        self.subprametros2=Label(self.prametros0,text="Color Brillo S:"+str(CbrilloS)).place(x=0,y=70,width=100,height=30)
        self.subprametros3=Label(self.prametros0,text="Color Oscuro S:"+str(CoscuroS)).place(x=0,y=105,width=100,height=30)
        self.subprametros4=Label(self.prametros0,text="Color Brillo V:"+str(CbrilloV)).place(x=0,y=135,width=100,height=30)
        self.subprametros5=Label(self.prametros0,text="Color Oscuro V:"+str(CoscuroV)).place(x=0,y=165,width=100,height=30)

        self.btnSave=Button(self.prametros0,text="Guardar",command=self.Guardar_).place(x=10,y=350,width=100,height=30)

    def AbrirCamara(self):
        global Enceder0
        if Enceder0:
            Enceder0=False
        else:
            Enceder0=True
            self.Video_RGB()
    def Guardar_0(self):
        save_data={
            "NucleoC": KerC,
            "NucleoR": KerR,
            "LowerTheshold": ThrL,
            "UpperTheshold": ThrU,
            "Epsilon": Eps,
        }
        with open('configB', "w") as f:
            json.dump(save_data,f)
            print("Datos Salvados")
    
    def Guardar_(self):
        save_data={
            "Color Brillo H": CbrilloH,
            "Color Oscuro H": CoscuroH,
            "Color Brillo S": CbrilloS,
            "Color Oscuro S": CoscuroS,
            "Color Brillo V": CbrilloV,
            "Color Oscuro V": CoscuroV,
        }
        with open('configA', "w") as f:
            json.dump(save_data,f)
            print("Datos Salvados")
    def Guardar_1 (self):
        save_data={
            "alto": altonuevo,
            "ancho":anchonuevo,
        }
        with open('configWH', "w") as f:
            json.dump(save_data,f)
            print("Datos Salvados")
    
    def cargar_automatic(self):
        global altoalmacen, anchoalmacen 
        try: 
            with open('configWH','rb') as f:
                save_data= json.load(f)
            altoalmacen = save_data["alto"]
            anchoalmacen= save_data["ancho"]
        except Exception as e:
            print
            "error loading saved state:", str(e)

    def Cargar_Ajustes(self):

        try:
            with open('configA', "rb") as f:
                save_data = json.load(f)
            self.slider01.set(save_data["Color Brillo H"])
            self.slider02.set(save_data["Color Oscuro H"])
            self.slider03.set(save_data["Color Brillo S"])
            self.slider04.set(save_data["Color Oscuro S"])
            self.slider05.set(save_data["Color Brillo V"])
            self.slider06.set(save_data["Color Oscuro V"])
        except Exception as e:
            print
            "error loading saved state:", str(e)
    def Cargar_Ajustes0(self):
        try:
            with open('configB', "rb") as f:
                save_data = json.load(f)
            self.SkerA1.set(save_data["NucleoC"])
            self.SkerA2.set(save_data["NucleoR"])
            self.SkerA3.set(save_data["LowerTheshold"])
            self.SkerA4.set(save_data["UpperTheshold"])
            self.SkerA5.set(save_data["Epsilon"])
        except Exception as e:
            print
            "error loading saved state:", str(e)
    def perimeter(self):
        global Btn1
        if Btn1:
            self.ExtraContorno.place_forget()
            self.FormaFig.place_forget()
            Btn1=False
        else:
            self.ExtraContorno.place(x=0,y=230,width=350,height=200)
            self.FormaFig.place(x=680,y=210,width=200,height=200)
            Btn1=True
    def color(self):
        global Btn0
        if Btn0:
            self.IdColor.place_forget()
            self.DetAgujero.place_forget()
            Btn0=False
        else:
            self.IdColor.place(x=0,y=1,width=350,height=230)
            self.DetAgujero.place(x=680,y=10,width=200,height=200)
            Btn0=True 
class dMiMenu(Frame):

    cap=None
    
    def __init__(self, master=None):
        super().__init__(master,width=900,height=300)
        self.master=master
        self.pack()
        self.ParametrosConIA()
        
        
    def Video_RGB(self):
        global cap
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.visualizar()
    def visualizar(self):
        global cap 
        if cap is not None:
            ret, self.frame = cap.read()
            if ret == True:
                self.frame = imutils.resize(self.frame, width=320)
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                
                im = Image.fromarray(self.frame)
                img = ImageTk.PhotoImage(image=im)
                self.lblVideoPre2.configure(image=img)
                self.lblVideoPre2.image = img
                self.lblVideoPre2.after(10, self.visualizar)   
            else:
                self.lblVideoPre2.image = ""
                cap.release()
    def Abrir ():
        ventana_nueva3=Toplevel()
        ventana_nueva3.wm_title("Modo Automatico")
        aplicacion03=dMiMenu(ventana_nueva3)
        dMiMenu.Video_RGB(aplicacion03)
    
    
        
    def ParametrosConIA(self):
        global bien
        self.bien=StringVar()       
        # self.mal=StringVar()       
        self.Idgeneral=LabelFrame(self,text="General IA")
        self.Idgeneral.place(x=0,y=0,width=900,height=300)
        
        self.lblactua0=Label(self.Idgeneral,text="Deteccion:")
        self.lblactua0.place(x=10,y=10,width=60,height=40)
        self.lblactua1=Label(self.Idgeneral,textvariable=self.bien)
        self.lblactua1.place(x=65,y=10,width=30,height=40)
        # self.lblactua2=Label(self.Idgeneral,textvariable=self.mal)
        # self.lblactua2.place(x=70,y=10,width=200,height=40)
        
        self.lblVideoPre2=Label(self.Idgeneral)
        self.lblVideoPre2.place(x=100,y=0,width=720,height=200)
        
        self.btnpredict=Button(self.Idgeneral,text="Iniciar",command=self.segimineto)
        self.btnpredict.place(x=200,y=240,width=100,height=30)
        
        self.btnpredict0=Button(self.Idgeneral,text="Predecir",command=self.prediccion)
        self.btnpredict0.place(x=300,y=240,width=100,height=30)
        
        self.btnCapturar=Button(self.Idgeneral,text="C.Imagen",command=self.captuara_imagen)
        self.btnCapturar.place(x=400,y=240,width=100,height=30)
        #predict(self.frame)
        
        self.checkbtn0=Checkbutton(self.Idgeneral,text="Img Correcta",variable=checkbtn01).place(x=500,y=240,width=100,height=40)
        
   
    
    def contornoD(self,img,contorno):
        
        rect1= cv2.minAreaRect(contorno)
        box1 = cv2.boxPoints(rect1)
        box1 = np.int0(box1)

        w, h = (int(n) for n in  rect1[1])
        xs, ys = zip(*box1)
        x1, y1 = min(xs), min(ys)
        x2, y2 = max(xs), max(ys)
        center = int((x1 + x2) / 2), int((y1 + y2) / 2)
        size = int((x2 - x1)), int((y2 - y1))           
           
        rotated = False
        angle = rect1[2]

        if angle < -45:
            angle += 90
            rotated = True

        rot_m = cv2.getRotationMatrix2D((size[0] / 2, size[1] / 2), angle, 1.0)
        cropped = cv2.warpAffine(cv2.getRectSubPix(img, size, center), rot_m, size)

        cw = w if not rotated else h
        ch = h if not rotated else w

        img_crop = cv2.getRectSubPix(cropped, (cw, ch), (size[0] / 2, size[1] / 2))
        #im_draw  = cv2.drawContours(img, [box1], -1, (0, 0, 255), 5)
        return img_crop
       
        
    def detecciondeObjeto(self,captura):
        global max_countour,conversion
        
        conversion=cv2.cvtColor(captura,cv2.COLOR_BGR2RGB)
        imgray = cv2.cvtColor(captura,cv2.COLOR_RGB2GRAY)
      
        gauss = cv2.GaussianBlur(imgray, (5,5), 0)
        #blur = cv2.blur(gris, (3, 3))
        #Aplicar Canny a frame
        canny = cv2.Canny(gauss, 138, 113)
        canny  = cv2.dilate(canny, None, iterations=1)
        canny = cv2.erode(canny, None, iterations=1)
        #contornos= cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        contornos, _  = cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        max_countour = max(contornos, key = cv2.contourArea,default=None)
        #print(type(max_countour))
        objetos_contorno=[]
        

        for cnt in contornos:
            area=cv2.contourArea(cnt)
            # epsilon = inCon4*cv2.arcLength(cnt,True)
            # approx = cv2.approxPolyDP(cnt,epsilon,True)
            if area>200:
                objetos_contorno.append(cnt)
                
        return objetos_contorno    
        
    def captuara_imagen(self):
        
        if (checkbtn01.get()==1):     
            cropped = self.contornoD(conversion,max_countour)
            NuevoRecorte=cropped
            cv2.imwrite(imagenesCorrVa + "/" +str(uuid.uuid4())+".png", NuevoRecorte)
            print("Imagen salvada Correctamente")
        else:
            cropped = self.contornoD(conversion,max_countour)
            NuevoRecorte=cropped
            cv2.imwrite(imagenesIncorrVa + "/" +str(uuid.uuid4())+".png", NuevoRecorte)
            print("Imagen salvada Correctamente+")
    def segimineto(self):
        global box00
        cont=self.detecciondeObjeto(self.frame)
        for c in cont:
            
            rect=cv2.minAreaRect(c)
            (x,y),(w,h), angulo=rect
        
            #cv2.circle(self.frame, (int(x),int(y)),5,(255,0,0),-1)

            box00= cv2.boxPoints(rect)
            box00 =np.int0(box00)
            #cv2.polylines(self.frame, [box00], True, (0,255,0),2)
            if estado0==1:
                cv2.polylines(self.frame, [box00], True, (0,255,0),2)
                #estado1=0
                #cv2.putText(self.frame, "Ancho {} cm".format(None), (int(x-100),int(y+15)),cv2.FONT_HERSHEY_PLAIN, 1, (100,200,0),2)
            elif estado1==1:
                cv2.polylines(self.frame, [box00], True, (255,0,0),2)
                #estado0=0
                #cv2.putText(self.frame, "Ancho {} cm".format(None), (int(x-100),int(y+15)),cv2.FONT_HERSHEY_PLAIN, 1, (100,200,0),2)
            else:
                cv2.polylines(self.frame, [box00], True, (0,0,255),2)
                # cv2.putText(self.frame, "Ancho {} cm".format(None), (int(x-100),int(y+15)),cv2.FONT_HERSHEY_PLAIN, 1, (100,200,0),2)
            
        im = Image.fromarray(self.frame)
        img = ImageTk.PhotoImage(image=im)
        self.lblVideoPre2.configure(image=img)
        self.lblVideoPre2.image = img
        self.lblVideoPre2.after(10,self.segimineto)
        
    def prediccion(self):
        global estado0,estado1
        contt=self.detecciondeObjeto(self.frame)
        for cp in contt:
            
            cropped = self.contornoD(conversion,max_countour)
            #x = load_img(cropped, target_size=(longitud, altura))
            qx= cv2.resize(cropped,(50,50),interpolation=cv2.INTER_CUBIC)
            qx = img_to_array(qx)
            qx = np.expand_dims(qx, axis=0)
            array = cnn.predict(qx)
            result = array[0]
            answer = np.argmax(result)
            if answer == 0:
                self.bien.set("Bien")
                estado0=1
                estado1=0
            elif answer == 1:
                self.bien.set("Mal")
                estado0=0 
                estado1=1
              
        im = Image.fromarray(self.frame)
        img = ImageTk.PhotoImage(image=im)
        self.lblVideoPre2.configure(image=img)
        self.lblVideoPre2.image = img
        self.lblVideoPre2.after(20,self.prediccion)
class eMiMenu(Frame):
     
    def __init__(self, master=None):
        super().__init__(master,width=260,height=150)
        self.master=master
        self.pack()
        self.configuracionOut()
    
    def Abrir ():
        global ventana_nueva3
        ventana_nueva3=Toplevel()
        ventana_nueva3.wm_title("Opcciones Avanzadas Selccionadas")
        aplicacion03=eMiMenu(ventana_nueva3)
        eMiMenu.configuracionOut(aplicacion03)

    def configuracionOut(self):
        
        self.GeneralFrame=LabelFrame(self,text="General")
        self.GeneralFrame.place(x=0,y=0,width=260,height=150)
        self.checkbtnD0=Checkbutton(self.GeneralFrame,text="Salida Digital 0",variable=checkbtnD0,onvalue=1,offvalue=0)
        self.checkbtnD0.place(x=0,y=0,width=100,height=40)
        self.checkbtnD0.deselect()
        self.btnguardarD0= Button(self.GeneralFrame,text="Guardar",command=self.Guardarestado).place(x=0,y=100,width=80,height=30)
        self.btncancelarD0= Button(self.GeneralFrame,text="Cancelar",command=ventana_nueva3.destroy).place(x=90,y=100,width=80,height=30)
    def preproceso(self):
        if checkbtnD0==1:
            self.estabtnD0=1
            self.estabtnD1=0
            self.estabtnD2=0
        elif checkbtnD0==0:
            self.estabtnD0=0
            self.estabtnD1=1
            self.estabtnD2=1
    def Guardarestado(self):
        
        save_data={
            "EstadoD0":checkbtn01(),
            "EstadoD1":self.estabtnD1,
            "EstadoD2":self.estabtnD2,
        }
        with open('EstadoOut', "w") as f:
            json.dump(save_data,f)
            print("Datos Salvados")

    def cargar_automatic(self):
        try: 
            with open('configWH','rb') as f:
                save_data= json.load(f)
            self.estabtnD0 = save_data["EstadoD0"]
            self.estabtnD1= save_data["EstadoD1"]
            self.estabtnD2=save_data["EstadoD2"]
        except Exception as e:
            print
            "error loading saved state:", str(e)

    
ventana = Tk()
ventana.wm_title("Programa IA aplha")
aplicacion00=aMiMenu(ventana)
#ventana.wm_geometry("380x480")
Enceder0=False
Btn0 = False
Btn1 = False
checkbtn01=IntVar()
checkbtnD0=IntVar()
checkbtnD1=IntVar()
checkbtnD2=IntVar()

# url= "rtsp://admin:Chiloscamara02@192.168.0.109:554/video"

# url= "http://admin:Chiloscamara02@192.168.0.109:443/videofeed"

#imagenesCorr="D:/dence/OneDrive/2023 Egresado/Tesis/Proyecto/Imagenes/entrenamiento/ImagenesCorrectas"
imagenesCorr="C:/Users/isidr/OneDrive/2023 Egresado/Tesis/Proyecto/Imagenes/entrenamiento/ImagenesCorrectas"
imagenesIncorr="C:/Users/isidr/OneDrive/2023 Egresado/Tesis/Proyecto/Imagenes/entrenamiento/ImagenesIncorrectas"
# imagenesIncorr="D:/dence/OneDrive/2023 Egresado/Tesis/Proyecto/Imagenes/entrenamiento/ImagenesIncorrectas"

#imagenesCorrVa="D:/dence/OneDrive/2023 Egresado/Tesis/Proyecto/Imagenes/validacion/ImagenesCorrectas"
imagenesCorrVa="C:/Users/isidr/OneDrive/2023 Egresado/Tesis/Proyecto/Imagenes/validacion/ImagenesCorrectas"
#imagenesCorr="C:/Users/<username>/OneDrive/2023 Egresado/Tesis/Proyecto/ImagenesCorrectas"
# imagenesIncorrVa="D:/dence/OneDrive/2023 Egresado/Tesis/Proyecto/Imagenes/validacion/ImagenesIncorrectas"
imagenesIncorrVa="C:/Users/isidr/OneDrive/2023 Egresado/Tesis/Proyecto/Imagenes/validacion/ImagenesIncorrectas"
#imagenesIncorr="C:/Users/<username>/OneDrive/2023 Egresado/Tesis/Proyecto/ImagenesIncorrectas"
# if not os.path.exists('ImagenesCorrectas'):
#     print('Carpeta Creada: ImagenesCorrectas')
#     os.makedirs('ImagenesCorrectas')
# if not os.path.exists('ImagenesIncorrectas'):
#     print('Carpeta Creada: ImagenesIncorrectas')
#     os.makedirs('ImagenesIncorrectas')

longitud, altura = 50, 50
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)
estado0=0
estado1=0

aplicacion00.Video_RGB()

aplicacion00.mainloop()