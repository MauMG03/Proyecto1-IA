import heapq

class Estado:
    def __init__(self, x, y, agua, costo):
        self.x = x
        self.y = y
        self.agua = agua
        self.costo = costo

    def __lt__(self, otro):
        return self.costo < otro.costo

def bombero_inteligente_costo_uniforme(mundo):
    n = len(mundo)
    m = len(mundo[0])
    puntos_de_fuego = 2
    puntos_de_fuego_apagados = 0
    inicio = None
    objetivos = []

    # Encontrar la ubicación del bombero y los puntos de fuego
    for i in range(n):
        for j in range(m):
            if mundo[i][j] == 5:  # Punto de inicio
                inicio = Estado(i, j, 0, 0)
            elif mundo[i][j] == 2:  # Punto de fuego
                objetivos.append((i, j))

    def es_valido(x, y):
        return 0 <= x < n and 0 <= y < m and mundo[x][y] != 1

    frontera = []
    heapq.heappush(frontera, inicio)
    visitados = set()

    while frontera:
        actual = heapq.heappop(frontera)

        if (actual.x, actual.y) in objetivos:
            puntos_de_fuego_apagados += 1
            objetivos.remove((actual.x, actual.y))

            if puntos_de_fuego_apagados == puntos_de_fuego:
                return actual.costo

        visitados.add((actual.x, actual.y))

        # Generar los vecinos posibles
        vecinos = [(actual.x - 1, actual.y), (actual.x + 1, actual.y), (actual.x, actual.y - 1), (actual.x, actual.y + 1)]

        for vecino_x, vecino_y in vecinos:
            if es_valido(vecino_x, vecino_y) and (vecino_x, vecino_y) not in visitados:
                nuevo_agua = actual.agua
                nuevo_costo = actual.costo

                if mundo[vecino_x][vecino_y] == 6:  # Hidrante
                    nuevo_agua = 2  # Llenar la cubeta de 2 litros
                elif mundo[vecino_x][vecino_y] == 3:  # Cubeta de 1 litro
                    nuevo_agua = 1  # Llenar la cubeta de 1 litro
                elif mundo[vecino_x][vecino_y] == 4:  # Cubeta de 2 litros
                    nuevo_agua = 0  # Llenar la cubeta de 2 litros
                elif mundo[vecino_x][vecino_y] == 2:  # Punto de fuego
                    if nuevo_agua > 0:
                        nuevo_agua -= 1  # Apagar el fuego
                    else:
                        continue  # No se puede pasar por el fuego sin agua

                nuevo_costo += 1 + nuevo_agua
                nuevo_estado = Estado(vecino_x, vecino_y, nuevo_agua, nuevo_costo)
                heapq.heappush(frontera, nuevo_estado)

    return float('inf')  # No se encontró una solución

# Ejemplo de uso con el nuevo formato
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

costo = bombero_inteligente_costo_uniforme(mundo)

if costo != float('inf'):
    print(f"Costo mínimo para apagar todos los puntos de fuego: {costo}")
    
else:
    print("No se encontró una solución")

