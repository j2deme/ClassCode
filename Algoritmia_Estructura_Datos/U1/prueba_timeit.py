import timeit

codigo = '''
suma = 0
for i in range(1_000_000):
  suma += i
'''


def sumaN():
    n = 1_000_000
    suma = 0
    for i in range(n):
        suma += i
    return suma


ejecuciones = 10
tiempo = timeit.timeit(sumaN, number=ejecuciones)

print(f"Tiempo promedio: {tiempo / ejecuciones:.6f} segundos")
