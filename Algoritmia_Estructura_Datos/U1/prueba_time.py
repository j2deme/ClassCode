import time

inicio = time.time()
suma = 0
for i in range(1_000_000):
    suma += i
fin = time.time()
print(f"Tiempo: {fin - inicio:.4f} segundos.")
