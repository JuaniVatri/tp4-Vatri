"""Ejercicio 5: Contar elementos en una tupla
Dada la siguiente tupla:
numeros = (1, 2, 2, 3, 4, 4, 4, 5)
a) Cuenta cuántas veces aparece el número 4 en la tupla.
b) Imprime el resultado."""
# Dada la tupla
numeros = (1, 2, 2, 3, 4, 4, 4, 5)

# a) Contar cuántas veces aparece el número 4 en la tupla
cantidad_4 = numeros.count(4)

# b) Imprimir el resultado
print("El número 4 aparece", cantidad_4, "veces en la tupla")