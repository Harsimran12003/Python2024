# What is a Function/method/Procedure
# A function is a piece of code, which we use again and again
# It can input, which is processed and give output

def f(x):
    y = x * x + 1
    print(y)

f(1)
f(2)
f(3)

def whole_square(a,b):
    result = a*a + b*b + 2*a*b
    print("Result: " , result)

whole_square(5,2)    
whole_square(a=5,b=2)