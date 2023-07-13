def natural_a_romano(numero):
    if numero == 1:
        resultado = "I"
        return resultado
    elif numero == 2:
        resultado = "II"
        return resultado
    elif numero == 3:
        resultado = "III"
        return resultado
    elif numero == 4:
        resultado = "IV"
        return resultado
    elif numero == 5:
        resultado = "V"
        return resultado
    elif numero == 6:
        resultado = "VI"
        return resultado
    elif numero == 7:
        resultado = "VII"
        return resultado
    elif numero == 8:
        resultado = "VIII"
        return resultado
    elif numero == 9:
        resultado = "IX"
        return resultado
    elif numero == 10:
        resultado = "X"
        return resultado
    
numero = int(input("Ingrese un numero: "))
resultado = natural_a_romano(numero)
print("Su equivalente en número romano es: ",resultado)
