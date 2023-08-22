"""
Pedir por teclado el nombre del usuario. En caso de que el nombre
sea ingresado correctamente, saludarlo. 
En caso contrario, informar el error.

"""

nombre = input("Ingrese nombre: ")

if nombre != "":
    print("Bienvenido", nombre)
else:
    print("Error. Nombre vacio")