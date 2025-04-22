def Equipos(datosliga):
    # crea una lista que guardará el nombre de los equipos
    equipos = []

    # revisa los nombre de uno en uno
    for partido in datosliga:
        # si el equipo local no está en la lista lo añade a ella
        if partido['Team 1'] not in equipos:
            equipos.append(partido['Team 1'])
        # lo mismo con el equipo visitante
        if partido['Team 2'] not in equipos:
            equipos.append(partido['Team 2'])

    # devuelve la lista de nombres
    return equipos
