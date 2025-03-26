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

# Inicio de sesion
def login():
    datos = cargar_datos()
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in datos["usuarios"] and datos["usuarios"][usuario]["contraseña"] == contraseña:
        print(f"✅ Bienvenido, {usuario} ({datos['usuarios'][usuario]['rol']})")
        return usuario, datos["usuarios"][usuario]["rol"]
    else:
        print("❌ Usuario o contraseña incorrectos.")
        return None, None

#Menu admin
def menu_administrador():
    datos = cargar_datos()
    while True:
        print("\n--- MENÚ ADMINISTRADOR ---")
        print("1. Crear curso")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_curso = input("Ingrese el nombre del curso: ")
            if nombre_curso in datos["cursos"]:
                print("❌ El curso ya existe.")
            else:
                datos["cursos"][nombre_curso] = {}
                guardar_datos(datos)
                print(f"✅ Curso '{nombre_curso}' creado con éxito.")
        elif opcion == "2":
            break
        else:
            print("❌ Opción inválida.")

