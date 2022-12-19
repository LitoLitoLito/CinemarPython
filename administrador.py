from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector
from PIL import Image, ImageTk

# CONFIGURACIÓN DE VENTANA
#------------------------------------
root = Tk()
root.geometry("1200x600+200+50");
root.title("Sistema de CRUD");

# MARCO DE LA PANTALLA PRINCIPAL
tela_principal = Frame(root, bg="pale green")
tela_principal.place(x=0,y=0,width=1200,height=600)
#------------------------------------

cine = Image.open('imagenes/cinemar.png')
cine = cine.resize((300,70), Image.ANTIALIAS)
cine = ImageTk.PhotoImage(cine)
l_cine = Label(tela_principal, image=cine, compound=LEFT, anchor='nw', bg="pale green",bd=0,activebackground="#3b3b3b")
l_cine.place(x=550,y=20)

texto_admin = Label(tela_principal, text="Administrador", font=("Arial Black",22),bg="pale green", fg="black")
texto_admin.place(x=220, y=10)

reservas_cuadro = Label(tela_principal, text="Reservas", font=("Arial Black",12),bg="pale green", fg="black")
reservas_cuadro.place(x=1100, y=70)

funciones_cuadro = Label(tela_principal, text="Funciones", font=("Arial Black",12),bg="pale green", fg="black")
funciones_cuadro.place(x=690, y=330)

#-----------------------------------------------
im_admin_crud = Image.open('imagenes/admin_crud.png')
im_admin_crud = im_admin_crud.resize((60,60), Image.ANTIALIAS)
im_admin_crud = ImageTk.PhotoImage(im_admin_crud)
l_admin_crud= Label(tela_principal, image=im_admin_crud, compound=LEFT, anchor='nw', bg="pale green",bd=0,activebackground="#3b3b3b")
l_admin_crud.place(x=80,y=40)

#-----------------------------------------------
# INSERCIÓN Y CARGA DE BOTÓN
reserva_cliente = Image.open('imagenes/reserva_de_clientes.png')
reserva_cliente  = reserva_cliente.resize((190,30), Image.ANTIALIAS)
reserva_cliente  = ImageTk.PhotoImage(reserva_cliente )
reserva = Button(tela_principal, image=reserva_cliente, compound=LEFT, anchor='nw', 
bg="pale green",bd=0,activebackground="pale green") #command=insert
reserva.place(x=15,y=130)

reserva_particular = Image.open('imagenes/reserva_particular.png')
reserva_particular  = reserva_particular.resize((190,30), Image.ANTIALIAS)
reserva_particular  = ImageTk.PhotoImage(reserva_particular)
particular = Button(tela_principal, image=reserva_particular, compound=LEFT, anchor='nw', 
bg="pale green",bd=0,activebackground="pale green") #command=insert
particular.place(x=15,y=390)

crear_funcion = Image.open('imagenes/crear_una_funcion.png')
crear_funcion  = crear_funcion.resize((190,30), Image.ANTIALIAS)
crear_funcion  = ImageTk.PhotoImage(crear_funcion)
crear_f = Button(tela_principal, image=crear_funcion, compound=LEFT, anchor='nw', 
bg="pale green",bd=0,activebackground="pale green") #command=insert
crear_f.place(x=15,y=170)

modificar_funcion = Image.open('imagenes/modificar_una_funcion.png')
modificar_funcion = modificar_funcion.resize((190,30), Image.ANTIALIAS)
modificar_funcion = ImageTk.PhotoImage(modificar_funcion)
modificar_f = Button(tela_principal, image=modificar_funcion, compound=LEFT, anchor='nw', 
bg="pale green",bd=0,activebackground="pale green") #command=insert
modificar_f.place(x=15,y=250)

modificar_funcion1 = Entry(tela_principal, width=23,font=("Arial",11))
modificar_funcion1.place(x=15, y=290)

eliminar_sala = Image.open('imagenes/eliminar_una_sala.png')
eliminar_sala = eliminar_sala.resize((190,30), Image.ANTIALIAS)
eliminar_sala = ImageTk.PhotoImage(eliminar_sala)
eliminar_s = Button(tela_principal, image=eliminar_sala, compound=LEFT, anchor='nw', 
bg="pale green",bd=0,activebackground="pale green") #command=insert
eliminar_s.place(x=15,y=320)

eliminar_sala1 = Entry(tela_principal, width=23,font=("Arial",11))
eliminar_sala1.place(x=15, y=360)

descuento_porcentaje = Image.open('imagenes/descuento_porcentaje.png')
descuento_porcentaje = descuento_porcentaje.resize((190,30), Image.ANTIALIAS)
descuento_porcentaje = ImageTk.PhotoImage(descuento_porcentaje)
descuento_p = Button(tela_principal, image=descuento_porcentaje, compound=LEFT, anchor='nw', 
bg="pale green",bd=0,activebackground="pale green") #command=insert
descuento_p.place(x=15,y=460)

descuento_porcentaje1 = Entry(tela_principal, width=23,font=("Arial",11))
descuento_porcentaje1.place(x=15, y=500)

