ruta = input("introduce la ruta del archivo: ")

try:
    archivo = open(ruta)
    print(archivo.read())
except FileNotFoundError:
    print("el archovo no existe: ")