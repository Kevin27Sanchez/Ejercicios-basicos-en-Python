# 4. Calcular el factorial de un numero
def factorial (numero):
    resultado= 1
    for i in range(1,numero+1):
        resultado = resultado*i

numero=int(input("Ingrese un número: "))
resultado = factorial(numero)
print("El factorial del número ingresado es: ", resultado)