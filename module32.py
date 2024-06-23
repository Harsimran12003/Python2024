#FACTORIAL OF NUMBER
def factorial(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        fact = number * factorial(number - 1)
        return fact

num = int(input("Enter number to print factorial: "))

print("Factorial of" , num , "is:" , factorial(num))