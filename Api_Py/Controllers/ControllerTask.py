from Conn import get_db_connection
from Models.Task import TaskCreate
import pypyodbc

def Root():
    connection = get_db_connection() #Mandamos a llamar funcion para crear conexion

    # Crear un cursor
    cursor = connection.cursor()

    # Ejecutar una consulta en base de datos SQL 
    cursor.execute("SELECT * FROM Tasks")

    # Obtener y mostrar los resultados
    rows = cursor.fetchall()
    #for row in rows:
        #print(row)

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    print("Funcion desde mi controlador")

    return rows