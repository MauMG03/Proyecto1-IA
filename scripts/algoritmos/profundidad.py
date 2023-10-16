import time
from .nodo import *
    
##Función profundidad
##Argumentos:
##    nodo: Instancia Nodo
##Retorna:
##    diccionario informacion que contiente: {
##      nodo: Objeto de clase Nodo
##      tiempo: Int que contiene el tiempo del algoritmo
##      nodos_expandidos: Int que contiene cantidad de nodos expandidos
##      recorrido: Array de arrays. Array de mapas que contienen el recorrido del bombero
##      }

def profundidad():
    #Se lee el mundo de "mundo.txt"
    with open("scripts/algoritmos/mundo.txt", "r") as file:
        #Leer el contenido del archivo
        content = file.read()

    #Se usa eval para parsear el contenido a una variable de python 
    mundo = eval(content)

    #Se busca y guarda la posición del bombero
    for y, fila in enumerate(mundo):
        for x, elemento in enumerate(fila):
            if elemento == 5:
                posicionBombero = [y, x]

