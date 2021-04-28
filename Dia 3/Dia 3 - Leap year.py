# Dia 3 - 100DaysOfCodeChallenge
# Leap year
year = int(input("Which year do you want to check?"))
while year < 0:
    year = int(input("Which year do you want to check?"))
if (year % 4 != 0):
    print("Not leap!")
elif (year % 100) == 0 and (year % 400) != 0:
    print("Not leap!")
else:
    print("Leap!")
    