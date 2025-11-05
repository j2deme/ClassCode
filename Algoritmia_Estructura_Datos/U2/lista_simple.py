from nodo import Nodo


class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, item):
        nodo = Nodo(item)
        nodo.siguiente = self.cabeza
        self.cabeza = nodo
