# Función que ordena los equipos por sus puntos
def Clasificacion(datos):

    # Ordena los datos en el orden de puntos (posición 4 de los datos)
    return sorted(datos, key=lambda x: (-x[4], x[0]))
