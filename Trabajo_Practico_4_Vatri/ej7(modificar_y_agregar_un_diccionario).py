"""Ejercicio 7: Modificar un diccionario
Dado el siguiente diccionario: persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
a) Cambia el valor de la clave edad a 31.
b) Agrega una nueva clave profesión con el valor "Ingeniero".
c) Imprime el diccionario modificado."""
# Dado el diccionario
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# a) Cambiar el valor de la clave edad a 31
persona["edad"] = 31

# b) Agregar una nueva clave profesión con el valor "Ingeniero"
persona["profesión"] = "Ingeniero"

# c) Imprimir el diccionario modificado
print(persona)