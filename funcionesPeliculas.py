class Funciones():
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
    
    