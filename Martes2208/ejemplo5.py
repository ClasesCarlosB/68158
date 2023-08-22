"""
Un medico nutricionista necesita un programa para calcular el indice de masa 
corporal de sus pacientes:

El indice se calcula como : Peso / (altura^2)

Necesitamos pedir los ingresos, y mostrar los resultados.

Tambien el programa tiene que decidir si:

imc <= 18 : BAJO PESO
18 < imc <= 26 : PESO NORMAL
imc>26: SOBRE PESO

"""

peso = input("Ingrese peso del paciente en kg: ")
peso = float(peso)

altura = input("Ingrese altura del paciente en m: ")
altura = float(altura)

imc = peso / (altura**2)

print("El imc del paciente es:",imc)


if imc <= 18:
    print("Bajo peso")
elif imc <= 26:
    print("Peso normal")
else:
    print("Sobre peso")