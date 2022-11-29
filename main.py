from funciones import pedirNumeroEntero, agregarCliente, conexionDB

from funcionesPeliculas import crearFunciones

from peliculas import agregarDbPelicula, agregarPelicula, verPeliculas

from vistas import *

from usuarios import agregarDB, crearUsuario, verUsuarios

from funcionesPeliculas import agregarDbFunciones

menuInicio()
salir = False
opcion = 0
 
while not salir: 
    print ("Elige una opcion") 
    opcion = pedirNumeroEntero() 
    if opcion == 1:
        email1 = agregarCliente()
        us = crearUsuario(email1)
        conn = conexionDB()
        agregarDB(conn, us.idusuario, us.clave, us.nombre, us.apellido, us.estado, us.fechanacimiento, us.celular)
        menuInicio()
    elif opcion == 2:
        print ("Opcion 2")
        menuInicio()
    elif opcion == 3:
        print("Ver CARTELERA 3")
        menuInicio()
    elif opcion == 4:
        administrador()
        acceso = int(input())
        if acceso==1234:
            print("Acceso PERMITIDO")
            administrar()
            salir1=False
            while not salir1:
                print ("Elige una opcion") 
                opcion = pedirNumeroEntero() 
                if opcion == 1:
                    print('1.- Crear Salas')
                    administrar()
                elif opcion == 2:
                    us1 = crearFunciones()
                    conn = conexionDB()
                    agregarDbFunciones(conn, us1.Idfuncion, us1.Idsala, us1.Idpelicula, us1.Horario, us1.Fecha, us1.Estado)
                    administrar()
                elif opcion == 3:
                    peliculas()
                    us2 = agregarPelicula()
                    conn = conexionDB()
                    agregarDbPelicula(conn, us2.Titulo, us2.Director, us2.Descripcion, us2.Genero, us2.Duracion)
                    administrar()
                elif opcion == 4:
                        print('4.- Eliminar Películas')
                        administrar()        
                elif opcion == 5:
                    conn = conexionDB()
                    verPeliculas(conn)
                    administrar()
                elif opcion == 6:
                    conn = conexionDB()
                    verUsuarios(conn)
                    administrar() 
                elif opcion == 7:
                    salir1 = True
                else:
                    print ("Introduce un numero entre 1 y 7")
                            
        else:
            print("Acceso DENEGADO")
        menuInicio()
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
        




