"""Ejercicio 10: Diccionario anidado
Dado el siguiente diccionario de alumnos: alumnos = { "alumno1": {"nombre": "Carlos", "edad": 20, "nota": 8.5}, "alumno2": {"nombre": "Lucía", "edad": 22, "nota": 9.0}, "alumno3": {"nombre": "Ana", "edad": 21, "nota": 7.5}, }
a) Imprime el nombre del alumno2.
b) Imprime la nota del alumno3."""
# Dado el diccionario de alumnos
alumnos = {
    "alumno1": {"nombre": "Carlos", "edad": 20, "nota": 8.5},
    "alumno2": {"nombre": "Lucía", "edad": 22, "nota": 9.0},
    "alumno3": {"nombre": "Ana", "edad": 21, "nota": 7.5},
}

# a) Imprimir el nombre del alumno2
nombre_alumno2 = alumnos["alumno2"]["nombre"]
print("Nombre del alumno2:", nombre_alumno2)

# b) Imprimir la nota del alumno3
nota_alumno3 = alumnos["alumno3"]["nota"]
print("Nota del alumno3:", nota_alumno3)