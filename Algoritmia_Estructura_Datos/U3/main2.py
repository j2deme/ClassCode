from nodo import Nodo
from bst import BST

arbol = BST()

# Insertamos varios nodos en paquete
nodos = [15, 3, 20, 25, 8, 4]
for n in nodos:
    arbol.insertar(n)

print(arbol)

# Usamos comentarios `# type: ignore` para evitar alertas de linters
print(arbol.raiz.valor, arbol.raiz.izquierda.valor,  # type: ignore
      arbol.raiz.derecha.valor)  # type: ignore

# Impresión visual del árbol (usa la libreria `rich` si está disponible, sino una versión de texto simple).
arbol.mostrar_arbol()
