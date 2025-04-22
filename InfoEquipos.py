#Se importan las funciones que utiliza internamente InfoEquipos
from QuienGana import QuienGana
from Puntos import Puntos
from Clasificacion import Clasificacion

#Funcion que recibe los datos de la liga y los equipos para generar informacion sobre los mismos
def InfoEquipos(datosliga,equipos):

    #Se genera un lista que contiene los equipos con los partidos ganados, perdidos y empatados
    lista = []
    for equipo in equipos:
        lista.append([equipo,0,0,0])

    #Recorre los datos de la liga y genera un array con los resultados
    for fila in datosliga:
        resultado = fila["FT"].split("-")

        #Mediante la funcion quien gana comprueba si ha ganado el visitante o el local
        if QuienGana(resultado) == -1:
            #Si gana el visitante aumenta partidos ganados del visitante y partidos perdidos a local
            for equipo in lista:
                if fila["Team 2"] in equipo:
                    equipo[1] += 1
                elif fila["Team 1"] in equipo:
                    equipo[3] += 1

        elif QuienGana(resultado) == 1:
            #Si gana el local aumenta partidos ganados del local y partidos perdidos a visitante
            for equipo in lista:
                if fila["Team 1"] in equipo:
                    equipo[1] += 1
                elif fila["Team 2"] in equipo:
                    equipo[3] += 1

        else:
            #Si es empate, aumenta el valor de partidos empatados a ambos equipos
            for equipo in lista:
                if fila["Team 2"] in equipo or fila["Team 1"] in equipo:
                    equipo[2] += 1

    #Recorre los equipos de la lista y le agrega el valor total de sus puntos
    for equipo in lista:
        equipo.append(Puntos(equipo))

    #Mediante la funcion Clasificacion ordena los equipos por puntos
    lista = Clasificacion(lista)
    return lista
