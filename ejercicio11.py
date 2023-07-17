#numero entero y diferente a 0 e indicar si es par o impar
numero = 0

while numero == 0:
    try:
        numero = int(input("Ingrese un número diferente de cero: "))
        if numero == 0:
            print("El número debe ser diferente de cero. Inténtelo nuevamente.")
    except ValueError:
        print("Error: Debe ingresar un número entero. Inténtelo nuevamente.")

if numero %2 == 0:
    print("El número ", numero, " es par")
else:
    print("El número ", numero, " es impar")
