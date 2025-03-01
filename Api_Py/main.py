from fastapi import FastAPI
import pypyodbc as odbc 
from Conn import get_db_connection

app=FastAPI()


@app.get("/")  #Realiza conexion a base de datos y trae todos sus registros
def root():

    connection = get_db_connection()

    #connection = odbc.connect(connection_string)
    #print("Conexión exitosa!")

    # Crear un cursor
    cursor = connection.cursor()

    # Ejecutar una consulta en base de datos SQL 
    cursor.execute("SELECT * FROM Tasks")

    # Obtener y mostrar los resultados
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    return{"message": "Registros en base de datos de tabla Tasks"}


@app.get("/get_tasks") #Funcion para obtener todos los registros de la tabla Tasks
def get_tasks():

    #connection = odbc.connect(connection_string)
    #print("Conexión exitosa!")

    connection = get_db_connection()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Tasks")
    records = cursor.fetchall()

    print(records)

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    return records #Regresamos todos los valores que obtenemos de la base de datos


#@app.post("/add_task") #Funcion para agregar nuevos registros de task (PENDIENTE SIN TERMINAR)
#def add_tasks(task:stg=Form(...)):

    #connection = odbc.connect(connection_string)
    #print("Conexión exitosa!")

    #cursor = connection.cursor()
    #cursor.execute("INSERT INTO Tasks (Title, Description, Status, CreationDate, DueDate) VALUES (%s, %s, 'Pending', '2025-03-01 09:00:00', '2025-03-05 17:00:00'),")
    #records = cursor.fetchall()

    #print(records)

    # Cerrar el cursor y la conexión
    #cursor.close()
    #connection.close()

    #return records #Regresamos todos los valores que obtenemos de la base de datos