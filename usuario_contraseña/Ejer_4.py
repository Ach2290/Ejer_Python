## Modificar el contenido de un fichero.

elige = input("añade texto (a) o sobreescribe texto(w)")
if elige == "a":

    file = open("new.txt", "a")
    file.write(input("escribe en el archivo"))

else:

    file = open("new.txt","w")
    file.write(input("escribe en el archivo"))