from funciones import crearUsuario, agregarCliente, pedirNumeroEntero

from vistas import menuInicio

menuInicio()
salir = False
opcion = 0
 
while not salir: 
    print ("Elige una opcion") 
    opcion = pedirNumeroEntero() 
    if opcion == 1:
        email1 = agregarCliente()
        crearUsuario(email1)
        menuInicio()
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 4")
        




