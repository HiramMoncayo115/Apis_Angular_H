import pypyodbc as odbc 

def get_db_connection():

    connection_string = (
    "DRIVER={SQL Server};"           #{ODBC Driver 17 for SQL Server}
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=Py_&_net_&_Angular;"
    "UID=User_apps;"
    "PWD=1234;"
    )

    try:
        connection = odbc.connect(connection_string)
        print("Conexión exitosa!")
        return connection
    except odbc.Error as e:
        raise Exception(f"Error al conectar a la base de datos: {e}")
    


