# Dia 3 - 100DaysOfCodeChallenge
# BMI Calculator
height = float(input("Enter your height in m: "))
while height <= 0: 
    height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
while weight <= 0:
    weight = float(input("Enter your weight in kg: "))
# Usando round() ele arredonda para cima ou para baixo
BMI = round(weight / height ** 2, 2)
print(BMI)

# Interpretação dos valores IMC
if BMI < 18.5:
    print("Underweight")
elif(BMI < 25):
    print("Normal weight")
elif(BMI < 30):
    print("Overweight")
elif(BMI < 35):
    print("Obese")
else:
    print("Clinically obese")