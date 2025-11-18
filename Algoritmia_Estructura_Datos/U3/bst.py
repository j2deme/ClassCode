from nodo import Nodo


class BST:
    """Árbol binario de búsqueda (BST).

    Observaciones de diseño / uso:
    - Las anotaciones usan `Nodo | None` (requiere Python 3.10+).
    - Los duplicados, por la implementación actual, se insertan en la rama
      derecha (debido al `else` en la comparación).
    """

    def __init__(self):
        # Raíz del árbol; None si el árbol está vacío.
        self.raiz: Nodo | None = None

        # Intento de mejorar la impresión si la librería `rich` está disponible.
        # Esto no cambia la lógica, solo la presentación.
        try:
            from rich import print  # type: ignore
        except ImportError:
            pass

    def insertar(self, valor) -> Nodo:
        # Inserción pública: si la raíz no existe, se crea. En otro caso,
        # delegamos en el helper recursivo `_insertar`.
        if self.raiz is None:
            self.raiz = Nodo(valor)
        elif valor < self.raiz.valor:
            self.raiz.izquierda = self._insertar(self.raiz.izquierda, valor)
        else:
            # Los duplicados caerán por la rama derecha.
            self.raiz.derecha = self._insertar(self.raiz.derecha, valor)
        return self.raiz

    def _insertar(self, nodo, valor) -> Nodo:
        # Helper recursivo: crea un nuevo nodo si la posición es None;
        # en caso contrario baja por la rama apropiada.
        if nodo is None:
            nodo = Nodo(valor)
        elif valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        else:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        return nodo

    def buscar(self, valor):
        # - Devolver el nodo que contiene `valor` o None si no existe.
        if self.raiz is None:
            return None
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        else:
            return self._buscar(nodo.derecha, valor)

    def eliminar(self, valor):
        # Definimos un método público para eliminar un nodo con el valor dado.
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        # Casos a cubrir:
        # 1) Nodo hoja -> reemplazar por None
        # 2) Nodo con un hijo -> reemplazar por su hijo
        # 3) Nodo con dos hijos -> reemplazar por el sucesor (mínimo del subárbol
        # derecho) y eliminar ese sucesor.
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            # Nodo encontrado
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            # Nodo con dos hijos: obtener el sucesor (mínimo del subárbol derecho)
            sucesor = self.minimo(nodo.derecha)

            nodo.valor = sucesor.valor  # type: ignore
            nodo.derecha = self._eliminar(
                nodo.derecha, sucesor.valor)  # type: ignore

        return nodo

    def minimo(self, nodo):
        if nodo is None:
            return None

        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo

    def mostrar_arbol(self):
        """Muestra el árbol usando rich.tree si está disponible.

        Este método es puramente de presentación; el árbol en sí no se modifica.
        Se usan emojis para hacer la salida más didáctica.
        """
        try:
            from rich.tree import Tree  # type: ignore
            from rich import print  # type: ignore

            if self.raiz is None:
                print("🌳 El árbol está vacío")
                return

            tree = Tree(f"🌱 Raíz: {self.raiz.valor}", style="bold green")
            self._construir_arbol_rich(self.raiz, tree)
            print(tree)

        except ImportError:
            # Fallback a impresión simple
            self._mostrar_arbol_simple()

    def _construir_arbol_rich(self, nodo, arbol_rich):
        """Construye recursivamente ramas para `rich.Tree`.

        Nota: este método solo se usa si `rich` está instalado.
        """
        if nodo.izquierda:
            izquierda_rama = arbol_rich.add(
                f"👈 Izq: {nodo.izquierda.valor}", style="red")
            self._construir_arbol_rich(nodo.izquierda, izquierda_rama)
        elif nodo.derecha:
            # Añadir marcador explícito de vacío para claridad visual.
            arbol_rich.add("👈 Izq: ∅", style="dim red")

        if nodo.derecha:
            derecha_rama = arbol_rich.add(
                f"👉 Der: {nodo.derecha.valor}", style="blue")
            self._construir_arbol_rich(nodo.derecha, derecha_rama)
        elif nodo.izquierda:
            arbol_rich.add("👉 Der: ∅", style="dim blue")

    def _mostrar_arbol_simple(self):
        """Impresión de respaldo sin `rich` (estructura textual).
        """
        if self.raiz is None:
            print("Árbol vacío")
            return
        self._mostrar_arbol_recursivo(self.raiz, 0, "Raíz:")

    def _mostrar_arbol_recursivo(self, nodo, nivel, prefijo=""):
        """Imprime el nodo actual y luego sus hijos (si existen), mostrando
        explícitamente nodos vacíos para que la forma del árbol sea clara.
        """
        if nodo is not None:
            espacios = "  " * nivel
            print(f"{espacios}{prefijo} {nodo.valor}")

            if nodo.izquierda or nodo.derecha:
                if nodo.izquierda:
                    self._mostrar_arbol_recursivo(
                        nodo.izquierda, nivel + 1, "I--")
                else:
                    espacios_vacios = "  " * (nivel + 1)
                    print(f"{espacios_vacios}I-- ∅")

                if nodo.derecha:
                    self._mostrar_arbol_recursivo(
                        nodo.derecha, nivel + 1, "D--")
                else:
                    espacios_vacios = "  " * (nivel + 1)
                    print(f"{espacios_vacios}D-- ∅")
