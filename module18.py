#LINEAR SEARCH
instagram_user_names = ["john.j", "fionna", "harry_h", "leo.32", "ben_a"]
names = ["John Jackson", "Fionna Flynn", "Harrison", "Leonardo", "Bennethan"]

user_name = input("Enter user name to search: ")

#Below approach consumes too much time and memory

"""
idx = 0

if user_name == instagram_user_names[idx]:
    print("Name is: " , names[idx])
elif user_name == instagram_user_names[idx+1]:
    print("Name is: " , names[idx+1])
elif user_name == instagram_user_names[idx+2]:
    print("Name is: " , names[idx+2])
elif user_name == instagram_user_names[idx+3]:
    print("Name is: " , names[idx+3])
elif user_name == instagram_user_names[idx+4]:
    print("Name is: " , names[idx+4])
else:
    print("Cannot find user")
"""

"""
# WHILE LOOP
idx = 0
while idx < len(instagram_user_names):
    if user_name == instagram_user_names[idx]:
        print("Name is: " , names[idx])
        break
    idx += 1 
"""

flag = False

for idx in range(0, len(instagram_user_names)):  #idx will from 0 till 4 (len-1)
    if user_name == instagram_user_names[idx]:
        print("Name is: " , names[idx])
        flag = True
        break
    
if flag == False:
    print(user_name, "not found")
    
