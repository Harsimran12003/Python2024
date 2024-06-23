
class Customer:
    def __init__(self, name="NA", phone="NA", email="NA", address="NA"):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        

    def show(self):
        print("\n~~~~~~~~~~~~~~~~~~~~CUSTOMER~~~~~~~~~~~~~~~~~~~~")
        print("Name: {} | Phone: {} | Email: {}".format(self.name, self.phone, self.email))
        print("Address: {} ".format(self.address))
              
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

