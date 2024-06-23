"""
    Code 3 Objects
    1. Dish : name, price, rating
    2. Menu : name, number_of_dishes, dishes 
        1 Menu can have many Dishes (1 to many)
    3. Restaurant : name, phone, email, address, operating_hours, ratings, menu
        1 Restaurant can have 1 Menu (1 to 1)

"""
# Class for the Object Dish

class Dish:

     def __init__(self, name="NA", price=0, rating=0):
          self.name = name
          self.price = price
          self.rating = rating

     def show(self):
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          print("Dish : {} | \u20B9 {} | {} \u2B50" .format(self.name , self.price, self.rating))
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
          
          
#dish1 = Dish()
#dish2 = Dish("Noodles" , 250, 4.2)
#dish3 = Dish("Pasta" , 200, 4.5)

#dish1.show()
#dish2.show()
#dish3.show()


# List of dishes
"""
dishes = [Dish() , 
          Dish("Noodles" , 250, 4.2), 
          Dish("Pasta" , 200, 4.5)]


for idx in range(0 , len(dishes)):
     dishes[idx].show()
"""