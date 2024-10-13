"""Ejercicio 3: Índices y slicing en tuplas
Dada la siguiente tupla: frutas = ("manzana", "banana", "cereza", "naranja", "kiwi")
a) Imprime el segundo elemento de la tupla.
b) Imprime los tres primeros elementos de la tupla.
c) Imprime el último elemento de la tupla usando un índice negativo."""
# Dada la tupla
frutas = ("manzana", "banana", "cereza", "naranja", "kiwi")

# a) Imprimir el segundo elemento de la tupla
segundo_elemento = frutas[1]
print("Segundo elemento:", segundo_elemento)

# b) Imprimir los tres primeros elementos de la tupla
tres_primeros = frutas[:3]
print("Tres primeros elementos:", tres_primeros)

# c) Imprimir el último elemento de la tupla usando un índice negativo
ultimo_elemento = frutas[-1]
print("Último elemento:", ultimo_elemento)