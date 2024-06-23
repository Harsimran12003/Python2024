file = open("customer.csv" , "r")
# data = file.read()
# print(data)

lines = file.readlines()

print("File Data: ")
print(lines)
file.close()