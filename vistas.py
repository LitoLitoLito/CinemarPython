def menuInicio():
        print('--------------------------------------')
        print('            MENU INICIO            ')
        print('--------------------------------------')
        print('1.- Registrarse')
        print('2.- Reservar Función')
        print('3.- Ver Funciones')
        print('4.- Administrar')
        print('5.- Salir')
        print('--------------------------------------')
        
def menuReservarFuncion():
        print('--------------------------------------')
        print('            RESERVAR FUNCIONES            ')
        print('--------------------------------------')
        print('Funciones Activas, elija Función')
        print('Ejemplo --- Función "X" ---> Numero de Opción ')
        print('--------------------------------------')
        

def administrar():
        print('--------------------------------------')
        print('            MENU ADMINISTRAR            ')
        print('--------------------------------------')
        print('1.- Crear Salas')
        print('2.- Crear Funciones')
        print('3.- Agregar y/o eliminar Películas')
        print('4.- Ver Peliculas')
        print('5.- Ver Clientes Registrados')
        print('6.- Salir')
        print('--------------------------------------')

def administrador():
        print('--------------------------------------')
        print('     INGRESE CLAVE DE ACCESO 1234     ')
        print('--------------------------------------')

def prueba():
        print(" ******  EXITOSA PRUEBA ******")
        
def mostrarPeliculas(peliculas):
        
        print("------------------------------------")
        print(" TODAS LAS PELICULAS DISPONIBLES ")
        print("------------------------------------")
        lst = list(map(list,peliculas))
        for i in range(len(lst)):
                print("------------------------------------")
                print(f"Id ---> {lst[i][0]}) Titulo ---> {lst[i][1]}")
                print(f"Director ---> {lst[i][2]}")
                print(f"Descripcion ---> {lst[i][3]}")
                print(f"Género ---> {lst[i][4]}")
                print(f"Duración ---> {lst[i][5]}")
                print(f"Estado ---> {lst[i][6]}")
                print("------------------------------------")
                print("------------------------------------")
                print("------------------------------------")
                