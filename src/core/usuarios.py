# Lógica de registro e inicio sesión
from database.conexion import *
import bcrypt  # Para enscriptar contraseñas


class Usuario:
    def __init__(self, correo, contrasena):
        self.correo = correo
        self.__contrasena = contrasena

    def encriptar_contrasena(self):
        # Genera una cadena de texto aleatoria en formato de bytes
        salt = bcrypt.gensalt()
        self.__hashed = bcrypt.hashpw(self.__contrasena.encode("utf-8"), salt)
        return self.__hashed

    def registrar_usuario(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        try:
            self.__hashed = self.encriptar_contrasena()
            valores = (self.correo, self.__hashed, self.nombre, self.apellido)
            sql = "insert into usuarios values(null, %s, %s, %s, %s)"

            conexion = conectar_db()
            cursor = conexion.cursor()

            cursor.execute(sql, valores)  # Pushea los usuarios
            conexion.commit()  # Guarda la base de datos
            conexion.close()  # Cierra la conexion

        except mysql.connector.Error as error:
            print("Ocurrio un error al guardar los datos", error)

    def verificar_usuario(self, correo_ingresado, contrasena_ingresada):
        try:
            self.__contrasena_ingresada = contrasena_ingresada
            conexion = conectar_db()
            cursor = conexion.cursor()

            consulta = "SELECT contrasena FROM usuarios WHERE correo = %s"
            cursor.execute(consulta, (correo_ingresado,))
            resultado = (
                cursor.fetchone()
            )  # Devuelve la primer fila con los valores, si no lo encuentra devuelve none

            cursor.close()
            conexion.close()

            if resultado:
                self.__hashed = resultado[0]  # Obtiene la contraseña del resultado
                if bcrypt.checkpw(
                    self.__contrasena_ingresada.encode("utf-8"), self.__hashed.encode("utf-8")
                ):
                    return True
                else:
                    return False
            else:
                return False

        except mysql.connector.Error as error:
            print("Ocurrio un error al verificar los datos", error)
