

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

