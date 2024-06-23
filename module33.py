def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        fib = fibonacci(num - 1) + fibonacci(num - 2)
        return fib
    
num = int(input("Enter length of fibonacci series: "))

print("Fibonacci series of is: " , fibonacci(num))