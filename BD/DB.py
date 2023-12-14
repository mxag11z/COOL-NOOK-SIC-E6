import json
import firebase_admin
from firebase_admin import credentials, db

# Inicializar la conexión a Firebase
cred = credentials.Certificate('cool-nook.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://COOL-NOOK.firebaseio.com'
})

ref = db.reference('/datos')  # Reemplaza '/datos' con la ruta de tu base de datos

# Operación para agregar un nuevo registro
def agregar_registro(caducidad, id_producto, ingreso, nombre, tipo):
    nuevo_registro = ref.push()
    nuevo_registro.set({
        'caducidad': caducidad,
        'id_producto': id_producto,
        'ingreso': ingreso,
        'nombre': nombre,
        'tipo': tipo
    })
    print("Registro agregado correctamente.")

# Operación para obtener todos los registros
def obtener_registros():
    registros = ref.get()
    if registros:
        for uid, registro in registros.items():
            print(f"ID: {uid}, Caducidad: {registro['caducidad']}, ID Producto: {registro['id_producto']}, Ingreso: {registro['ingreso']}, Nombre: {registro['nombre']}, Tipo: {registro['tipo']}")
    else:
        print("No hay registros en la base de datos.")

# Operación para actualizar un registro por su ID
def actualizar_registro(uid, caducidad, id_producto, ingreso, nombre, tipo):
    registro = ref.child(uid)
    if registro.get():
        registro.update({
            'caducidad': caducidad,
            'id_producto': id_producto,
            'ingreso': ingreso,
            'nombre': nombre,
            'tipo': tipo
        })
        print("Registro actualizado correctamente.")
    else:
        print("Registro no encontrado.")

# Operación para eliminar un registro por su ID
def eliminar_registro(uid):
    registro = ref.child(uid)
    if registro.get():
        registro.delete()
        print("Registro eliminado correctamente.")
    else:
        print("Registro no encontrado.")


def agregar_registros_desde_json():
    try:
        with open('datos.json', 'r') as file:
            registros = json.load(file)
            for registro in registros:
                agregar_registro(
                    registro['caducidad'],
                    registro['id_producto'],
                    registro['ingreso'],
                    registro['nombre'],
                    registro['tipo']
                )
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error al agregar registros: {e}")

if __name__ == "__main__":
    agregar_registros_desde_json()