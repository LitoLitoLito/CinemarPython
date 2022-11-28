from vistas import mostrarPeliculas


class Peliculas:
    def __init__(self, IdPelicula, Titulo, Director, Descripcion, Genero, Duracion, Estado):
        self.__IdPelicula = IdPelicula
        self.__Titulo = Titulo
        self.__Director = Director
        self.__Descripcion = Descripcion
        self.__Genero = Genero
        self.__Duracion = Duracion
        self.__Estado = Estado
    
    @property
    def Idpelicula(self):
        return self.__IdPelicula
    @Idpelicula.setter
    def Idpelicula(self, IdPelicula):
        self.__IdPelicula = IdPelicula

    @property
    def Estado(self):
        return self.__Estado
    @Estado.setter
    def Estado(self, Estado):
        self.__Estado = Estado

    @property
    def Duracion(self):
        return self.__Duracion
    @Duracion.setter
    def Duracion(self, Duracion):
        self.__Duracion = Duracion

    @property
    def Genero(self):
        return self.__Genero
    @Genero.setter
    def Genero(self, Genero):
        self.__Genero = Genero

    @property
    def Descripcion(self):
        return self.__Descripcion
    @Descripcion.setter
    def Descripcion(self, Descripcion):
        self.__Descripcion = Descripcion
    
    @property
    def Director(self):
        return self.__Director
    @Director.setter
    def Director(self, Director):
        self.__Director = Director

    @property
    def Titulo(self):
        return self.__Titulo
    @Titulo.setter
    def Titulo(self, Titulo):
        self.__Titulo = Titulo

def verPeliculas(conn):
    conexion = conn
    with conexion.cursor() as cursor:
        consulta = "SELECT * FROM peliculas;"
        cursor.execute(consulta)
        peliculas = cursor.fetchall()
        mostrarPeliculas(peliculas)