#1. Convertir de modeda sol a dolar y viceversa 

def convertir_soles_a_dolares(monto):
    tasa_cambio = 0.28  
    dolares = monto * tasa_cambio
    return dolares

def convertir_dolares_a_soles(monto):
    tasa_cambio = 0.28 
    soles = monto / tasa_cambio
    return soles

def mostrar_menu():
    print("1. Convertir de Soles a Dólares")
    print("2. Convertir de Dólares a Soles")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        monto_soles = float(input("Ingrese el monto en Soles: "))
        monto_dolares = convertir_soles_a_dolares(monto_soles)
        print(f"{monto_soles} Soles equivalen a {monto_dolares} Dólares.\n")
    elif opcion == "2":
        monto_dolares = float(input("Ingrese el monto en Dólares: "))
        monto_soles = convertir_dolares_a_soles(monto_dolares)
        print(f"{monto_dolares} Dólares equivalen a {monto_soles} Soles.\n")
    elif opcion == "3":
        print("Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.\n")
