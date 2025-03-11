from fastapi import FastAPI, HTTPException
from Conn import get_db_connection
from Models.Task import TaskCreate
from Controllers.ControllerTask import Root
import pypyodbc

app=FastAPI()


@app.get("/")  #Realiza conexion a base de datos y trae todos sus registros
def root():

    #connection = get_db_connection() #Mandamos a llamar funcion para crear conexion

    # Crear un cursor
    #cursor = connection.cursor()

    # Ejecutar una consulta en base de datos SQL 
    #cursor.execute("SELECT * FROM Tasks")

    # Obtener y mostrar los resultados
    #rows = cursor.fetchall()
    #for row in rows:
        #print(row)

    # Cerrar el cursor y la conexión
    #cursor.close()
    #connection.close()

    Result = Root();

    print(Result)

    return Result


@app.get("/get_tasks") #Funcion para obtener todos los registros de la tabla Tasks
def get_tasks():

    connection = get_db_connection() #Mandamos a llamar funcion para crear conexion

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Tasks")
    records = cursor.fetchall()

    print(records)

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    return records #Regresamos todos los valores que obtenemos de la base de datos


@app.post("/tasks/", response_model=TaskCreate)
def create_task(task: TaskCreate):

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        query = "EXEC InsertTask @Title=?, @Description=?, @Status=?, @CreationDate=?, @DueDate=?"
        values = (task.title, task.description, task.status, task.creationDate, task.dueDate)
        cursor.execute(query, values)
        connection.commit()
        return task
    
    except pypyodbc.Error as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error al insertar la tarea: {e}")
    
    finally:
        cursor.close()
        connection.close()


#Proximos paso es cambiar toda la arquitectura para usar algo parecido como modelo vista controlador para separar la logica que tendremos a las llamadas 
#a la api y las conexiones a las bases de datos .