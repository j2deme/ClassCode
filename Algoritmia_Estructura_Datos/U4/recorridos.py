from collections import deque


class Recorridos:
    '''
    Versión básica del recorrido en profundidad (DFS) de un grafo.

    Limitaciones:
    - No maneja grafos dirigidos o ponderados.
    - No detecta ciclos.
    - No trata componentes desconectados.
    '''

    def dfs(self, grafo, inicio):
        visitado = set()
        pila = [inicio]
        while pila:
            v = pila.pop()
            if v not in visitado:
                visitado.add(v)
                print(v)
                pila.extend(reversed(grafo[v]))
        return visitado

    '''
    Versión básica del recorrido en anchura (BFS) de un grafo.

    Limitaciones:
    - No maneja grafos dirigidos o ponderados.
    - No detecta ciclos.
    - No detalla niveles de profundidad.
    '''

    def bfs(self, grafo, inicio):
        visitado = set()
        cola = deque([inicio])
        visitado.add(inicio)
        while cola:
            v = cola.popleft()
            print(v)
            for vecino in grafo[v]:
                if vecino not in visitado:
                    visitado.add(vecino)
                    cola.append(vecino)
        return visitado
