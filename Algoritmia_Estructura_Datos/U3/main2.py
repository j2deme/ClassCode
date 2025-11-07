from nodo import Nodo
from bst import BST

arbol = BST()

# Insertamos varios nodos en paquete
nodos = [15, 10, 20, 8, 12, 13]
for n in nodos:
    arbol.insertar(n)

print(arbol)

# Usamos comentarios `# type: ignore` para evitar alertas de linters
print(arbol.raiz.valor, arbol.raiz.izquierda.valor,  # type: ignore
      arbol.raiz.derecha.valor)  # type: ignore

# Impresión visual del árbol (usa la libreria `rich` si está disponible, sino una versión de texto simple).
arbol.mostrar_arbol()


resultado = arbol.buscar(12)  # Cambiar el valor por uno que no exista
if resultado:
    print(f"Encontrado: {resultado.valor}")
else:
    print("No encontrado")
