import hashlib
import json


def guardar_datos_usuarios(datos_usuarios):
    with open('usuarios.json', 'w') as archivo:
        json.dump(datos_usuarios, archivo)


def cargar_datos_usuarios():
    try:
        with open('usuarios.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}


def registrar_usuario():
    nombre_usuario = input("Introduce un nombre de usuario: ")

    # Verificar si el usuario ya existe
    if nombre_usuario in datos_usuarios:
        print("El usuario ya existe. Por favor, introduce otro nombre de usuario.")
        return

    # Pedir y encriptar la contraseña
    contraseña = input("introduce una contraseña: ")
    confirmar_contraseña = input("Confirma la contraseña: ")

    if contraseña != confirmar_contraseña:
        print("Las contraseñas no coinciden. Intenta de nuevo.")
        return

    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()

    # Guardar el nuevo usuario y su contraseña encriptada
    datos_usuarios[nombre_usuario] = hash_contraseña
    guardar_datos_usuarios(datos_usuarios)
    print("Te has registrado.")


def iniciar_sesion():
    nombre_usuario = input("Introduce tú nombre de usuario: ")

    # Verificar si el usuario existe
    if nombre_usuario not in datos_usuarios:
        print("El usuario no existe. ¿Desea registrarse?")
        respuesta = input("marca 'si' o 'no': ").lower()

        if respuesta == 'si':
            registrar_usuario()
        else:
            print("No se puede iniciar sesión.")
        return

    # Verificar la contraseña
    contraseña = input("Introduce tú contraseña: ")
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()

    if datos_usuarios[nombre_usuario] == hash_contraseña:
        print("Has iniciado sesión.")
    else:
        print("Contraseña erronea.")


# Cargar datos de usuarios existentes
datos_usuarios = cargar_datos_usuarios()

# Menú principal
while True:
    print("\nBienvenido al registro y login.")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == '1':
        iniciar_sesion()
    elif opcion == '2':
        registrar_usuario()
    elif opcion == '3':
        print("Gracias por pasarte por aqui. ¡Hasta luego MariCarmen!")
        break
    else:
        print("Opción no válida. Por favor, no me sea cenutrio e introduce  1, 2 o 3.")