# Day 2 - 100DaysOfCodeChallenge
# BMI calculator
height = float(input("Enter your height in m: "))
while height <= 0: 
    height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
while weight <= 0:
    weight = float(input("Enter your weight in kg: "))
# Usando round() ele arredonda para cima ou para baixo 
print(round(weight / height ** 2))
