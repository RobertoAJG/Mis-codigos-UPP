#cofigo para experimentar con MessageBox
from tkinter import *
from tkinter import messagebox

ventana = Tk ()
###
def mensaje():
    i=0
    messagebox.showinfo("Pinche gente","Dice no tocar")

def mensaje1():
    i=0
    messagebox.showinfo("Recordatorio","Toma agua uwu")
    
def mensaje2():
    i=0
    messagebox.showinfo("Hola","Puto si lo lees")
    
def Error():
    messagebox.showerror("Error 404","Meter estancia I")
    
def Adv():
    messagebox.showwarning("Atención","Puedes reporbar el cuatri por no hacer tarea")

ventana.geometry('200x200')

#definimos componentes de ventana
boton_MSG = Button(ventana, text= "No tocar", command=mensaje)
boton_MSG1= Button(ventana, text="Presioname", command=mensaje1)
boton_MSG2= Button(ventana, text="Presionar", command=mensaje2)
boton_err= Button(ventana, text="click para ver el error",command=Error)
Boton_adv= Button(ventana, text="Urgente", command=Adv)

#definimos posicion en ventana de los controles o widgets
#boton_MSG.pack()
#boton_MSG1.pack()
#boton_MSG2.pack()
#boton_err.pack()
#Boton_adv.pack()
boton_MSG.place(x=35, y=30)
boton_MSG1.place(x=35, y=60)
boton_MSG2.place(x=35, y=90)
boton_err.place(x=35, y=120)
Boton_adv.place(x=35, y=150)
####
ventana.mainloop()