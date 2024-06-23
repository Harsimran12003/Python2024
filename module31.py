""" numbers = [1 , 3 ,5]

max = numbers[0]

for idx in range (1 , len(numbers)):
    if numbers[idx] > max:
        max = numbers[idx]

print("Max: " , max) """

def max(data , length):
    if length == 1:
        return data[0]
    
    else:
        previous = max(data, length-1)
        current = data [length-1]

        if previous > current:
            return previous
        else: 
            return current

numbers = [1 , 3 , 5]

result = max(numbers , len(numbers))
print(result)