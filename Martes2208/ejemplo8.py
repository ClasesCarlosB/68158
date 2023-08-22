

a = input("Ingrese año: ")
a = int(a)

if a % 400 == 0:
    print("BISIESTO")
else:
    if a % 4 == 0 and a % 100 != 0:
        print("Bisiesto")
    else:
        print("No bisiesto")
        