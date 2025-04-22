#Función QuienGana que comprueba el ganador del partido
def QuienGana(resultado):

    #Comprueba el resultado y devuelve 0 si es empate, 1 si gana el local y -1 si gana el visitante
    if resultado[0] == resultado[1]:
        return 0
    elif resultado[0] > resultado[1]:
        return 1
    else:
        return -1
