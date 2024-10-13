"""Ejercicio 4: Verificar existencia de un elemento
Dada la tupla: colores = ("rojo", "verde", "azul", "amarillo")
a) Verifica si el color "morado" está presente en la tupla.
b) Verifica si el color "azul" está presente en la tupla.
c) Imprime el resultado de ambas verificaciones."""
# Dada la tupla
colores = ("rojo", "verde", "azul", "amarillo")

# a) Verificar si el color "morado" está presente en la tupla
morado_presente = "morado" in colores

# b) Verificar si el color "azul" está presente en la tupla
azul_presente = "azul" in colores

# c) Imprimir el resultado de ambas verificaciones
print("¿Está 'morado' presente en la tupla?", morado_presente)
print("¿Está 'azul' presente en la tupla?", azul_presente)