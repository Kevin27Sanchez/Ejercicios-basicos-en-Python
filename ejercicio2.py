#Convertir de Kg a gramos y viceversa
def kilogramos_a_gramos(cantidad):
    cantidad_en_gramos=cantidad*1000
    return cantidad_en_gramos

def gramos_a_kilogramos(cantidad):
    cantidad_en_kilogramos=cantidad/1000
    return cantidad_en_kilogramos

def menu():
    print("1. De kilogramos a gramos")
    print("2. De gramos a kilogramos")
    print("3. Salir")

while  True:
    menu()
    opcion=int(input("Elija una opción: "))

    if opcion == 1:
        cantidad = int(input("Ingrese la cantidad en kilogramos: "))
        resultado = kilogramos_a_gramos(cantidad)
        print("La cantidad en gramos es de: ", resultado)

    elif opcion == 2:
        cantidad = int(input("Ingrese la cantidad en gramos: "))
        resultado = gramos_a_kilogramos(cantidad)
        print("La cantidad en kilogramos es de: ", resultado)
    elif opcion == 3:
        break

    else:
        print("Elija una opcion correcta!!!")