#Ingresar 10 letras e indicar cuantas son vocales y cuantos son consonantes
import random

for i in range (10):
    letra = chr(random.randint(97, 112)) 
    print("Letra :", letra)

    if letra.isalpha():
        if letra.lower() in "aeiou":
            print(letra, "es una vocal.")
        else:
            print(letra, "es una consonante.")

