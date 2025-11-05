"""Nodo usado por estructuras de datos en U3.

Nota de diseño:
- Las anotaciones de tipo `Nodo | None` y el operador `|` para unión requieren Python 3.10+.
"""


class Nodo:
    def __init__(self, valor):
        self.valor: int | str = valor
        self.izquierda: Nodo | None = None
        self.derecha: Nodo | None = None

    def __str__(self) -> str:
        return f"{self.valor}"
