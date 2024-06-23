# Elevator Problem

floors = 10
floor = 0
floor_to_go = int(input("Enter floor to go: "))

while floor <= floors:
    print("At floor number " , floor)
    if floor_to_go == floor:
        print("You have reached at Floor Number: " , floor)
        break
    floor += 1

for floor in range(0, 11):
    print("At Floor Number:", floor)

    if floor_to_go == floor:
        print("You have Reached at Floor Number:", floor)
        break