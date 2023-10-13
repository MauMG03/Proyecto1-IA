from nodo import *
import time, copy
    

##Función amplitud
##Argumentos:
##    nodo: Instancia Nodo
##Retorna:
##    ?
def amplitud():

    # Definimos el mundo
    #(Mundo de prueba para comprobar que funciona bien)
    # mundo = [
    # [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    # [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    # [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    # [2, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    # [5, 3, 6, 1, 0, 0, 0, 1, 0, 1],
    # [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    # [2, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    # [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    # [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    # [0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
    # ]
    #(Mundo del proyecto)
    mundo = [
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 2, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [5, 0, 0, 6, 4, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [3, 0, 0, 0, 2, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
    ]

    #Definimos la cola
    queue = []

    #Definimos la variable que almacenará la cantidad de nodos expandidos
    nodos_expandidos = 1

    #Creamos estado y nodos raíces
    estado_raiz = Estado(mundo, [4, 0], 0, 0)
    nodo_raiz = Nodo(estado_raiz, None, None, 0, 0)

    #Añadimos nodo_raiz a la cola
    queue.append(nodo_raiz)

    #Empezamos a tomar el tiempo inicial
    start = time.time()
    while True:
        #time.sleep(0.5)
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

            #print("Profundidad del nodo: " + str(nodo.profundidad))
            #print("Costo del nodo: " + str(nodo.costo))
            #print("El algoritmo de Amplitud ha terminado :D")
            #print(f"El tiempo total en el código es: {end-start}")

            # Esto es para ver la ruta del padre por consola
            # print("Aquí esta la ruta completa:")
            # while (nodo is not None):
            #     print("Costo: " + str(nodo.costo))
            #     print(nodo.estado.mapa)
            #     nodo = nodo.padre

            #Guardar el recorrido hecho
            recorrido = []
            nodoFinal = copy.deepcopy(nodo)
            while (nodo is not None):
                #Debido a la estructura del código, si el bombero se encuentra en una
                #Cubeta o hidrante, este no se encuentra en el mapa.
                #Para mostrar el recorrido, modificaremos el mapa a guardar en 'recorrido'
                mapa = copy.deepcopy(nodo.estado.mapa)
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
                "nodo": copy.deepcopy(nodoFinal),
                "tiempo": tiempo_final,
                "nodos_expandidos": nodos_expandidos
            }

            informacion = [informacion, recorrido]
            return informacion

        #Expandimos nodo_raíz
        direcciones = nodo.posiblesMovimientos()
        for direccion in direcciones:
            nodos_expandidos += 1
            parametros = nodo.mover(direccion)
            nuevo_nodo = Nodo(parametros[0], nodo, parametros[1], parametros[2], parametros[3])
            queue.append(nuevo_nodo)

        


        
    
    
    

    

    