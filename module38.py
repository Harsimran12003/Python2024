from module37 import Dish   # type: ignore

class Menu:
     def __init__(self, name="NA" , number_of_dishes=0, dishes=[]):
          self.name = name
          self.number_of_dishes = number_of_dishes
          self.dishes = dishes
          

     def show(self):
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          print("Menu : {} | {}" .format(self.name , self.number_of_dishes))
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

          print("Dishes: ")
          for idx in range(0 ,len(self.dishes)):
               self.dishes[idx].show()

"""dishes = [
          Dish("Noodles" , 250, 4.2), 
          Dish(name="Pasta" , price=200, rating=4.5)]

menu = Menu( 
            name = "Italian Delight" , 
            number_of_dishes = len(dishes), 
            dishes = dishes )

menu.show()
"""