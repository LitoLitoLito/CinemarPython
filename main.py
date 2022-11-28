from funciones import pedirNumeroEntero, agregarCliente, conexionDB

from funcionesPeliculas import crearFunciones

from peliculas import verPeliculas

from vistas import menuInicio, administrador, administrar

from usuarios import agregarDB, crearUsuario

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
                    pass
                elif opcion == 2:
                    us1 = crearFunciones()
                    conn = conexionDB()
                    agregarDbFunciones(conn, us1.Idfuncion, us1.Idsala, us1.Idpelicula, us1.Horario, us1.Fecha, us1.Estado)
                    salir1=True
                    menuInicio()
                    
                elif opcion == 3:
                    print ("Opcion 3")
                
                elif opcion == 4:
                    conn = conexionDB()
                    verPeliculas(conn)
                    salir1=True
                                        
                elif opcion == 5:
                    print ("Opcion 5")
                
                elif opcion == 6:
                    salir1 = True
                else:
                    print ("Introduce un numero entre 1 y 6")
                            
        else:
            print("Acceso DENEGADO")
        menuInicio()
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
        




