import mysql.connector


from usuarios import Usuario

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero ---> "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero')
    return num

def conexionDB():
    try:
        conexion = mysql.connector.connect(host='localhost', user='root',password='20205701*', db='cinepython')
        return conexion
    except (mysql.err.OperationalError, mysql.err.InternalError) as e: print("Ocurrió un error al conectar: ", e)
    

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

def validarCliente():
            conexion = conexionDB()
            with conexion.cursor() as cursor:
                consulta = "SELECT IdUsuario FROM usuarios"
                cursor.execute(consulta)
                record = cursor.fetchall()
                for i in range(len(record)):
                    if record [i] [0] == nombreusuario_entry:
                        conexion.close()
                        print("True - True - True ")
                        return True
            conexion.close()
            print("False - False - False ")
            return False
