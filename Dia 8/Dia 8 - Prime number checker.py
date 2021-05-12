# Dia 8 - 100DaysOfCodeChallenge
# Prime number checker
def prime_checker(number):
    is_prime = True
    for possible_divisors in range(2, number//2 + 1):
        if(number % possible_divisors == 0):
            
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number.")

number = int(input("Write a number: "))
prime_checker(number)