#Importa las funciones LeerPartidos e impClasificacion
from LeerPartidos import LeerPartidos
from impClasificacion import impClasificacion

#Obtine los datos del fichero
liga = LeerPartidos()
#Mediante los metodos internos de la funcion impClasificacion
#Obtiene y muestra la clasificacion de la liga
impClasificacion(liga)
