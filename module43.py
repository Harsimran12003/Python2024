"""
driver -> name,phone,email,license_number,rating,age,gender,vehicle [1 to 1]
1 driver has 1 vehicle

vehicle -> reg_number, brand, model, color
customer -> name, phone, email, address,gender, age
ride -> customer, date, time, from_location, to_location, distance, fare, driver [1 to 1]

1 Ride has 1 Customer
1 Ride has 1 Driver
"""

class Vehicle:

    def __init__(self, reg_number="NA", brand="NA", model="NA", color="white"):
        self.reg_number = reg_number
        self.brand = brand
        self.model = model
        self.color = color

    def add_vehicle_details(self):
        print(">>> Enter vehicle details: ")
        self.reg_number = input("Enter Vehicle Registration Number: ")
        self.brand = input("Enter Vehicle Brand: ")
        self.model = input("Enter Vehicle Model: ")
        self.color = input("Enter Vehicle Color: ")
        print("-----------------------------------------")

    def show(self):
        print("\n~~~~~~~~~~~~~~~~VEHICLE~~~~~~~~~~~~~~~~~~")
        print("Reg Number: {} | Brand: {} ".format(self.reg_number , self.brand))
        print("Model: {} | Color: {} ".format(self.model , self.color))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


"""
vehicle = Vehicle()
vehicle.add_vehicle_details()
vehicle.show()
"""