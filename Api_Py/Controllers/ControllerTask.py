from fastapi import HTTPException
from Conn import get_db_connection
from Models.Task import TaskCreate
import pypyodbc


def Root(): #Funcion la cual se ejecuta cuando cargmamos nuestra URL principal (Solo para pruebas)

    connection = get_db_connection() #Mandamos a llamar funcion para crear conexion
    cursor = connection.cursor() # Crear un cursor

    cursor.execute("SELECT * FROM Tasks") # Ejecutar una consulta en base de datos SQL 
    
    rows = cursor.fetchall() # Obtener y mostrar los resultados

    cursor.close() # Cerrar el cursor y la conexión
    connection.close()

    print("Function from my controller")

    return rows


def get_tasks(): #Funcion para obtener todos los datos de las tabla Tasks

    connection = get_db_connection() #Mandamos a llamar funcion para crear conexion

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Tasks with(nolock)")
    records = cursor.fetchall()

    cursor.close() # Cerrar el cursor y la conexión
    connection.close()

    print("function get tasks from my controller")

    return records


def add_Task(task: TaskCreate): #Funcion para agregar tasks en nuestra base de datos desde nuestro modelo con un SP creado desde la base de datos 
    
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

        print("Function add tasks from my controller with SP created in DB")


def delete_Task(task_id = int):
    
    connection = get_db_connection()
    cursor = connection.cursor()

    try:

        query = "EXEC DeleteTask @Id = ?;"
        values = (task_id,)

        cursor.execute(query, values)

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task no encontrada")
        
        connection.commit()

        return {"message": f"Task con Id {task_id} eliminada exitosamente"}

    except pypyodbc.Error as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error al insertar la tarea: {e}")
    
    finally:
        cursor.close()
        connection.close()

        print("Function delete tasks from my controller with SP created in DB si aqui")

