from module43 import Vehicle  # type: ignore

class Driver:
    def __init__(self, name="NA",phone="NA",email="NA",license_number="NA",rating=2.5,age=0,gender="NA",
                 vehicle=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.license_number = license_number
        self.rating = rating
        self.age = age
        self.gender = gender
        self.vehicle = vehicle

    def add_driver_details(self):
        print(">>>Enter driver details ")
        self.name = input("Enter Driver Name: ")
        self.phone = input("Enter Driver Phone: ")
        self.email = input("Enter Driver Email: ")
        self.license_number = input("Enter Driver Licence Number: ")
        self.rating = float(input("Enter Driver Rating: "))
        self.age = int(input("Enter Driver Age: "))
        self.gender = input("Enter Driver Gender: ")
        print("-----------------------------------------")

        # 1 to 1 mapping
        self.vehicle = Vehicle()
        self.vehicle.add_vehicle_details()

    def show(self):
        print("\n~~~~~~~~~~~~~~~~DRIVER~~~~~~~~~~~~~~~~~~")
        print("Name: {} | Phone: {} | Email: {}".format(self.name , self.phone, self.email))
        print("License Number: {} | Rating: {} ".format(self.license_number , self.rating))
        print("Age: {} | Gender: {} ".format(self.age , self.gender))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.vehicle.show()
        

"""
driver = Driver()
driver.add_driver_details()
driver.show()
"""