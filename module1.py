#Our Very First Program
# Containers

#Single Value Container

#Create statement ->to create SVC in RAM
#username is a reference variable
user_name = "auribises"

#Read statement -> to read data inside a container
print(user_name, id(user_name), type(user_name))

#UPDATE statement
user_name = "harsimran"
print(user_name, id(user_name), type(user_name))

user_name = 123
print(user_name, id(user_name), type(user_name))

#DELETE statement
del user_name
