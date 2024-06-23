# Conditional Operators
# ==, !=, > , < , >= , <=

cab_fare = 500
e_wallet = 600

result = e_wallet >= cab_fare  #edge case or boundary case >=

print("Can i book the cab: " , result)
print(type(result))


# Logical operators -> and , or

email = input("Enter email: ")
password = input("Enter password: ")

result = (email == "john@example.com") and (password == "john123")


otp = 5228
user_otp = int(input("Enter OTP: "))

print("Is OTP Correct ? ", otp == user_otp)


# Membership Testing
# is, is not

a = 10
b = 10

print (a == b)     # checks if value of a and b is same
print( a is b)     # checks if a and b are pointing to same element i.e they have same hashcode in them
# print(id(a))  -> these are same 
# print(id(b))
print(a is not b)  # false