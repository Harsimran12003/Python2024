from module44 import Driver # type: ignore
from module46 import Customer # type: ignore

class Ride:
    def __init__(self , customer=None, date="NA", time="NA", from_location="NA", 
                 to_location="NA", distance="2 km", fare=0, driver=None):
        self.customer = customer
        self.date = date
        self.time = time
        self.from_location = from_location
        self.to_location = to_location
        self.distance = distance
        self.fare = fare
        self.driver = driver
    
    def add_ride_details(self):

        print(">>>Enter ride details ")
        self.date = input("Enter Ride Date: ")
        self.time = input("Enter Ride Time: ")
        self.from_location = input("Enter the from location: ")
        self.to_location = input("Enter the to location: ")
        self.distance = input("Enter the distance: ")
        self.fare = int(input("Enter Ride Fare: "))
        print("-----------------------------------------")


    def link_customer(self, customer):
        self.customer = customer

    def link_driver(self, driver):
        self.driver = driver


    def show(self):
        self.customer.show()

        print("\n~~~~~~~~~~~~~~~~RIDE~~~~~~~~~~~~~~~~~~")
        print("Date: {} | Time: {} ".format(self.date , self.time))
        print("From: {} | To: {} ".format(self.from_location , self.to_location))
        print("Fare: {} | Distance: {}".format(self.fare,self.distance))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        self.driver.show()