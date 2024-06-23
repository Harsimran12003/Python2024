#Operators
#Arithmetic Operators
#+ , - , /, **, //, %

product_price = 200
gst_tax = 0.18

price_to_pay = product_price + gst_tax * product_price
print(price_to_pay , type(price_to_pay) , id(price_to_pay))

number = 10

result = number/3 
print("Result: " , result)     #floating point division
result = number // 3   #integral division
print("Result: " , result)

base = 2
result = base * 2
print(result)
result = base ** 3    #raised to power
print(result)

bucket_size = 7
hashcode = 120 % bucket_size   #remainder operator
print("Hashcode: " , hashcode)


#Assignment Operator
# = , += ,  -=, *= , **=, /=, //=, %=

#A new reference variable age, will be created in Stack
#A container 20 will be created in Heap
#Hashcode of 20 will be stored in age
#Hence, age is a REFERENCE VARIABLE

age = 20

#UPDATE OPERATION
#age = age + 10
age += 10      #Shorthand operator add and assign
print("Age : " , age)

age %= 3
age //= 3
print("Age : " , age)
age -= 1
print("Age : " , age)


#Increment and decrement
qty = 1
qty += 1
qty -= 1
qty += 5
qty -= 1
qty **= 2
print("Quantity: " , qty)