"""
 I have HDFC Bank Credit Card.
 HDFC Bank will charge 15% interest on outstanding amount
 Minimum, you should be able to pay 10% of outstanding amount else your credit score will be compromised.

 April 2024 -> 50,000 ---> input by user
    April 2024,  min ---> 5000
                 pending -> 45000
                         + 15% of 45,000 = 6750
 I can only pay max of 8000 per month -----> input by user

 Find in which month whole amount will become 0                         
 """



amount = int(input("Enter the amount you have spent: "))
             
print("You have to pay 10% of" , amount , "that is" , 0.10*amount , "first.")

amount = amount - (0.10 * amount)
interest = 0.15 * amount
amount += interest

print("\nOutstanding amount including 15% interest: " , amount)
          
min_amount = int(input("Enter the minimum amount you can pay per month: "))

month = 0
while amount > 0:
    
    amount -= min_amount
    if amount < 0: 
        amount = 0

    month += 1   
    print("Month", month, "Outstanding Amount = ", amount)


month_names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }


start_month = 4
end_month = start_month + month

start_year = 2024
if month > 8:
    start_year += 1
    end_month = end_month - 12

print("Your outstanding amount will become zero in :" , month_names[end_month], start_year)
    


