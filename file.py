from pymongo import MongoClient
import pymongo.errors

try:
    # Conectar a MongoDB
    MONGO_URI = MongoClient("mongodb://localhost", 27017)
    MONGO_URI.server_info()  # Verificar la conexión
    print("Conexión a MongoDB exitosa")

    # Listar bases de datos disponibles
    bases_de_datos = MONGO_URI.list_database_names()
    if bases_de_datos:
        print("Bases de datos disponibles:")
        for dbs in bases_de_datos:
            print(f"- {dbs}")
    else:
        print("No hay bases de datos disponibles.")
    
    db = MONGO_URI["TiendaRopa"]  # Crear o seleccionar la base de datos

    coleccion = db["productos"]  # Crear o seleccionar la colección
   
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido:", errorTiempo)

except pymongo.errors.ConnectionFailure as errorConexion:
    print("Falló la conexión a MongoDB: ", errorConexion)
