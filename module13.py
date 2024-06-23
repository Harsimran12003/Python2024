#Bitwise Operators
# &, |, ^

num1 = 10
num2 = 8
print(bin(num1))
print(bin(num2))

result1 = num1 & num2  #AND
result2 = num1 | num2  #OR
result3 = num1 ^ num2  #XOR

print(result1)
print(result2)
print(result3)

#Shift Operators
# >> , <<

num1 = 8
num2 = 2
result1 = num1 >> num2    # 8 / 2^2

print("Result right shift: " , result1)

number = result1 << num2
print("Number: " , number)

result2 = num1 << num2   # 8 * 2^2

print("Result left shift: " , result2)

number = -11
result = number >> 2
print(result)

# 13
# >> 2
# 0 0 0 0  1 1 0 1
# - - 0 0  0 0 1 1 -> 3

# -11
# 1 1 1 1  0 1 0 0
#                1
# 1 1 1 1  0 1 0 1
# >> 2

# _ _ 1 1  1 1 0 1
# 1 1 1 1  1 1 0 1

# 0 0 0 0  0 0 1 0
#                1
# 0 0 0 0  0 0 1 1  -> -3

# -13

# 0 0 0 0  1 1 0 1

# 1 1 1 1  0 0 1 0
#                1
# 1 1 1 1  0 0 1 1

# _ _ 1 1  1 1 0 0
# 1 1 1 1  1 1 0 0 

# 0 0 0 0  0 0 1 1
#                1
# 0 0 0 0  0 1 0 0 -> -4