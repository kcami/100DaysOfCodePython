# Dia 3 - 100DaysOfCodeChallenge
# Pizza order
size = (input("What size pizza do you want? S, M or L ")).upper()
pepperoni = (input("Do you want pepperoni? Y or N ")).upper()
cheese = (input("Do you want extra cheese? Y or N ")).upper()

if size == "S":
    price = 15
elif size == "M":
    price = 20
else: 
    price = 25

if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3 

if cheese == "Y":
    price += 1
print(f"Your bill is: ${price:.2f}")