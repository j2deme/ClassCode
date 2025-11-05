"""Algoritmos de ordenamiento didácticos.

Contiene implementaciones sencillas con trazas impresas para seguir el proceso paso a paso.
"""


class Ordenamiento:

    def burbuja(self, arr):
        # Bubble sort clásico (complejidad O(n^2)).
        n = len(arr)
        for i in range(0, n - 1):
            for j in range(0, n - i - 1):
                # Muestra el proceso de comparación e intercambio.
                print(f"i: {i}, j:{j}, compara {arr[j]} con {arr[j+1]}")
                if arr[j] > arr[j + 1]:
                    print(f"Intercambia {arr[j]} con {arr[j+1]}")

                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        return arr

    def insercion(self, arr):
        # Insertion sort clásico (complejidad O(n^2)).
        n = len(arr)
        for i in range(1, n):
            clave = arr[i]
            j = i - 1
            # Muestra el proceso de comparación e inserción.
            while j >= 0 and arr[j] > clave:
                print(f"i: {i}, j:{j}, compara {arr[j]} con {clave}")
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = clave
        return arr
