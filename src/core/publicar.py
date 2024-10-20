# Lógica publicaciones
from database.conexion import *


def subir_publicacion_a_bd(
    titulo, descripcion, ubicacion, fecha_creacion, fecha_evento, creador
):
    try:
        sql = "insert into publicaciones values(null,%s, %s, %s, %s, NULL, %s, 0, %s)"
        valores = (
            titulo,
            descripcion,
            ubicacion,
            fecha_creacion,
            fecha_evento,
            creador,
        )
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

    except mysql.connector.Error as error:
        print(f"Ocurrió un error {error}")
