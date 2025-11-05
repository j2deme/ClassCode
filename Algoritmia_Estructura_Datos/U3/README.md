# Algoritmos de Ordenamiento y Estructuras de Datos Avanzadas - Unidad 3

Esta unidad introduce algoritmos de ordenamiento básicos y estructuras de datos de árbol (Árbol Binario de Búsqueda - BST) con ejemplos didácticos en Python.

El material está pensado para uso en clase: incluye trazas impresas para seguir el comportamiento de los algoritmos y funciones de visualización para presentar estructuras.

## Contenidos

- `nodo.py` — Clase `Nodo` mínima usada por el BST. Contiene `valor`, `izquierda` y `derecha`.

  - Nota: las anotaciones de tipo usan el operador `|` (unión) y por tanto requieren Python 3.10+;
    si se necesita compatibilidad con Python 3.8/3.9, usar `Optional["Nodo"]` o
    `from __future__ import annotations`.

- `bst.py` — Implementación didáctica de un Árbol Binario de Búsqueda (BST).

  - Implementa inserción y utilidades de visualización (usa `rich` si está instalado,
    con fallback textual).

- `ordenamiento.py` — Módulo con algoritmos de ordenamiento didácticos.

  - `Ordenamiento.burbuja` implementa bubble sort con trazas impresas paso a paso.

## Requisitos

- Python 3.10+ recomendado (anotaciones con `|`).
- Opcional: instalar `rich` para una visualización del árbol más amigable:

```bash
pip install rich
```

## ¿Cómo usarlo?

Abre una terminal en la carpeta `Algoritmia_Estructura_Datos/U3` y ejecuta:

- Demo de ordenamiento

  ```bash
  python .\main.py
  ```

- Demo de BST (Binary Search Tree)

  ```bash
  python .\main2.py
  ```

## Notas y retos

- `main.py` usa `random.sample(...)` para generar datos, para reproducir la misma salida, se puede fijar la semilla con `random.seed(42)` antes de la generación.
- En funciones didácticas es habitual imprimir trazas para explicar algoritmos, por lo mismo, veremos muchas impresiones en consola.
