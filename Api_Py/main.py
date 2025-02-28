from fastapi import FastAPI
import pypyodbc as odbc 

connection_string = (
    "DRIVER={SQL Server};"           #{ODBC Driver 17 for SQL Server}
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=Py_&_net_&_Angular;"
    "UID=User_apps;"
    "PWD=1234;"
)

app=FastAPI()



@app.get("/")
def root():
    connection = odbc.connect(connection_string)
    print("Conexión exitosa!")

    # Crear un cursor
    cursor = connection.cursor()

    # Ejecutar una consulta
    cursor.execute("SELECT * FROM Tasks")

    # Obtener y mostrar los resultados
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    return{"message": "Hello World aqui tenemos la api FASTApi"}


@app.get("/get_tasks")
def get_tasks():

    connection = odbc.connect(connection_string)
    print("Conexión exitosa!")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Tasks")
    records = cursor.fetchall()

    print(records)

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    return records