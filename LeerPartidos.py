import csv

#Funcion que lee el contenido de la liga como una lista de diccionarios
def LeerPartidos():
    try:
        with open("liga.csv",encoding="UTF-8") as file:

            #Lee el fichero como una lista de diccionarios
            reader = csv.DictReader(file,delimiter=",")

            #Introduce el contenido del fichero en una lista y la devuelve
            contenido = list(reader)
            return contenido

    except FileNotFoundError:
        print("No se ha encontrado el archivo...")
