#!/usr/bin/env python3

"""
Escribir un programa que lea 10 números enteros desde el teclado simulando una encuesta que pregunte a
una muestra de 10 personas "¿Cuánto mide (cm)?
Las respuestas se deberán almacenar en una lista.
La salida del programa debe ser la media y la desviación típica de la variable aleatoria "altura"
"""

print('Enunciado ejercicio #001')
print('------------------------')
print('Escribir un programa que lea 10 números enteros desde el teclado simulando una encuesta que pregunte a')
print('una muestra de 10 personas "¿Cuánto mide (cm)?')
print('Las respuestas se deberán almacenar en una lista.')
print('La salida del programa debe ser la media y la desviación típica de la variable aleatoria "altura"')

# Start with an empty list
data = []
num = 3

# Read the heights
n = 0
while n < num:
    print("Encuesta #", n+1," ")
    height = int(input("¿Cuánto mides (cm)? "))
    data.append(height)
    n += 1 

# Calculate the average
sum = 0
for x in data:
    sum += x

average = sum / num
print("La altura media es", average, "cm")

# Calculate the standard deviation
import math
sum = 0
for x in data:
    sum += (x - average)**2

std = math.sqrt(sum/num)
print("La desviación estándar es", std, "cm")


