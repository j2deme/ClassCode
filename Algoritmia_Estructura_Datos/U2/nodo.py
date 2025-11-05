class Nodo:
    def __init__(self, dato):
        self.valor = dato
        self.siguiente: Nodo | None = None
