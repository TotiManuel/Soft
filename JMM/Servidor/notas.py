from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("500x200")
root.title("NOTAS")

ventana=ttk.Frame(root)
ventana.place()

label_nota1=Label(root, text="1) Terminar Curso Prep Henry")
label_nota1.place(x=10,y=10)

label_nota2=Label(root, text="2) Trabajar en el Proyecto Gestion Bomberos")
label_nota2.place(x=10,y=30)

label_nota3=Label(root, text="3) Hacer programa para el registro del pali")
label_nota3.place(x=10,y=50)

label_nota4=Label(root, text="4) Actualizar mi programa")
label_nota4.place(x=10,y=70)

label_nota5=Label(root, text="5) Hacer Pagina de la Clinica Fusavim")
label_nota5.place(x=10,y=90)

label_nota6=Label(root, text="6) Aprender React")
label_nota6.place(x=10,y=110)

label_nota7=Label(root, text="7) Recordar Lenguajes")
label_nota7.place(x=10,y=130)

root.mainloop()
