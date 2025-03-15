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

@app.post("/deleted_task/{task_id}", response_model=TaskCreate)
def create_task(task_id = int:

    Result = ControllerTask.add_Task(task)

    return "Added succesfully"


#Proximos paso es cambiar toda la arquitectura para usar algo parecido como modelo vista controlador para separar la logica que tendremos a las llamadas 
#a la api y las conexiones a las bases de datos . (COMPLETADO)

#Agregar funcion de delet y de update front(En progreso)

#Hacer la comunicacion con la app Agular desde front