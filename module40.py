def add(num1 , num2):
    result = num1+ num2
    print("result is: {}".format(result))

print(hex(id(add)))
print("add is: " , add)

# Execute Copy Operation
add (10,20)

# Reference Copy Operation
hello = add

hello(50,30)

def add (num1 , num2 , num3):
    result = num1 +num2+num3
    print("result is: {}".format(result))

add(80,53,41)