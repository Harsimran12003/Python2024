#Add to cart program
cart =[]
price = []
quantity = []
print("Welcome to Foodies")
print("~~~~~~~~~~~~~~~~~~~~~\n")

menu={
    "Pizza":350,
    "Burger":100,
    "Pasta":150,
    "Fries":200,
    "Noodles":250
}

print("Menu: " , menu)

while True:
    item = input("\nEnter food item to add in cart or 0 to quit: ")
    
    if item == "0":
     break

    qty = int(input("Enter the quantity for the item: "))

    quantity.append(qty)
    cart.append(item)
    price.append(menu[item] * qty)

print("Your cart: " , cart)
print("Prices: " , price)
print("Quantity: " , quantity)
print("-------------------------")
print("Total items: " , len(cart))
print("Total bill: " , sum(price))