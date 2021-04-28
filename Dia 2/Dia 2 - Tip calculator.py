# Day 2 - 100DaysOfCodeChallenge
# Tip calculator
print("Welcome to the tip calculator")

total = float(input("What was the total bill? "))
while total <= 0:
    total = float(input("What was the total bill? "))

people = float(input("How many people to slipt the bill? "))
while people <= 0:
    people = float(input("How many people to slipt the bill? "))

percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
while percentage not in [10, 12, 15]:
    percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
value = round((total + total * percentage / 100) / people, 2)
print(f"Each person should pay: {value:.2f}")