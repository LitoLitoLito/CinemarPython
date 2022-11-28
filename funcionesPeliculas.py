from vistas import prueba


class Funciones:
    def __init__(self, idFuncion, idSala, idPelicula, horario, fecha, estado):
        self.__idFuncion = idFuncion
        self.__idSala = idSala
        self.__idPelicula = idPelicula
        self.__horario = horario
        self.__fecha = fecha
        self.__estado = estado
    
    @property
    def Idfuncion(self):
        return self.__idFuncion
    @Idfuncion.setter
    def Idfuncion(self, idFuncion):
        self.__idFuncion = idFuncion
    
    @property
    def Idsala(self):
        return self.__idSala
    @Idsala.setter
    def Idsala(self, idSala):
        self.__idSala = idSala
    
    @property
    def Idpelicula(self):
        return self.__idPelicula
    @Idpelicula.setter
    def Idpelicula(self, idPelicula):
        self.__idPelicula = idPelicula
        
    @property
    def Horario(self):
        return self.__horario
    @Horario.setter
    def Horario(self, horario):
        self.__horario = horario
    
    @property
    def Fecha(self):
        return self.__fecha
    @Fecha.setter
    def Fecha(self, fecha):
        self.__fecha = fecha
    
    @property
    def Estado(self):
        return self.__estado
    @Estado.setter
    def Estado(self, estado):
        self.__estado = estado
    
def crearFunciones():
    print("*************************************************")
    print("Ingrese Número de Funcion ---> ")
    print("*************************************************")
    idfuncion = int(input())
    print("*************************************************")
    print("Ingrese (1) Sala 2d ó (2) Sala 3D ---> ")
    print("*************************************************")
    idSala = int(input())
    print("*************************************************")
    print("Ingrese Número de la Pelicula (1 a 13 ---> ")
    print("*************************************************")
    idPelicula = int(input())
    print("*************************************************")
    print("Ingrese Horario de la Función (HH:MM:SS) ---> ");
    print("*************************************************")
    horario = input()
    print("*************************************************")
    print("Ingrese Fecha de la Función (AA-MM-DD) ---> ");
    print("*************************************************")
    fecha = input()
    estado = 1
    us1 = Funciones(idfuncion, 
                   idSala, 
                   idPelicula, 
                   horario, 
                   fecha, 
                   estado)
    return us1

def agregarDbFunciones(conn, idfuncion, idSala, idPelicula, horario, fecha, estado):
    conexion = conn
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO funciones (IdFuncion, IdSala, IdPelicula, Horario, Fecha, Estado) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(consulta, (idfuncion, idSala, idPelicula, horario, fecha, estado))
        conexion.commit()
        conexion.close()
    print("****  SE REGISTRO CORRECTAMENTE ***")