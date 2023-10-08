from tkinter import *

ventana = Tk()
ventana.title("Calculadora Basica")
ventana.configure(bg='black')
#i = 0

#entrada
e_texto = Entry(ventana, font = ("Arial 24"),fg=("purple"),bg=("white"))
e_texto.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady=5)

i = 0

def click_boton(valor):
    global i
    e_texto.insert(i,valor)
    i += 1
    
def borrar():
    e_texto.delete(0, END)
    i = 0

def Eliminar():
    global i
    i= i-1
    e_texto.delete(i,END)

def operacion():
    ecuacion = e_texto.get()    
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0
    
def Sci():
    numero = e_texto.get()
    numero_notacion_cientifica = "{:.2e}".format(float(numero))
    e_texto.delete(0, END)
    e_texto.insert(0, numero_notacion_cientifica)
    i = 0

def activar():
    estado_actual = boton_eliminar.cget('state')
    nuevo_estado = 'normal' if estado_actual == 'disabled' else 'disabled'
    boton_eliminar.configure(state=nuevo_estado)
    

boton1 = Button(ventana, text="1", width=5, height=2, cursor="hand2", bg="yellow", command=lambda:click_boton(1))
boton2 = Button(ventana, text="2", width=5, height=2, bg="red", fg="white", cursor="hand2", command=lambda:click_boton(2))
boton3 = Button(ventana, text="3", width=5, height=2, cursor="hand2", bg="yellow", command=lambda:click_boton(3))
boton4 = Button(ventana, text="4", width=5, height=2, bg="red", fg="white", cursor="hand2", command=lambda:click_boton(4))
boton5 = Button(ventana, text="5", width=5, height=2, cursor="hand2", bg="yellow", command=lambda:click_boton(5))
boton6 = Button(ventana, text="6", width=5, height=2, bg="red", fg="white", cursor="hand2", command=lambda:click_boton(6))
boton7 = Button(ventana, text="7", width=5, height=2, cursor="hand2", bg="yellow", command=lambda:click_boton(7))
boton8 = Button(ventana, text="8", width=5, height=2, bg="red", fg="white", cursor="hand2", command=lambda:click_boton(8))
boton9 = Button(ventana, text="9", width=5, height=2, cursor="hand2", bg="yellow", command=lambda:click_boton(9))
boton0 = Button(ventana, text="0", width=5, height=2, bg="red", fg="white", command=lambda:click_boton(0))

boton_borrar = Button(ventana, text="AC", width=5, height=2, bg="yellow", command=lambda:borrar())
boton_Parentesis1 = Button(ventana, text="(", width=5, height=2,  bg="red", fg="white", command=lambda:click_boton("("))
boton_Parentesis2 = Button(ventana, text=")", width=5, height=2, bg="yellow", command=lambda:click_boton(")"))
boton_Punto = Button(ventana, text=".", width=5, height=2, bg="yellow", command=lambda:click_boton("."))
boton_Sci = Button(ventana,text="Sci", width=5, height=2, bg="red", fg="white", command=lambda:Sci())
boton_eliminar = Button(ventana, text="<-", width=5, height=2, bg="red", fg="white", command=lambda:Eliminar())

boton_div = Button(ventana, text="/", width=5, height=2, bg="red", fg="white", command=lambda:click_boton("/") )
boton_mult = Button(ventana, text="x", width=5, height=2, bg="red", fg="white", command=lambda:click_boton("*"))
boton_suma = Button(ventana, text="+", width=5, height=2, bg="yellow", command=lambda:click_boton("+"))
boton_resta = Button(ventana, text="-", width=5, height=2, bg="red", fg="white", command=lambda:click_boton("-"), cursor="")
boton_igual = Button(ventana, text="=", width=5, height=2,  bg="yellow",command=lambda:operacion())
boton_activar = Button(ventana, text= "Active", width= 5, height=2, bg="yellow", command=lambda:activar())

#asignamos colocacion de elementos en ventana
boton_borrar.grid(row=1, column=3, padx=5, pady=5)
boton_Parentesis1.grid(row=1, column=0, padx=5, pady=5)
boton_Parentesis2.grid(row=1, column=1, padx=5, pady=5)
boton_div.grid(row=1, column=2, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_suma.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_resta.grid(row=4, column=3, padx=5, pady=5)
boton_eliminar.grid(row=1, column=4, padx=5,pady=5)

boton0.grid(row=5, column=0, padx=5, pady=5)
boton_Punto.grid(row=5, column=1, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)
boton_Sci.grid(row=5, column=2, padx=5, pady=5)
boton_activar.grid(row=2, column=4, padx=5, pady=5)




ventana.mainloop()