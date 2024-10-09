import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="bhpcw7xr6yo5qhopcadr-mysql.services.clever-cloud.com",      
            user="uxibc4wewbdlw4ck",       
            password="Z7NCbwQlWkKVStxYBKgP", 
            database="bhpcw7xr6yo5qhopcadr" 
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos")
        return conn
    except mysql.connector.Error as err:
        print(f"Error al conectarse: {err}")
        return None
