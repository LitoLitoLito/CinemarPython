import tkinter
from tkinter import *
from tkinter import messagebox

from funciones import conexionDB
from usuarios import Usuario, agregarDB



def menu_pantalla():
    global pantalla
    pantalla = Tk()
    pantalla.configure(bg='pale green')
    pantalla.geometry("300x380")
    pantalla.title("Bienvenidos")
    pantalla.iconbitmap("imagenes/logo.ico")
    
    Label(text="",bg='pale green').pack() 
    image=PhotoImage(file="imagenes/cinemar.png")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()
    Label(text="",bg='pale green').pack() 
    
    Label(text="Acceso al Sistema", bg="navy",fg="white",width="300",height="1",font=("calibri", 15)).pack()
    Label(text="",bg='pale green').pack()    
    
    Button(text="Iniciar Sesión", height="2", width="30", command=inicio_sesion).pack()
    Label(text="",bg='pale green').pack()
    
    Button(text="Registrarse", height="2", width="30", command=registrar).pack()
    
    pantalla.mainloop()   
     
  
def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesión")
    pantalla1.iconbitmap("imagenes/logo.ico")
    pantalla1.configure(bg='pale green')
    
    Label(pantalla1, text="",bg='pale green').pack() 
    Label(pantalla1, text="Por favor ingrese su usuario (e-mail)\n y Contraseña a continuación", bg="navy",fg="white",width="300",height="2",font=("calibri", 12)).pack()
    Label(pantalla1, text="",bg='pale green').pack()    
    
    global nombreusuario_verify
    global contrasenausuario_verify
    
    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()
    
    global nombre_usuario_entry
    global contrasena_usuario_entry
    
    Label(pantalla1, text="Usuario", bg='pale green').pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1,bg='pale green').pack()
    
    Label(pantalla1, text="Contraseña", bg='pale green').pack()
    contrasena_usuario_entry = Entry(pantalla1, show="*" , textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1,bg='pale green').pack()
    
    Button(pantalla1, text="Iniciar Sesión").pack()
    
def registrar():
    global pantalla2
    pantalla2=Toplevel(pantalla)
    pantalla2.geometry("400x500")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("imagenes/logo.ico")
    pantalla2.configure(bg='pale green')
    
    global nombreusuario_entry, contrasena_entry, nombre_entry, apellido_entry, fechaNacimiento_entry, celular_entry
    
    nombreusuario_entry=StringVar()
    contrasena_entry=StringVar()
    nombre_entry=StringVar()
    apellido_entry=StringVar()
    fechaNacimiento_entry=StringVar()
    celular_entry=StringVar()
    
    Label(pantalla2, text="Por favor ingrese un Usuario (e-mail) y Contraseña\n de su elección y otros datos para el registro al Sistema", bg="navy",fg="white",width="300",height="2",font=("calibri", 12)).pack()
    Label(pantalla2,bg='pale green').pack()
    
    Label(pantalla2, text="Usuario", bg='pale green').pack()
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2,bg='pale green').pack()
    
    Label(pantalla2, text="Contraseña", bg='pale green').pack()
    contrasena_entry = Entry(pantalla2, show="*")
    contrasena_entry.pack()
    Label(pantalla2,bg='pale green').pack()
    
    Label(pantalla2, text="Nombre", bg='pale green').pack()
    nombre_entry = Entry(pantalla2,)
    nombre_entry.pack()
    Label(pantalla2,bg='pale green').pack()
    
    Label(pantalla2, text="Apellido", bg='pale green').pack()
    apellido_entry = Entry(pantalla2,)
    apellido_entry.pack()
    Label(pantalla2,bg='pale green').pack()
    
    Label(pantalla2, text="Fecha Nacimiento (AAAA-MM-DD)", bg='pale green').pack()
    fechaNacimiento_entry = Entry(pantalla2,)
    fechaNacimiento_entry.pack()
    Label(pantalla2,bg='pale green').pack()
    
    Label(pantalla2, text="Celular", bg='pale green').pack()
    celular_entry = Entry(pantalla2,)
    celular_entry.pack()
    Label(pantalla2,bg='pale green').pack()
    
    Button(pantalla2, text="Registrar", command=validarCliente).pack()
    
                
    
    
    
def validarCliente():
            conexion = conexionDB()
            with conexion.cursor() as cursor:
                consulta = "SELECT IdUsuario FROM usuarios"
                cursor.execute(consulta)
                record = cursor.fetchall()
                for i in range(len(record)):
                    if record [i] [0] == nombreusuario_entry.get():
                        conexion.close()
                        print("True - True - True ")
                        messagebox.showinfo(message="Usuario Existente - Ingrese otro e-mail", title="Aviso")
                        pantalla2.destroy()
                        registrar()
                sepuedeAgregar()
            conexion.close()
            
def sepuedeAgregar():              
    idusuario =  nombreusuario_entry.get()
    clave = contrasena_entry.get()
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    estado = 1
    fechaNacimiento = fechaNacimiento_entry.get()
    celular = celular_entry.get()
    us = Usuario(idusuario,clave,nombre,apellido,estado,fechaNacimiento,celular)
    conn = conexionDB()
    agregarDB(conn, us.idusuario, us.clave, us.nombre, us.apellido, us.estado, us.fechanacimiento, us.celular)
    messagebox.showinfo(message="SE REGISTRO CORRECTAMENTE", title="Aviso")
    pantalla2.destroy()

                

    

menu_pantalla()