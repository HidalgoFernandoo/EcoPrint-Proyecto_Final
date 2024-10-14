import mysql.connector


def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost", user="root", password="root", database="ecoprint"
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
        return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectarse: {error}")
        return None
