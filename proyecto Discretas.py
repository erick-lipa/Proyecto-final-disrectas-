import sys

INF = 10**9

class NODO:
    def __init__(self, id, ciudad):
        self.id = id
        self.ciudad = ciudad


class ARISTA:
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso


class ListaDeAdyacencia:
    def __init__(self, cantidadNodos):
        self.V = cantidadNodos
        self.A = 0
        self.adj = [[] for _ in range(cantidadNodos)]
        self.nodos = [None] * cantidadNodos

        # MATRICES PARA FLOYD WARSHALL
        self.dist = [[INF]*cantidadNodos for _ in range(cantidadNodos)]
        self.pred = [[None]*cantidadNodos for _ in range(cantidadNodos)]

        for i in range(cantidadNodos):
            self.dist[i][i] = 0

    def agregarNodo(self, id, ciudad):
        self.nodos[id] = NODO(id, ciudad)

    def agregarArista(self, origen, destino, peso):
        u, v = origen.id, destino.id

        # Lista de adyacencia
        self.adj[u].append(ARISTA(origen, destino, peso))
        self.adj[v].append(ARISTA(destino, origen, peso))

        # MATRICES PARA FLOYD WARSHALL
        self.dist[u][v] = peso
        self.dist[v][u] = peso

        self.pred[u][v] = u
        self.pred[v][u] = v

        self.A += 1

    def floydWarshall(self):
        print("\nCalculando rutas óptimas entre TODAS las ciudades...\n")
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):

                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]

                
                        self.pred[i][j] = self.pred[k][j]

    def obtenerRuta(self, origen, destino):
        if self.pred[origen][destino] is None:
            return []

        ruta = []
        actual = destino

        while actual is not None:
            ruta.append(actual)
            if actual == origen:
                break
            actual = self.pred[origen][actual]

        ruta.reverse()
        return ruta

    def mostrarResultadosRuta(self, origenId, destinoId):
        distancia = self.dist[origenId][destinoId]

        if distancia >= INF:
            print("\nNo existe ruta entre estas ciudades.\n")
            return

        print(f"\n📏 Distancia mínima: {distancia} km\n")

        ruta = self.obtenerRuta(origenId, destinoId)
        print("🧭 Ruta óptima:")
        for r in ruta:
            print(self.nodos[r].ciudad, end=" → ")
        print("FIN\n")

        self.calcularCostoCombustible(distancia)
        self.calcularTiempoRecorrido(distancia)

    def calcularTiempoRecorrido(self, km):
        lluvia = input("¿Está lloviendo? (si/no): ").lower()
        velocidad = 30 if lluvia == "si" else 90
        minutos = (km / velocidad) * 60
        print(f"⏱ Tiempo estimado: {minutos:.2f} minutos\n")

    def calcularCostoCombustible(self, km):
        PRECIO = 15753
        REND = 50
        galones = km / REND
        costo = galones * PRECIO
        print(f"⛽ Galones necesarios: {galones:.2f}")
        print(f"💰 Costo total: ${costo:.2f}\n")

    def mostrarNodos(self):
        print("\nLista de ciudades (nodos):")
        for i in range(self.V):
            print(f"{i}: {self.nodos[i].ciudad}")
        print()


