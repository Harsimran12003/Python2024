# Bubble Sort
print("----------BUBBLE SORT-------------")
numbers = []
length = int(input("Enter number of elements: "))
print("Enter numbers for list: ")

for idx in range (0 , length):
    num = int(input())
    numbers.append(num)


print("List of numbers: " , numbers)


for i in range( 0 , len(numbers)):
    for j in range ( i+1 , len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print("Sorting in ascending order : " , numbers)