ver_funciones = Image.open('imagenes/ver_funciones.png')
ver_funciones = ver_funciones.resize((190,30), Image.ANTIALIAS)
ver_funciones = ImageTk.PhotoImage(ver_funciones)
ver_f = Button(tela_principal, image=ver_funciones, compound=LEFT, anchor='nw', 
bg="pale green",bd=0,activebackground="pale green") #command=insert
ver_f.place(x=15,y=210)

reserva_particular1 = Entry(tela_principal, width=23,font=("Arial",11))
reserva_particular1.place(x=15, y=430)

#-----------------------------------------------
# Funciones en cartelera
chicas_pesadas = Image.open('imagenes/chicas_pesadas_3_0.png')
chicas_pesadas = chicas_pesadas.resize((150,75), Image.ANTIALIAS)
chicas_pesadas = ImageTk.PhotoImage(chicas_pesadas)
chicas = Button(tela_principal, image=chicas_pesadas, compound=LEFT, anchor='nw', 
bg="pale green",bd=0,activebackground="pale green") #command=insert
chicas.place(x=800,y=390)

enola = Image.open('imagenes/enola_holmes_4_0.png')
enola = enola.resize((150,75), Image.ANTIALIAS)
enola = ImageTk.PhotoImage(enola)
enola_1 = Button(tela_principal, image=enola, compound=LEFT, anchor='nw', 
bg="pale green",bd=0,activebackground="pale green") #command=insert
enola_1.place(x=1000,y=390)

chihiro = Image.open('imagenes/chihiro_5_0.png')
chihiro = chihiro.resize((150,75), Image.ANTIALIAS)
chihiro = ImageTk.PhotoImage(chihiro)
chihiro_1 = Button(tela_principal, image=chihiro, compound=LEFT, anchor='nw', 
bg="pale green",bd=0,activebackground="pale green") #command=insert
chihiro_1.place(x=800,y=500)

mowgli = Image.open('imagenes/mowgli_relatos_6_0.png')
mowgli = mowgli.resize((150,75), Image.ANTIALIAS)
mowgli = ImageTk.PhotoImage(mowgli)
mowgli_1 = Button(tela_principal, image=mowgli, compound=LEFT, anchor='nw', 
bg="pale green",bd=0,activebackground="pale green") #command=insert
mowgli_1.place(x=1000,y=500)

todos_los_dias = Label(tela_principal, text="Todos los Días a las 16:00:00 - Sala --> 1", font=("Arial Black",11),bg="pale green", fg="black")
todos_los_dias.place(x=800, y=360)
todos_los_dias_1 = Label(tela_principal, text="Todos los Días a las 21:00:00 - Sala --> 2", font=("Arial Black",11),bg="pale green", fg="black")
todos_los_dias_1.place(x=800, y=470)

#Ventana Muestra la ventana de datos de la base de datos y su número de columnas
tv1=ttk.Treeview(tela_principal,columns=("IdReserva","Horario","IdFuncion","IdSala","IdPelicula", "IdUsuario","Nombre", "Fecha","Precio", "Estado"), show='headings')
tv1.place(x=215, y=100)
#coluna
tv1.column("IdReserva",minwidth=0,width=120)
tv1.column("Horario",minwidth=0,width=80)
tv1.column("IdFuncion",minwidth=0,width=100)
tv1.column("IdSala",minwidth=0,width=100)
tv1.column("IdPelicula",minwidth=0,width=50)
tv1.column("IdUsuario",minwidth=0,width=120)
tv1.column("Nombre",minwidth=0,width=100)
tv1.column("Fecha",minwidth=0,width=100)
tv1.column("Precio",minwidth=0,width=100)
tv1.column("Estado",minwidth=0,width=100)
# Encabezamiento
tv1.heading("IdReserva",text="IdReserva")
tv1.heading("Horario",text="Horario")
tv1.heading("IdFuncion",text="IdFuncion")
tv1.heading("IdSala",text="IdSala")
tv1.heading("IdPelicula",text="IdPelicula")
tv1.heading("IdUsuario",text="IdUsuario")
tv1.heading("Nombre",text="Nombre")
tv1.heading("Fecha",text="Fecha")
tv1.heading("Precio",text="Precio")
tv1.heading("Estado",text="Estado")

#línea
ttk.Separator(tela_principal, orient=HORIZONTAL).place(x=250,y=345,  width=400)

tv=ttk.Treeview(tela_principal,columns=("IdFuncion","IdSala","IdPelicula","Horario","Fecha", "Estado"), show='headings')
tv.place(x=215, y=360)
#coluna
tv.column("IdFuncion",minwidth=0,width=120)
tv.column("IdSala",minwidth=0,width=80)
tv.column("IdPelicula",minwidth=0,width=100)
tv.column("Horario",minwidth=0,width=100)
tv.column("Fecha",minwidth=0,width=50)
tv.column("Estado",minwidth=0,width=120)

# Encabezamiento
tv.heading("IdFuncion",text="IdFuncion")
tv.heading("IdSala",text="IdSala")
tv.heading("IdPelicula",text="IdPelicula")
tv.heading("Horario",text="Horario")
tv.heading("Fecha",text="Fecha")
tv.heading("Estado",text="Estado")


root.mainloop()