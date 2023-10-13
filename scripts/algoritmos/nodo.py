import copy

##Clase Estado
##Argumentos:
##    mapa: Array de arrays que indican el mapa del bombero
##    posicion: Array de dos elementos: [y, x]
##    cubeta: Int que indica el tamaño de la cubeta del bombero
##      0 = No tiene cubeta aún
##      1 = Cubeta de 1 L
##      2 = Cubeta de 2 L
##    agua: Int que indica cuantos L lleva el bombero
class Estado:
    def __init__(self, mapa, posicion, cubeta, agua):
        self.mapa = mapa
        self.posicion = posicion
        self.cubeta = cubeta
        self.agua = agua

##Clase Nodo
##Argumentos:
##    estado: Instancia de Estado del mapa
##    nodo_padre: Instancia de Nodo predecesor al nodo instanciado
##    operador: Operador aplicado al nodo
##    profundidad: La profundida en la que se encuentra el nodo
##    costo_ruta: El costo que lleva hasta el momento el nodo

class Nodo:
    def __init__(self, estado, padre, operador, profundidad, costo):
        self.estado = estado
        self.padre = padre
        self.operador = operador
        self.profundidad = profundidad
        self.costo = costo
    
    ##Función posiblesMovimientos
    ##Argumentos:
    ##    self: Instancia Nodo
    ##Retorna:
    ##    movimientos: Array de posibles movimientos
    ##      0 = arriba
    ##      1 = derecha
    ##      2 = abajo
    ##      3 = izquierda
    def posiblesMovimientos(self):

        ##Función direccionContrario
        ##Arroja la dirección contrario de un operador
        def direccionContraria(direccion1, direccion2):
            if ((direccion1 == 0 and direccion2 == 2) or (direccion1 == 2 and direccion2 == 0)):
                return True
            elif ((direccion1 == 1 and direccion2 == 3) or (direccion1 == 3 and direccion2 == 1)):
                return True
            
            return False
            
        ##Función cambióEstado
        ##Arroja si los estados de los dos nodos son diferentes o no
        def cambioEstado(estado1, estado2):
            #Si el bombero obtuvo una cubeta o si la cantidad de agua cambió
            if ((estado1.cubeta != estado2.cubeta) or (estado1.agua != estado2.agua)):
                return True
            
            return False

        #Guardamos posicion en x
        y = copy.deepcopy(self.estado.posicion[0])
        #Guardamos posicion en y
        x = copy.deepcopy(self.estado.posicion[1])

        #Guardar en un array lo que se encuentra alrededor del bombero
        mapa_alrededor = []

        #0 = Arriba, 1 = Derecha, 2 = Abajo, 3 = Izquierda
        #Si se trata de una frontera, se trabajará como si fuera una pared
        if (y > 0):
            mapa_alrededor.append(self.estado.mapa[y-1][x])
        else:
            mapa_alrededor.append(1)

        if (x < 9):
            mapa_alrededor.append(self.estado.mapa[y][x+1])
        else:
            mapa_alrededor.append(1)

        if (y < 9):
            mapa_alrededor.append(self.estado.mapa[y+1][x])
        else:
            mapa_alrededor.append(1)

        if (x > 0):
            mapa_alrededor.append(self.estado.mapa[y][x-1])
        else:
            mapa_alrededor.append(1)

        # try:
        #     mapa_alrededor.append(self.estado.mapa[y-1][x])
        # except:
        #     mapa_alrededor.append(1)
        # try:
        #     mapa_alrededor.append(self.estado.mapa[y][x+1])
        # except:
        #     mapa_alrededor.append(1)
        # try:
        #     mapa_alrededor.append(self.estado.mapa[y+1][x])
        # except:
        #     mapa_alrededor.append(1)
        # try:
        #     mapa_alrededor.append(self.estado.mapa[y][x-1])
        # except:
        #     mapa_alrededor.append(1)
        
        direccion = 0
        movimientos = []
        for posicion in mapa_alrededor:
            # Si la posicion es una pared o si es un fuego y no tiene agua 
            if (posicion != 1 and not (posicion == 2 and self.estado.agua == 0)):
                #Si el operador es para devolverse. 
                if (direccionContraria(self.operador, direccion)):
                    #Si el estado cambió, añada la dirección, sino, no
                    if (cambioEstado(self.padre.estado, self.estado)):
                        movimientos.append(direccion)
                #Ya que no se está devolviendo, añada la dirección por defecto
                else:
                    movimientos.append(direccion)
            
            #Seguir con la siguiente dirección
            direccion += 1
        
        return movimientos
            
    ##Función mover
    ##Argumentos:
    ##    self: Instancia Nodo
    ##    direccion: Dirección en la que se moverá el bombero
    ##      0 = arriba
    ##      1 = derecha
    ##      2 = abajo
    ##      3 = izquierda
    ##Retorna:
    ##    Array con: [nuevo_estado, operador, profunidad, costo]
    def mover(self, direccion):
        # Definicion de costos
        costo_movimiento = 1
        # Sumar la cantidad de agua que lleva
        costo_movimiento += copy.deepcopy(self.estado.agua)
        #Hago una copia del estado
        nuevo_estado = copy.deepcopy(self.estado)

        #Guardamos posicion en x
        y = copy.deepcopy(self.estado.posicion[0])
        #Guardamos posicion en y
        x = copy.deepcopy(self.estado.posicion[1])

        if (direccion == 0): # 0 es arriba
            #Asignar vacio donde estaba el bombero (A excepción de 3, 4, 6 que son cubetas e hidrante)
            if (self.estado.mapa[y][x] not in (3, 4, 6)):
                nuevo_estado.mapa[y][x] = 0
            #Guardo que hay en el lugar a desplazar
            objeto = self.estado.mapa[y-1][x]
            #Asignar bombero al nuevo espacio (A excepción de 3, 4, 6 que son cubetas e hidrante)
            if (self.estado.mapa[y-1][x] not in (3, 4, 6)):
                nuevo_estado.mapa[y-1][x] = 5
            #Se asigna nueva posicion al bombero
            nuevo_estado.posicion = [y-1, x]

        elif (direccion == 1): #1 es derecha
            if (self.estado.mapa[y][x] not in (3, 4, 6)):
                nuevo_estado.mapa[y][x] = 0
            objeto = self.estado.mapa[y][x+1]
            if (self.estado.mapa[y][x+1] not in (3, 4, 6)):
                nuevo_estado.mapa[y][x+1] = 5
            nuevo_estado.posicion = [y, x+1]

        elif (direccion == 2): #2 si es abajo
            if (self.estado.mapa[y][x] not in (3, 4, 6)):
                nuevo_estado.mapa[y][x] = 0
            objeto = self.estado.mapa[y+1][x]
            if (self.estado.mapa[y+1][x] not in (3, 4, 6)):
                nuevo_estado.mapa[y+1][x] = 5
            nuevo_estado.posicion = [y+1, x]

        elif (direccion == 3): #3 si es izquierda
            if (self.estado.mapa[y][x] not in (3, 4, 6)):
                nuevo_estado.mapa[y][x] = 0
            objeto = self.estado.mapa[y][x-1]
            if (self.estado.mapa[y][x-1] not in (3, 4, 6)):
                nuevo_estado.mapa[y][x-1] = 5
            nuevo_estado.posicion = [y, x-1]

        #Cambios necesarios respecto a la nueva posición del bombero
        if (objeto == 2): #Si pasó por un punto de fuego, restar agua
            nuevo_estado.agua -= 1
        elif (objeto == 3): #Si pasó por una cubeta de 1L
            if (self.estado.cubeta == 0): #Si no tiene una cubeta
                nuevo_estado.cubeta = 1
        elif (objeto == 4): #Si pasó por una cubeta de 2L
            if (self.estado.cubeta == 0): #Si no tiene una cubeta
                nuevo_estado.cubeta = 2
        elif (objeto == 6 and self.estado.cubeta > 0 and self.estado.agua == 0): #Si pasó por un hidrante, tiene cubeta, y no tiene agua
            nuevo_estado.agua = self.estado.cubeta

        #Sumar profundidad y costo
        profundidad = self.profundidad + 1
        costo = self.costo + costo_movimiento
        operador = direccion

        return [nuevo_estado, operador, profundidad, costo]

    ##Función esMeta
    ##Argumentos:
    ##    self: Instancia Nodo
    ##Retorna:
    ##    boolean: Si ya se han apagado los puntos de fuego
    def esMeta(self):
        for fila in self.estado.mapa:
            if 2 in fila:
                return False
        
        return True