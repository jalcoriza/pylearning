#!/usr/bin/env python3

"""
Ejemplos de python
by jav
"""

# Elementary python use samples
print("Hello")

# Data classes
print("The type of '3.2' is", type(3.2))

# Type conversion int()/float()/str()
print("The pi number is", float('3.1415'))

# Conventions
# i) variables begin with a small letter
# ii) constants are written in capital letters
PI = 3.1415
r1 = 25.54
perimeter = 2*PI*r1

print("The perimeter of a circle with radius of 25.54cm is equal to", perimeter, "cm")

decimal = 3 + len("hi")
print(decimal)

print("Algunas expresiones matemáticas")
print("2^20=",2**20)
print("27/4 tiene un cociente de", 27//4,"y un resto de",27%4,"i.e. ",27//4,"x 4 +",27%4,"= 27")

print("Algunas expresiones lógics")
print("True or False =", True or False)
print("7>=9 =",7>=9)

print("Algunos ejemplos de manejo de strings")
print("Concatenación: 'hol'+'a' =",'hol'+'a')
print("Repetición: 'ja' * 3=",'ja'*3)

# Notas rápidas
type(2**1024)
age = int(input('Tell me your age: '))
print('Your age is', age)

if age >= 18:
    print('You can drive')
else:
    print('You can\'t drive')

weight = float(input("What's your weigth in kg? "))
height = float(input("What's your weight in meters? "))
imc = weight / (height**2)

print("Your IMC is ",imc," so...")
if imc < 18.5:
    print("You're in good shape!")
elif imc >= 18.5 and imc < 25:
    print("You're in average shape!")
else:
    prinf("You're overweight!")

cars = ['Ford', 'Volvo', 'Tesla']
print(cars)
cars.append('Toyota')
x = cars[0]
print(cars)
cars.clear()
print(cars)

for a in range(1,10+1,1):
    print(a)

vehiculo = ['coche', 'moto', 'camion']
for i, v in enumerate(vehiculo):
    print(i, v)

altura_max = [4, 1.77, 4.5]
for i, v in zip(vehiculo, altura_max):
    print(i, v)

def potencia(base, exponente):
    return base**exponente

print('2^10=',potencia(2,10))

def f_vacia():
    print('Esta finción no devuelve nada')

n = f_vacia()
print(type(n))
print(n)

def s_to_hms(sec):
    h = sec//3600
    m = (sec%3600)//60
    s = (sec%3600)%60 
    return(h, m, s)

time=8273648273
[h, m, s] = s_to_hms(time)
print(time,'seconds are ',h ,' hours, ',m ,'minutes and ',s ,'seconds')

a = [[1,2,3,4],[5,6],[7,8,9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()

thisdict = {
        'apple': 'green',
        'banana': 'yellow',
        'cherry': 'red'
}
print(thisdict)

thisdict['apple'] = 'red'
print(thisdict)

thatdict = dict(apple='green', banana='yellow', cherry='red')
thatdict['damson'] = 'purple'
print(thatdict)

# Intercambiar dos columnas de una matriz
def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]

def print_matrix(m):
    for row in m:
        print(row)


n, m = 3, 3
a = [[2, 4, 3], [1, 1, 1], [0, 0, 0]]
print_matrix(a)

i, j = [int(i) for i in input('columns to swap: ').split()]
swap_columns(a, i, j)
print_matrix(a)


