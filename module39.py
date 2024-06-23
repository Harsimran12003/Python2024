from module38 import Menu # type: ignore
from module37 import Dish # type: ignore

class Restaurant:

    def __init__(self, name="NA", phone="NA", email="NA", address="NA", operating_hours="10.00 am to 11.00pm",
                  ratings=2.5, menu=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.operating_hours = operating_hours
        self.ratings = ratings
        self.menu = menu

    def show(self):
        print("****************************************************************")
        print("RESTAURANT - {}\n".format(self.name))
        print("\u260E  {} | \u2709  {}".format(self.phone , self.email))
        print("\u27DF  {} |  {} | {} \u2B50".format(self.address, self.operating_hours, self.ratings) )
        print("*****************************************************************\n")
        self.menu.show()


dishes = [
          Dish("Noodles" , 250, 4.2), 
          Dish(name="Pasta" , price=200, rating=4.5)]


Restaurant(name = "The Temptations", 
                        phone = "+91 5642133547" , 
                        email = "temptations@xyz.com",
                        address = "562 Royal Avenue , Bangalore",
                        operating_hours = "10.00 am to 10.30 pm ",
                        ratings = 4.3,
                        menu = Menu( 
                                name = "Italian Delight" , 
                                number_of_dishes = len(dishes), 
                                dishes = [
                                           Dish("Cheese Pizza" , 250, 4.2), 
                                           Dish(name = "Pasta" , price = 200, rating = 4.5),
                                           Dish("Veggie Pizza" , 350, 4.4)
                                         ]
                                   )
).show()
    