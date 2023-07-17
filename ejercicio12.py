#20 edades y decir cuales son mayores y menores de edad
import random

edades = []

for _ in range(20):
    edad = random.randint(1, 100) 
    edades.append(edad)

print("Todas las edades generadas:", edades)

mayores_de_edad = [edad for edad in edades if edad >= 18]
print("Edades mayores de edad:", mayores_de_edad)

menores_de_edad = [edad for edad in edades if edad < 18]
print("Edades mayores de edad:", menores_de_edad)
 