# Condition1 : You can apply promo code iff min amount is 500

promo_code = "GET200"
amount = float(input("Enter your amount: "))

min_amount = 500

#Conditional Construct: If/else

if amount > min_amount :
    print("You can apply promo code", promo_code)
    amount -= 200
    print("Promo code appliedd succesfully. Please Pay: " , amount)
else :
    print("You cannot apply promo code" , promo_code)
    print("Add items worth" , (min_amount - amount), "more")