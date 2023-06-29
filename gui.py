from tkinter import *

root = Tk()
root.title('Botón On/Off')
root.geometry("600x300")

# Variable global para saber si el estado del botón es ON/OFF
is_on = True

# Crear Label
my_label = Label(root,
    text = "El estatus del botón es ON",
    fg = "green",
    font = ("Helvetica", 32))

my_label.pack(pady = 20)

# Función para el botón
def switch():
    # Usamos la variable global para saber el estado actual del botón
    global is_on
    
    # Determina si el botón está encendido o apagado
    if is_on:
        on_button.config(text = off)
        my_label.config(text = "El estatus del botón es OFF",
                        fg = "red")
        is_on = False
    else:
        on_button.config(text = on)
        my_label.config(text = "El estatus del botón es ON", fg = "green")
        is_on = True

# Definir texto del botón
on = 'Botón ON'
off = 'Botón OFF'


on_button = Button(root, text=on, bd = 2,
                command = switch)
on_button.pack(pady = 50)
root.mainloop()