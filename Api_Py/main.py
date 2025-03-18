from fastapi import FastAPI, HTTPException
from Conn import get_db_connection
from Models.Task import TaskCreate
import Controllers.ControllerTask as ControllerTask
import pypyodbc


app=FastAPI()


@app.get("/")  #Realiza conexion a base de datos y trae todos sus registros
def root():

    Result = ControllerTask.Root();
    print(Result)

    return "Root succesfully"


@app.get("/get_tasks") #Funcion para obtener todos los registros de la tabla Tasks
def get_tasks():

    records = ControllerTask.get_tasks();
    print(records)

    return "get_tasks" 


@app.post("/add_task/", response_model=TaskCreate)
def create_task(task: TaskCreate):

    Result = ControllerTask.add_Task(task)

    return "Added succesfully"

@app.delete("/deleted_task/{task_id}")
def create_task(task_id = int):

    message = ControllerTask.delete_Task(task_id)

    return message


#Proximos paso es cambiar toda la arquitectura para usar algo parecido como modelo vista controlador para separar la logica que tendremos a las llamadas 
#a la api y las conexiones a las bases de datos . (COMPLETADO)

#Agregar funcion de delet y de update front(En progreso) 

#def delete_task(task_id: int):
    #connection = get_db_connection()
    #cursor = connection.cursor()

    #try:
        # Llamar al Stored Procedure
        #query = "EXEC DeleteTask @Id=?"
        #values = (task_id,)
        
        #cursor.execute(query, values)
        # Verificar si se eliminó algo
        #if cursor.rowcount == 0:
            #raise HTTPException(status_code=404, detail="Task no encontrada")
        #connection.commit()
        #return {"message": f"Task con Id {task_id} eliminada exitosamente"}

    #except pypyodbc.Error as e:
        #connection.rollback()
        #raise HTTPException(status_code=500, detail=f"Error al eliminar la tarea: {e}")
    #finally:
        #cursor.close()
        #connection.close()

#Hacer la comunicacion con la app Agular desde front