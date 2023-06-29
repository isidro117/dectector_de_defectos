from tkinter import *
from tkinter import ttk

ventana= Tk()
ventana.title("Ajuste de procesamiento Avanzado")
ventana.geometry("380x480")
Indexx=LabelFrame(ventana,text= "Princiapal")
Indexx.place(x=0,y=0,width=380,height=480)


checkbtn01=IntVar()
checkbtn02=IntVar()
checkbtn03=IntVar()
checkbtn04=IntVar()
checkbtn05=IntVar()
checkbtn06=IntVar()

c0= Checkbutton(Indexx,text="Extraccion de Contorno",variable=checkbtn01)
c0.place(x=10,y=0)

c1= Checkbutton(Indexx,text="Procesamiento 2",variable=checkbtn02)
c1.place(x=10,y=30)

c2= Checkbutton(Indexx,text="Procesamiento 3",variable=checkbtn03)
c2.place(x=10,y=60)

c3= Checkbutton(Indexx,text="Procesamiento 4",variable=checkbtn04)
c3.place(x=10,y=90)

c4= Checkbutton(Indexx,text="Procesamiento 5",variable=checkbtn05)
c4.place(x=10,y=120)

c5= Checkbutton(Indexx,text="Procesamiento 6",variable=checkbtn06)
c5.place(x=10,y=150)



BontonAcp=Button(Indexx,text="Aceptar")
BontonAcp.place(x=40,y=300,width=100,height=30)
BontonCanc=Button(Indexx,text="Cancelar")
BontonCanc.place(x=150,y=300,width=100,height=30)



ventana.mainloop()