def main():
        grafo = ListaDeAdyacencia(45)

        # CREACIÓN DE NODOS
        ciudades = [
            "Bucaramanga","San Gil","Barrancabermeja","Pamplona","Toledo",
            "La Fortuna","Barbosa","Puerto Araujo","Tunja","Medellín",
            "Quibdó","Pereira","Caucasia","Necoclí","Armenia","Manizales",
            "Mariquita","Ibagué","Bogotá","Neiva","Cali","Villavicencio",
            "San José del Guaviare","Yopal","Orocué","Duitama","Cúcuta",
            "Aguachica","El Banco Magdalena","Sincelejo","Montería","Cartagena",
            "Barranquilla","Santa Marta","Riohacha","Valledupar","Bosconia",
            "Popayán","Buenaventura","Pasto","Mocoa","Florencia",
            "San Vicente del Caguán","Saravena","Tumaco"
        ]

        for i, ciudad in enumerate(ciudades):
            grafo.agregarNodo(i, ciudad)

        n = grafo.nodos

        grafo.agregarArista(n[0], n[1], 99)
        grafo.agregarArista(n[0], n[2], 122)
        grafo.agregarArista(n[0], n[3], 123)
        grafo.agregarArista(n[0], n[4], 166)
        grafo.agregarArista(n[0], n[5], 88)
        grafo.agregarArista(n[1], n[6], 117)
        grafo.agregarArista(n[6], n[7], 136)
        grafo.agregarArista(n[6], n[8], 73)
        grafo.agregarArista(n[2], n[7], 91)
        grafo.agregarArista(n[7], n[9], 218)
        grafo.agregarArista(n[9], n[10], 253)
        grafo.agregarArista(n[9], n[11], 211)
        grafo.agregarArista(n[9], n[12], 282)
        grafo.agregarArista(n[9], n[13], 371)
        grafo.agregarArista(n[10], n[11], 253)
        grafo.agregarArista(n[11], n[14], 50)
        grafo.agregarArista(n[11], n[15], 51)
        grafo.agregarArista(n[15], n[16], 112)
        grafo.agregarArista(n[16], n[17], 134)
        grafo.agregarArista(n[17], n[14], 82)
        grafo.agregarArista(n[17], n[18], 197)
        grafo.agregarArista(n[17], n[19], 211)
        grafo.agregarArista(n[14], n[20], 175)
        grafo.agregarArista(n[18], n[8], 151)
        grafo.agregarArista(n[21], n[18], 114)
        grafo.agregarArista(n[21], n[22], 282)
        grafo.agregarArista(n[21], n[23], 261)
        grafo.agregarArista(n[23], n[25], 168)
        grafo.agregarArista(n[23], n[24], 131)
        grafo.agregarArista(n[25], n[8], 64)
        grafo.agregarArista(n[3], n[26], 74)
        grafo.agregarArista(n[26], n[27], 300)
        grafo.agregarArista(n[27], n[5], 153)
        grafo.agregarArista(n[27], n[28], 112)
        grafo.agregarArista(n[28], n[29], 339)
        grafo.agregarArista(n[29], n[30], 112)
        grafo.agregarArista(n[29], n[31], 185)
        grafo.agregarArista(n[30], n[12], 120)
        grafo.agregarArista(n[30], n[13], 149)
        grafo.agregarArista(n[31], n[32], 128)
        grafo.agregarArista(n[32], n[33], 98)
        grafo.agregarArista(n[33], n[34], 168)
        grafo.agregarArista(n[33], n[36], 160)
        grafo.agregarArista(n[34], n[35], 158)
        grafo.agregarArista(n[35], n[36], 157)
        grafo.agregarArista(n[20], n[37], 142)
        grafo.agregarArista(n[20], n[38], 116)
        grafo.agregarArista(n[37], n[19], 283)
        grafo.agregarArista(n[37], n[39], 245)
        grafo.agregarArista(n[37], n[40], 279)
        grafo.agregarArista(n[19], n[41], 243)
        grafo.agregarArista(n[19], n[42], 197)
        grafo.agregarArista(n[4], n[43], 789)
        grafo.agregarArista(n[44], n[39], 279)
        grafo.agregarArista(n[39], n[40], 154)
        grafo.agregarArista(n[27], n[36], 107) 

        # Mostrar ciudades
        grafo.mostrarNodos()

        # Ejecutar Floyd–Warshall
        grafo.floydWarshall()

        # Entrada
        origen = int(input("Ingrese el ID del nodo de origen: "))
        destino = int(input("Ingrese el ID del nodo de destino: "))

        grafo.mostrarResultadosRuta(origen, destino)


if __name__ == "__main__":

    main()
