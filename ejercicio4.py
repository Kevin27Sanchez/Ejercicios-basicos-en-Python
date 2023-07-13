suma_impares = 0
contador_impares = 0

for num in range(1, 20, 2):
    suma_impares += num
    contador_impares += 1
    if contador_impares == 10:
        break

print("La suma de los 10 primeros números impares es:", suma_impares)