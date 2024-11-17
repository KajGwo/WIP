import math;
#WIP
#I
print(int(7+4))
#II
print(int(10+40)/2)
#III
print(int(2**3))
#IV
print(int(7>5))
#V
r=4
#VI
area=3.14159 * r * r
#VII
print(area)
#VIII
print(round(area, 2))
#IX
first_name = "Mary"
#X
last_name = "Brown"
#XI
full_name = first_name + ' ' + last_name
#XII
full_name
#XIII
print(full_name)
#XIV 
len(full_name)
#XV
a = 5
h = 4
print(int((a*h)/2))
#XVI
x=((7+12+31)/3)
print(round(x,2))
#BMI CALC

height = input('height in cm: ')
weight = input('weight in kg: ')
height = float(height)
weight = float(weight)
bmi = weight / (height/100)**2
bmi = round(bmi,2)
print('Your BMI is', bmi)
print('Check on the Internet if your BMI is ok!!')
#DICE ROLLLL
import random
print("Dice rolling simulator")
for i in range(5):
    dice_roll = random.randint(1,6)
    print(dice_roll, end=" ")
#1.1
print(3 * 2 + 1)
print(5 + 10 * 5)
print(4 + 4 / 2 ** 2)
print(4 % 3 % 2 % 1)
print(1 + 2 % 3 ** 4 * 5)
True != False
print(type(50))
print(type(149.17))
print(type(4 * 7))
print(type(4.0 * 7))
print(type("Krakow University of Economics"))
print(type(True))
print(type(2 > 5))
#VARIABLES
num1 = input('num1: ')
num2 = input('num2: ')
num3 = input('num3: ')
result = float(num1) + float(num2) + float(num3)
print('Number 1: ', num1)
print('Number 2: ', num2)
print('Number 3: ', num3)
print('The result of summation: ', result)
#PROGRAM DO ZAMIENIANIA WARTOŚCI ZMIENNYCH 
x = 7
y = 34
z = 0
print("PRZED ZAMIANĄ: x=", x, "y=", y)
z = x
x = y
y = z
print("PO ZAMIANIE: x=", x, "y=", y)
#PROGRAM DO ZAMIANY KM/H NA M/S

kmh = input('km/h?: ')
print("km/h = ", kmh, "m/s = ", (float(kmh) * 0.28))

# A program that calculates the length of the diagonal of a rectangle with sides a and b.
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print(diagonal)

#a program that calculates the distance to the horizon from a height given in meters
h = float(input('twój wzrost w m?: '))
print("dystans do horyzontu to: "math.sqrt(h) * 3.57)













