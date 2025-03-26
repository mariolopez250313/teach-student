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

#registro de usuarios
def registrar_usuario():
    datos = cargar_datos()
    usuario = input("Ingrese un nombre de usuario: ")
    if usuario in datos["usuarios"]:
        print("❌ El usuario ya existe.")
        return
    contraseña = input("Ingrese una contraseña: ")
    rol = input("Ingrese el rol (administrador, profesor, estudiante): ").lower()
    
    if rol not in ["administrador", "profesor", "estudiante"]:
        print("❌ Rol inválido.")
        return
    
    datos["usuarios"][usuario] = {"contraseña": contraseña, "rol": rol, "cursos": {}}
    guardar_datos(datos)
    print(f"✅ {rol.capitalize()} registrado con éxito.")

