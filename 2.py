#CREATE
promo_code1= "ZOMATO40"
print(promo_code1, id(promo_code1), type(promo_code1))

#REFERENCE COPY OPERATION
promo_code2 = promo_code1
print(promo_code2, id(promo_code2), type(promo_code2))

#DELETE
del promo_code1
print(promo_code2, id(promo_code2), type(promo_code2))

#promo_code1 is deleted only
