# Promo code: ZOMATO
# Condition1: more than 249
# Condition2: 50% Off upto 150

amount = float(input("Enter amount: "))
promo_code = input("Enter promo code: ")


if promo_code == "ZOMATO":
    print("Promo code exists")

    if amount > 249:
        print("Promo code ZOMATO applied")
        discount = 0.50 * amount

        if discount >= 150:
            discount = 150

        amount -= discount
        print("Discount: " , discount)
        print("Amount to pay: " , amount)
    else:
        print("Amount is less")

else: 
    print("Promo code does not exist")
