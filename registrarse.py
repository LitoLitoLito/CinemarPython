from os import system
import tkinter as tk
import tkinter.font as tkFont

from funciones import agregarCliente, conexionDB
from usuarios import agregarDB, crearUsuario
from vistas import administrador, administrar, menuInicio

class App:
    def __init__(self, root):
        #setting title
        root.title("Menu Inicio")
        #setting window size
        width=328
        height=457
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_334=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_334["font"] = ft
        GMessage_334["fg"] = "#333333"
        GMessage_334["justify"] = "center"
        GMessage_334["text"] = "INICIO"
        GMessage_334.place(x=0,y=30,width=320,height=30)

        GButton_365=tk.Button(root)
        GButton_365["bg"] = "#cc0000"
        ft = tkFont.Font(family='Times',size=11)
        GButton_365["font"] = ft
        GButton_365["fg"] = "#ffffff"
        GButton_365["justify"] = "center"
        GButton_365["text"] = "Registrarse"
        GButton_365.place(x=10,y=70,width=305,height=30)
        GButton_365["command"] = self.registrar
        
        GButton_365=tk.Button(root)
        GButton_365["bg"] = "#cc0000"
        ft = tkFont.Font(family='Times',size=11)
        GButton_365["font"] = ft
        GButton_365["fg"] = "#ffffff"
        GButton_365["justify"] = "center"
        GButton_365["text"] = "Reservar Función"
        GButton_365.place(x=10,y=105,width=305,height=30)
        GButton_365["command"] = self.reservarFuncion
        
        GButton_365=tk.Button(root)
        GButton_365["bg"] = "#cc0000"
        ft = tkFont.Font(family='Times',size=11)
        GButton_365["font"] = ft
        GButton_365["fg"] = "#ffffff"
        GButton_365["justify"] = "center"
        GButton_365["text"] = "Ver Funciones"
        GButton_365.place(x=10,y=140,width=305,height=30)
        GButton_365["command"] = self.verFunciones
        
        GButton_365=tk.Button(root)
        GButton_365["bg"] = "#cc0000"
        ft = tkFont.Font(family='Times',size=11)
        GButton_365["font"] = ft
        GButton_365["fg"] = "#ffffff"
        GButton_365["justify"] = "center"
        GButton_365["text"] = "Administrar"
        GButton_365.place(x=10,y=175,width=305,height=30)
        GButton_365["command"] = self.administrador
        
        GButton_365=tk.Button(root)
        GButton_365["bg"] = "#cc0000"
        ft = tkFont.Font(family='Times',size=11)
        GButton_365["font"] = ft
        GButton_365["fg"] = "#ffffff"
        GButton_365["justify"] = "center"
        GButton_365["text"] = "Salir"
        GButton_365.place(x=10,y=210,width=305,height=30)
        GButton_365["command"] = self.quit
        
    def quit(self):
        root.destroy()

    def registrar(self):
        print("command")
        email1 = agregarCliente()
        us = crearUsuario(email1)
        conn = conexionDB()
        agregarDB(conn, us.idusuario, us.clave, us.nombre, us.apellido, us.estado, us.fechanacimiento, us.celular)
        print("command EXITOSO")
    
    def reservarFuncion(self):
        system("cls")
        print ("Opcion 2")
        menuInicio()
    
    def verFunciones(self):
        system("cls")
        print("Ver CARTELERA 3")
        menuInicio()
    
    def administrador(self):
        system("cls")
        administrador()
        acceso = int(input())
        if acceso==1234:
            print("Acceso PERMITIDO")
            administrar()
            salir1=False


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()