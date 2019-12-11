MATERIAS = 3

# Datos del alumno
print("Alumno 1")
nombre = input("Nombre completo: ")
grado = input("Grado: ")
grupo = input("Grupo: ")

# Hacer un ciclo, pedir datos y sumar la calificación
contador = 1
sumatoria = 0
while contador <= MATERIAS:
    nombre_materia = input("Nombre de la materia {}: ".format(contador))
    calificacion = float(input("Calificación en {}: ".format(nombre_materia)))
    # Sumar la calificación a la sumatoria
    sumatoria = sumatoria + calificacion
    # Aumentar el contador para no hacer un ciclo infinito
    contador = contador + 1
# Hacer cálculos e imprimir resultados
promedio = sumatoria / MATERIAS
print("""***** Resultados *****
Alumno: {} | {} {}
*******************************
* Promedio: {}
*******************************
""".format(nombre, grupo, grado, promedio))




# Datos del alumno
print("alumno 2") 
nombree = input("Nombre completo: ")
gradoo = input("Grado: ")
grupoo = input("Grupo: ")


# Hacer un ciclo, pedir datos y sumar la calificación
contador = 1
sumatoria = 0
while contador <= MATERIAS:
    nombre_materiaa = input("Nombre de la materia {}: ".format(contador))
    calificacion = float(input("Calificación en {}: ".format(nombre_materiaa)))
    # Sumar la calificación a la sumatoria
    sumatoria = sumatoria + calificacion
    # Aumentar el contador para no hacer un ciclo infinito
    contador = contador + 1


# Hacer cálculos e imprimir resultados
promedio = sumatoria / MATERIAS
print("""***** Resultados *****
Alumno: {} | {} {}
*******************************
* Promedio: {}
*******************************
""".format(nombree, grupoo, gradoo, promedio))


# Datos del alumno
print("alumno 3") 
nombre3 = input("Nombre completo: ")
grado3 = input("Grado: ")
grupo3 = input("Grupo: ")

# Hacer un ciclo, pedir datos y sumar la calificación
contador = 1
sumatoria = 0
while contador <= MATERIAS:
    nombre_materia3 = input("Nombre de la materia {}: ".format(contador))
    calificacion = float(input("Calificación en {}: ".format(nombre_materia3)))
    # Sumar la calificación a la sumatoria
    sumatoria = sumatoria + calificacion
    # Aumentar el contador para no hacer un ciclo infinito
    contador = contador + 1

# Hacer cálculos e imprimir resultados
promedio = sumatoria / MATERIAS
print("""***** Resultados *****
Alumno: {} | {} {}
*******************************
* Promedio: {}
*******************************
""".format(nombr3, grupo3, grado3, promedio))
