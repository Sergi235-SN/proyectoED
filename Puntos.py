#Funcion que recibe los datos de partidos y devuelve los puntos
def Puntos(info):
    
    ganados = info[1]
    empatados = info[2]

    puntosTotales = (ganados * 3) + (empatados)

    return puntosTotales
