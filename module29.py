def square_of_numbers(nums):
    print("Num is : ", nums, id(nums))

    for idx in range( 0 , len(nums)):
        nums[idx] = nums[idx] * nums[idx]
        print("Num is : ", nums[idx])

# Functions exist in memory
# print("sqaure: " , square) # hashcode and name of function

numbers = [10,20,30,40,50]
print("A. number is : " , numbers)
square_of_numbers(numbers)
print("B. number is: ", numbers)
