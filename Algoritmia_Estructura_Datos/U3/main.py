from ordenamiento import Ordenamiento
import random

ordenar = Ordenamiento()

# Generamos una lista aleatoria de 10 números.
desordenado = random.sample(range(1, 101), 10)
print(f"Lista desordenada: {desordenado}")

# Usaremos .copy() para mantener el original sin cambios.
arreglo2 = ordenar.burbuja(desordenado.copy())
print(f"Burbuja: {arreglo2}")
