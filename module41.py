def add (num1 , num2 , num3):
    result = num1 +num2+num3
    print("result is: {}".format(result))

add(num2 = 87 , num1 = 98, num3= 54)

# Default Arguments/Inputs
def square(num=5):
    result = num * num
    print("result is: {}".format(result))

square()
square(3)
square(num = 8)

# def subtract(num1=10 , num2): -> error
def subtract(num1 , num2 = 5):  #default values have right to left sequence
    result = num1 - num2
    print("result is: {}".format(result))

subtract(num1 = 10)