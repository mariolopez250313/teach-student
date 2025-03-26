# librerias utilizadas
import pickle
import os

#carga y guardado de datos
DATA_FILE = "datos.pkl"

def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            return pickle.load(f)
    return {"usuarios": {}, "cursos": {}}

def guardar_datos(datos):
    with open(DATA_FILE, "wb") as f:
        pickle.dump(datos, f)

