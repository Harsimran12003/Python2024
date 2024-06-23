numbers= [10,20,30,40,50]

#REFERENCE COPY OPERATION -> copy the hashcode
my_numbers= numbers

print (numbers, id(numbers), type(numbers))
print (my_numbers, id(my_numbers), type(my_numbers))

numbers[2]=35
print(my_numbers[2], type(my_numbers[2])) #change in one will cause change in other

del(numbers)
print(my_numbers) #my_numbers will not be deleted

num=[10,20,"30"]
print(type(num[2])) #double quoted data is string type