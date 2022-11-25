import mysql.connector

from usuarios import Usuario

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

def crearUsuario(email1):
    idusuario = email1
    clave = (input("Ingrese Clave de Ingreso ---> "))
    nombre = (input("Ingrese Nombre ---> "))
    apellido = (input("Ingrese Apellido ---> "))
    estado = 1
    fechaNacimiento = (input("Ingrese Fecha Nacimiento AAAA-MM-DD ---> "))
    celular = (input("Ingrese número celular ---> "))
    us = Usuario(idusuario,clave,nombre,apellido,estado,fechaNacimiento,celular)
    print(us.idusuario)
    print(us.clave)
    print(us.nombre)
    print(us.apellido)
    print(us.estado)
    print(us.fechanacimiento)
    print(us.celular)

def agregarCliente():
            print("*************************************************")
            print("Ingrese su correo electronico")
            print("Recuerde que será su USUARIO ---> ")
            print("*************************************************")
            email = input("---> ")
            existe = validarCliente(email)
            while (existe==True):
                print("*************************************************")
                print("Ya existe un usuario con ese correo")
                print("Ingrese otra direccion de e-mail")
                print("*************************************************")
                email = input("---> ")
                existe = validarCliente(email)
            return email        

def validarCliente(email):
            conexion = mysql.connector.connect(host='localhost', user='root',password='20205701*', db='cinepython')
            with conexion.cursor() as cursor:
                consulta = "SELECT IdUsuario FROM usuarios"
                cursor.execute(consulta)
                record = cursor.fetchall()
                for i in range(len(record)):
                    if record [i] [0] == email:
                        conexion.close()
                        return True
            conexion.close()
            return False
            