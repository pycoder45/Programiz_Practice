print("-"*50)

# 1.Python Program to Print Hello world!
print("Hello World")

#2.Python Program to Add Two Numbers
a = 2
b = 8
print(a + b)

# 3.Python Program to Find the Square Root
a = 64
Square_root = a**1/2

print(Square_root)

# 4.Python Program to Calculate the Area of a Triangle
base = 5
height = 10 
Area_Of_Tri = base*height*1/2

print(Area_Of_Tri)

# 5.Python Program to Solve Quadratic Equation
a = 3
b = 5
c = -7

sq_term = ( b**2 - 4*a*c )**(1/2)
soln_1 = (-b + sq_term)/(2*a)
soln_2 = (-b - sq_term)/(2*a)

print(f"The Solution Of the Given Quadratic Equation Is \n x = {soln_1} & x = {soln_2}")

print("-"*50)

# 6.Python Program to Swap Two Variables

var_1 = 45
var_2 = 18 

print("Old Variables : ",var_1,var_2)
temp = var_1

var_1 = var_2
var_2 = temp
print("New Variables : ",var_1,var_2)

# 7.Python Program to Generate a Random Number

import random 

num1 = random.random()
num2 = random.randint(0,50) # Gives The Random Integer in perticular range.
num3 = random.sample(range(80,100),5) # Generate A list of 5 random Integer 

print(num1,num2,num3)

# 8.Python Program to Convert Kilometers to Miles

#1 mile = 1.609344 kilometers

km = 12
mile = km/1.609344

print(mile)

# 9.Python Program to Convert Celcius To Fahrenheit

Celcius = 0
Fahrenheit = (Celcius*9/5) + 32 

print(Fahrenheit)

# 10.Python Program to Check if a Number is Positive, Negative or 0

numb = 3

if numb == 0 : 
  print("Number Is Zero")
elif numb >= 0 : 
  print("Number Is Greater Than Zero")
else : 
  print("Number Is Less Thak Zero ")
  
print("-"*50)


# Some tips :
