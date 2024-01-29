## Leer el contenido de una carpeta diferenciando entre ficheros y directorios.

import os


def listar_contenido_carpeta():

    ruta_carpeta = input("Ingrese la ruta de la carpeta:  ")

    try:
        # Obtener la lista de elementos en la ruta especificada
        contenido = os.scandir(ruta_carpeta)

        # Iterar sobre el contenido y diferenciar entre archivos y directorios
        for elemento in contenido:
            if elemento.is_file():
                print(f"Archivo: {elemento.name}")
            elif elemento.is_dir():
                print(f"Directorio: {elemento.name}")

    except NotADirectoryError:
        print(f"La ruta  '{ruta_carpeta}' no es una carpeta.")

# Llamada a la función para listar el contenido
listar_contenido_carpeta()