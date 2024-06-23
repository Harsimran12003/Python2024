"""
ZOMATO: 20% OFF
      : min value: 300
BINGO : 50% off
      : min value 500
      : max discount : 100
"""

promo_code = input("Enter Promo code: ")
amount = float(input("Enter amount: "))

if promo_code == "ZOMATO":
    print("ZOMATO exists")
    if amount > 300:
        discount = 0.20 * amount
        print("You can pay \u20b9" , (amount-discount))
    else:
        print("Amount is less. Please add items worth " , (300-amount), "more.")

elif promo_code == "BINGO":
    print("BINGO exists")
    if amount > 500:
        discount = 0.50 * amount
        if discount > 100:
            discount = 100
            amount -= discount
            amount = amount + 0.18*amount
            amount += 18.5  #delivery fee
            print("You can pay \u20b9" ,(amount))

    else:
        print("Amount is less. Please add items worth " , (500-amount), "more.")
        
else:
    print("Promo code invalid")