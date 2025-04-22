from InfoEquipos import InfoEquipos
from Equipos import Equipos

def impClasificacion(liga):

    equipos = Equipos(liga)

    info = InfoEquipos(liga,equipos)

    print("Clasif.Equipo Ganados Empatados Perdidos Puntos")
    for i,equipo in enumerate(info):
        if equipo[0] == "Celta":
            print(f"{i+1}.{equipo[0]}\t\t{equipo[1]}\t {equipo[2]}\t   {equipo[3]}\t   {equipo[4]}")
        else:
            print(f"{i+1}.{equipo[0]}\t{equipo[1]}\t {equipo[2]}\t   {equipo[3]}\t   {equipo[4]}")
