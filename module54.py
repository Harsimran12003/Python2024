
class Order:
    def __init__(self, id=0, dishes=None, customer=None , total=0):
        self.id = id
        self.dishes = dishes
        self.customer = customer
        self.total = total
        
    def show(self):
        print("\n~~~~~~~~~~~~~~~~~~~~ORDER~~~~~~~~~~~~~~~~~~~~")
        print("ID: {} | Total: {} ".format(self.id, self.total))

        print("Order placed by:")
        self.customer.show()

        print("~~~~~~~~~~~~~~~~Order Dishes~~~~~~~~~~~~~~~~")
        for dish in self.dishes:
            dish.show()

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
    def link_customer(self , customer):
        self.customer = customer

    def link_dishes(self , dishes):
        self.dishes = dishes

        for dish in dishes:
            self.total += dish.price