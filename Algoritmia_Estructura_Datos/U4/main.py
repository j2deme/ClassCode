from recorridos import Recorridos

grafo = {
    0: [4, 5],
    1: [3],
    2: [4],
    3: [1, 4],
    4: [0, 2, 3, 5],
    5: [0, 4],
    6: [8],
    7: [8],
    8: [6, 7]
}

recorrido = Recorridos()
recorrido.dfs(grafo, 0)

print("-----")

recorrido.bfs(grafo, 0)
