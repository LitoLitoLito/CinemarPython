from funciones import pedirNumeroEntero, agregarCliente, conexionDB

from vistas import menuInicio

from usuarios import agregarDB, crearUsuario

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
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        print("Opcion 4")
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
        




