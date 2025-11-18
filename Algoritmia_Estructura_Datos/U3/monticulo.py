class Monticulo:
    """Montículo (heap) configurable como máximo o mínimo.

    Implementación basada en arreglo (array heap)

    Parámetros:
    - A: iterable opcional con los elementos iniciales (no se hace heapify
      automáticamente; llamar a `build_heap()` si se quiere convertir `A` en
      un montículo válido).
    - max_heap: True para montículo máximo (por defecto), False para mínimo.
    """

    def __init__(self, A=None, max_heap=True):
        """Inicializa el montículo.

        Si se proporciona `A`, se copia a una lista interna `self.A`. Para
        convertir esa lista en un montículo válido, llamar a `build_heap()`.
        """
        self.A = list(A) if A is not None else []
        self.max_heap = max_heap

    def _swap(self, i, j):
        """Intercambia los elementos en las posiciones `i` y `j`.

        Método de utilidad interno; no realiza comprobaciones de rango para
        mantener la implementación ligera.
        """
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def parent(self, i):
        """Devuelve el índice del padre del nodo en posición `i`.

        - Fórmula: (i - 1) // 2.
        - Para i == 0 devuelve `None` en lugar de -1 para evitar indexación
            negativa accidental cuando se usa como índice (p. ej. `self.A[-1]`).
        """
        if i <= 0:
            return None
        return (i - 1) // 2

    def left(self, i):
        """Índice del hijo izquierdo de `i` (2*i + 1)."""
        return 2 * i + 1

    def right(self, i):
        """Índice del hijo derecho de `i` (2*i + 2)."""
        return 2 * i + 2

    def _compare(self, x, y):
        """Comparador interno que respeta el tipo de montículo.

        - Si `max_heap` es True, devuelve True cuando `x > y`.
        - Si `max_heap` es False (min-heap), devuelve True cuando `x < y`.

        Usado para seleccionar el hijo "óptimo" y decidir si subir/bajar.
        """
        return x > y if self.max_heap else x < y

    def shift_up(self, i):
        """Reposiciona el elemento en `i` hacia arriba hasta restaurar el
        invariante del montículo.

        Se usa tras `insertar` para mover el nuevo elemento a su posición.
        """
        # Usar parent de forma segura (puede devolver None cuando i == 0).
        p = self.parent(i)
        while p is not None and self._compare(self.A[i], self.A[p]):
            self._swap(i, p)
            i = p
            p = self.parent(i)

    def shift_down(self, i, n=None):
        """Reposiciona el elemento en `i` hacia abajo dentro del prefijo de
        longitud `n` (por defecto toda la lista) hasta restaurar el heap.

        Parámetros:
        - i: índice desde el que empezar a bajar.
        - n: tamaño efectivo del heap (útil cuando se implementan heapsort).

        Algoritmo:
        - Selecciona el hijo "óptimo" (mayor para max-heap, menor para
          min-heap) entre izquierdo/derecho.
        - Si el padre ya satisface la relación (_compare padre, hijo), se
          detiene; en caso contrario, intercambia y continúa.
        """
        if n is None:
            n = len(self.A)
        while self.left(i) < n:
            j = self.left(i)
            # Si existe hijo derecho y éste es "mejor" que el izquierdo,
            # elegir el derecho.
            if j + 1 < n and self._compare(self.A[j + 1], self.A[j]):
                j = j + 1
            # Si el padre ya es "mejor" que el hijo elegido, la propiedad
            # del heap se cumple y se puede detener.
            if self._compare(self.A[i], self.A[j]):
                break
            self._swap(i, j)
            i = j

    def insertar(self, clave):
        """Inserta `clave` en el montículo manteniendo la propiedad de heap.

        Inserta al final y luego aplica `shift_up` para colocarla correctamente.
        """
        self.A.append(clave)
        self.shift_up(len(self.A) - 1)

    def extraer_max(self):
        """Extrae y devuelve el elemento en la raíz (`self.A[0]`).

        Observaciones:
        - El nombre conserva `max` por compatibilidad con montículos máximos;
          si la instancia fue creada con `max_heap=False`, el método devolverá
          el elemento de la raíz del min-heap.
        - Lanza `IndexError` si el montículo está vacío.
        """
        if not self.A:
            raise IndexError('Se intento extraer de montículo vacío')
        top = self.A[0]
        last = self.A.pop()
        if self.A:
            # Reemplazamos raíz por el último elemento y bajamos para restaurar
            # la propiedad del heap.
            self.A[0] = last
            self.shift_down(0)
        return top

    def peek(self):
        """Devuelve el elemento en la raíz (`self.A[0]`) sin extraerlo.

        Lanza `IndexError` si el montículo está vacío.
        """
        if not self.A:
            raise IndexError('Se intento acceder a montículo vacío')
        return self.A[0]

    def build_heap(self):
        """Convierte la lista interna en un montículo válido en O(n).

        Aplica el procedimiento de heapify iterando desde el último padre
        hasta la raíz y llamando a `shift_down`.
        """
        n = len(self.A)
        # Índice del último padre en un heap de tamaño n: (n // 2) - 1
        # Esto evita depender de parent(n-1) y de valores None/-1.
        last_parent = (n // 2) - 1
        for i in range(last_parent, -1, -1):
            self.shift_down(i)
