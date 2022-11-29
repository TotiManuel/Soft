def AbrirServidor():
	os.system("cd Servidor && python server_locar.py")

def AbrirNotas():
	os.system("cd Servidor && python notas.py")

def Google():
	os.system("cd Servidor && cd Atajos && python abrir_google.py")

def ObtenerIp():
	ip=socket.gethostbyname(socket.gethostname()) + socket.gethostname()
	ip=Label(root, text=ip)
	ip.place(x=10, y=50)

def combobox():
    cbx.bind("<<ComboboxSelected>>", "changed")
    if (cbx.get()=="Notas"):
    	AbrirNotas()
    elif(cbx.get()=="Abrir Google"):
    	Google()
    elif(cbx.get()=="Iniciar Servidor"):
    	AbrirServidor()
    elif(cbx.get()=="Obtener IP"):
    	ObtenerIp()

import tkinter
from tkinter import *
from tkinter import ttk
import os
import socket

root=Tk()
root.geometry("300x100")
root.title("JMM")
ventana=ttk.Frame(root)
ventana.place()

cbx=ttk.Combobox(values=["Iniciar Servidor", "Abrir Google", "Notas","Obtener IP"])
cbx.set("Iniciar Servidor")
cbx.configure(width=25)
cbx.place(x=10, y=10)


boton=Button(root, text="Continuar", command=combobox, background="#b4b4b4")
boton.config(bd=5, relief=RAISED)
boton.place(x=10, y=40, width=150, height=50)


root.mainloop()
