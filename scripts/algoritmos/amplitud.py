import time
from .nodo import *
    
##Función amplitud
##Argumentos:
##    nodo: Instancia Nodo
##Retorna:
##    diccionario informacion que contiente: {
##      nodo: Objeto de clase Nodo
##      tiempo: Int que contiene el tiempo del algoritmo
##      nodos_expandidos: Int que contiene cantidad de nodos expandidos
##      recorrido: Array de arrays. Array de mapas que contienen el recorrido del bombero
##      }
def amplitud():

    #Se lee el mundo de "mundo.txt"
    with open("scripts/algoritmos/mundo.txt", "r") as file:
        #Leer el contenido del archivo
        content = file.read()

    #Se usa eval para parsear el contenido a una variable de python 
    mundo = eval(content)

    #Definimos la cola
    queue = []

    #Definimos la variable que almacenará la cantidad de nodos expandidos
    nodos_expandidos = 1

    #Se busca y guarda la posición del bombero
    for y, fila in enumerate(mundo):
        for x, elemento in enumerate(fila):
            if elemento == 5:
                posicionBombero = [y, x]

    #Creamos estado y nodos raíces
    estado_raiz = Estado(mundo, posicionBombero, 0, 0)
    nodo_raiz = Nodo(estado_raiz, None, None, 0, 0)

    #Añadimos nodo_raiz a la cola
    queue.append(nodo_raiz)

    #Empezamos a tomar el tiempo inicial
    start = time.time()
    while True:
        #Significa que falló
        if len(queue) == 0:
            return False
        #Extraemos el nodo que se encuentra en cabeza
        nodo = queue.pop(0)
        #Evaluamos si es meta
        if nodo.esMeta():
            #Guardamos el timepo que tomó el algoritmo
            end = time.time()
            tiempo_final = end-start

            #Guardar el recorrido hecho
            recorrido = []
            nodoFinal = nodo
            while (nodo is not None):
                #Debido a la estructura del código, si el bombero se encuentra en una
                #Cubeta o hidrante, este no se encuentra en el mapa.
                #Para mostrar el recorrido, se modifica el mapa a guardar en 'recorrido'
                mapa = nodo.estado.mapa
                estaBombero = False
                for fila in mapa:
                    if (5 in fila):
                        estaBombero = True
                
                #Si no se encuentra el bombero
                if not estaBombero:
                    #Tomar la posicion del bombero del estado del nodo
                    posicionBombero = nodo.estado.posicion
                    #Asignarla en el mapa
                    mapa[posicionBombero[0]][posicionBombero[1]] = 5

                recorrido.append(mapa)
                nodo = nodo.padre

            #Debido a que el recorrido se guardó al reves, aquí se voltea por así decirlo
            recorrido = recorrido[::-1]
            
            informacion = {
                "nodo": nodoFinal,
                "tiempo": tiempo_final,
                "nodos_expandidos": nodos_expandidos,
                "recorrido": recorrido
            }

            return informacion

        #Se expande el nodo raíz
        direcciones = nodo.posiblesMovimientos()
        for direccion in direcciones:
            nodos_expandidos += 1
            estado = nodo.mover(direccion)

            #Se calcula el costo del movimiento
            #Definición de costo
            costo_movimiento = 1
            #Sumar la cantidad de agua que lleva
            costo_movimiento += nodo.estado.agua
            #Se calcula el nuevo costo
            costo = costo_movimiento + nodo.costo

            #Se calcula la nueva profundidad
            profundidad = nodo.profundidad + 1

            nuevo_nodo = Nodo(estado, nodo, direccion, profundidad, costo)
            queue.append(nuevo_nodo)

        


        
    
    
    

    

    