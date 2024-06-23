class Customer:
    def __init__(self, name="NA", phone="NA", email="NA", address="NA",gender="NA", age=0):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.gender = gender
        self.age = age
        
    def add_customer_details(self):
        print(">>>Enter customer details ")
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")
        self.address = input("Enter Customer Address: ")
        self.gender = input("Enter Customer Gender: ")
        self.age = int(input("Enter Customer Age: "))
        print("-----------------------------------------")
        
    def show(self):
        print("\n~~~~~~~~~~~~~~~~CUSTOMER~~~~~~~~~~~~~~~~~~")
        print("Name: {} | Phone: {} | Email: {}".format(self.name , self.phone, self.email))
        print("Address: {} ".format(self.address))
        print("Gender: {} | Age: {} ".format(self.gender , self.age))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def to_csv(self):
        data = "{},{},{},{},{},{}\n".format(self.name,self.phone,self.email,self.address,self.gender,self.age)
        return data


"""customer = Customer()
customer.add_customer_details()
customer.show()
"""