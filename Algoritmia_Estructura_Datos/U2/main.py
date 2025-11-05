from nodo import Nodo
from lista_simple import ListaSimple
from pila import Pila
from cola import Cola

""" Ejemplo de uso de la clase Nodo """
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

print(nodo1.valor, nodo2.valor, nodo3.valor)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

print(nodo1.siguiente.siguiente.valor)  # type: ignore

""" Ejemplo de uso de la clase ListaSimple """
print("Lista Simple")
lista = ListaSimple()
lista.insertar_inicio(10)
lista.insertar_inicio(30)
lista.insertar_inicio(20)

print(lista.cabeza.valor)  # type: ignore

""" Ejemplo de uso de la clase Pila """
print("Pila")
pila = Pila()
pila.push("A")
pila.push("B")
pila.push("C")

print(pila.items)
print(pila.peek())
pila.pop()
print(pila.items)

""" Ejemplo de uso de la clase Cola """
print("Cola")
q = Cola()
# Agregamos varios elementos a la cola
q.enqueue("C")
q.enqueue("A")
q.enqueue("S")
q.enqueue("A")

print(q.items)
q.dequeue()  # Elimina el primer elemento agregado (C)
print(q.items)
q.enqueue("O")  # Agrega un nuevo elemento al final de la cola
q.dequeue()  # Elimina el siguiente elemento (A)
print(q.items)
