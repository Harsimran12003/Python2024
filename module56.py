from module53 import Dish
from module54 import Order
from module55 import Customer


dish_menu = [Dish("Pizza" , 350, 4.2),
          Dish("Noodles" , 250, 4.4),
          Dish("Pasta" , 240, 4.0),
          Dish("Pizza" , 350, 4.2),
          Dish("Burger" , 100 , 4.5)]

customer1 = Customer(name="John", phone="+91 6541265301", email="john@xyz.com", address="564 green hill")
customer2 = Customer(name="Fionna", phone="+91 654856231", email="fionna@xyz.com", address="45 redwood shores")

#order1 = Order(id=78951, dishes= [dish_menu[3], dish_menu[1]], customer=customer2 , total=600)

order1 = Order(id = 56213)
order1.link_customer(customer=customer1)
order1.link_dishes(dishes=[dish_menu[2], dish_menu[4]])

order1.show()