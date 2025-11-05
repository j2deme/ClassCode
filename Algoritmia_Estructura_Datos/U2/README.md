# Algoritmia y Estructura de Datos - Unidad 2

En esta unidad se implementan y prueban estructuras de datos lineales básicas usando Python: listas enlazadas simples, pilas y colas.

El objetivo es comprender la representación mediante nodos y las operaciones fundamentales (inserción, eliminación, recorrido).

## Contenidos

- `nodo.py` — Definición de la clase `Nodo` usada por las estructuras enlazadas. Contiene el valor y la referencia al siguiente nodo.
- `lista_simple.py` — Implementación de una lista enlazada simple (_single linked list_), con operaciones típicas como insertar al inicio/fin, buscar, eliminar, recorrer.
- `pila.py` — Implementación de una pila (LIFO), con operaciones `push`, `pop`, `peek`, `is_empty`.
- `cola.py` — Implementación de una cola (FIFO), con operaciones `enqueue`, `dequeue`, `front`, `is_empty`.

## ¿Cómo usarlo?

1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Abre una terminal en la carpeta `Algoritmia_Estructura_Datos/U2` o utiliza un entorno de desarrollo como VSCode para ejecutar el código.
3. Ejecuta el script principal:

```bash
python .\main.py
```

## Notas y retos

- Revisa `nodo.py` para entender la estructura del nodo antes de modificar `lista_simple.py`.
- Considera añadir métodos adicionales como `size()` o `reverse()` como ejercicio.
