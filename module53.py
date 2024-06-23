"""
    Customer : name, phone, email, address, orders
    Dish : name, price, category, ratings
    Order : id, number_of_items, dishes, total_bill

    1 Customer can place many Orders
    1 Order can have many Dishes
    1 Order can have 1 Customer
"""

class Dish:
    def __init__(self, name="NA", price=0, ratings=2.5):
        self.name = name
        self.price = price
        self.ratings = ratings


    def show(self):
        print("\n~~~~~~~~~~~~~~~~~~~~DISH~~~~~~~~~~~~~~~~~~~~")
        print("Name: {} | Price: {} | Ratings: {}".format(self.name, self.price, self.ratings))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

"""
def bubble_sort(data):
    for i in range( 0 , len(data)):
        for j in range ( i+1 , len(data)):
            if data[i].ratings < data[j].ratings:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    

dishes = [Dish("Pizza" , "350", 4.2),
          Dish("Noodles" , "250", 4.4),
          Dish("Pasta" , "240", 4.0),
          Dish("Pizza" , "350", 4.2),
          Dish("Burger" , "100" , 4.5)]


for dish in dishes:
    dish.show()


bubble_sort(dishes)
print("\n>>> Sorting high to low ratings: ")
for dish in dishes:
    dish.show()
    """
      

    