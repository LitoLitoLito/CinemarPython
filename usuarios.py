import mysql.connector

from vistas import mostrarUsuarios

class Usuario:
    def __init__(self, IdUsuario, clave, Nombre, Apellido, Estado, FechaNacimiento, Celular):
        self.__IdUsuario = IdUsuario
        self.__clave = clave
        self.__Nombre = Nombre
        self.__Apellido = Apellido
        self.__Estado = Estado
        self.__FechaNacimiento = FechaNacimiento
        self.__Celular = Celular
    
    @property
    def idusuario(self):
        return self.__IdUsuario
    @property
    def clave(self):
        return self.__clave
    @property
    def nombre(self):
        return self.__Nombre
    @property
    def apellido(self):
        return self.__Apellido
    @property
    def estado(self):
        return self.__Estado
    @property
    def fechanacimiento(self):
        return self.__FechaNacimiento
    @property
    def celular(self):
        return self.__Celular

    @idusuario.setter
    def idusuario(self, IdUsuario):
        self.__IdUsuario = IdUsuario
    
    @nombre.setter
    def nombre(self, Nombre):
        self.__Nombre = Nombre
    
    @apellido.setter
    def apellido(self, Apellido):
        self.__Apellido = Apellido
    
    @estado.setter
    def estado(self, Estado):
        self.__Estado = Estado
    @fechanacimiento.setter
    def fechanacimiento(self, FechaNacimiento):
        self.__FechaNacimiento = FechaNacimiento
    
    @celular.setter
    def celular(self, Celular):
            self.__Celular = Celular

def crearUsuario(email1):
    idusuario = (email1)
    clave = (input("Ingrese Clave de Ingreso ---> "))
    nombre = (input("Ingrese Nombre ---> "))
    apellido = (input("Ingrese Apellido ---> "))
    estado = 1
    fechaNacimiento = (input("Ingrese Fecha Nacimiento AAAA-MM-DD ---> "))
    celular = (input("Ingrese número celular ---> "))
    us = Usuario(idusuario,clave,nombre,apellido,estado,fechaNacimiento,celular)
    print(f"Usuario ---> {us.idusuario} ")
    print(f"Clave Personal ---> {us.clave}")
    print(f"Nombre ---> {us.nombre}")
    print(f"Apellido ---> {us.apellido}")
    print(f"Estado ---> {us.estado}")
    print(f"Fecha Nacimiento ---> {us.fechanacimiento}")
    print(f"Celular ---> {us.celular}")
    return us

def agregarDB(conn,idusuario, clave, nombre, apellido, estado, fechanacimiento, celular):
    conexion = conn
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO usuarios (IdUsuario, clave, Nombre, Apellido, Estado, FechaNacimiento, Celular) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(consulta, (idusuario, clave, nombre, apellido, estado, fechanacimiento, celular))
        conexion.commit()
        conexion.close()
    print("****  SE REGISTRO CORRECTAMENTE ***")
    
def verUsuarios(conn):
    conexion = conn
    with conexion.cursor() as cursor:
        consulta = "SELECT * FROM usuarios;"
        cursor.execute(consulta)
        usuarios = cursor.fetchall()
        mostrarUsuarios(usuarios)
        conexion.close()