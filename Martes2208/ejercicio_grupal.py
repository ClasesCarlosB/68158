"""
Calculadora de promedios

Pedir nombre del alumno. Luego pedir 3 notas por teclado. 
Y para finalizar, mostrar el promedio, decidir si el alumno,
esta aprobado o desaprobado.

Se aprueba con 6(inclusive).

"""

nombre = input("Ingrese nombre del alumno: ")

nota1 = input("Ingrese primer nota: ")
nota1 = float(nota1)

nota2 = input("Ingrese segunda nota: ")
nota2 = float(nota2)

nota3 = input("Ingrese tercer nota: ")
nota3 = float(nota3)


promedio = (nota1 + nota2 + nota3) / 3

print(nombre," tiene un promedio de:",promedio)

if promedio>=6:
    print("El alumno",nombre,"esta aprobado")
else:
    print("El alumno",nombre,"esta desaprobado")
 