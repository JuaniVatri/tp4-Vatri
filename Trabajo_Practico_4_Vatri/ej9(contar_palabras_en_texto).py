"""jercicio 9: Contar palabras en un texto
Dado el siguiente texto: texto = "manzana naranja manzana pera pera pera naranja manzana"
a) Escribe un programa que cuente cuántas veces aparece cada palabra en el texto utilizando un diccionario.
b) Imprime el diccionario resultante."""

# Dado el texto
texto = "manzana naranja manzana pera pera pera naranja manzana"

# a) Contar cuántas veces aparece cada palabra en el texto utilizando un diccionario
palabras = texto.split()
contador_palabras = {}

for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

# b) Imprimir el diccionario resultante
print(contador_palabras)