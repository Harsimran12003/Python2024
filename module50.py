name = input("Enter Customer Name: ")
phone = input("Enter Customer Phone: ")
email = input("Enter Customer Email: ")

customer_details = "{},{},{}".format(name,phone,email)

file = open("customer.csv" , "a")
file.write(customer_details)
print("Data saved...")
file.close()