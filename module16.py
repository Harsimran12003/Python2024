# Q1. The following list [78, 82, 90, 85] represents the scores of four students in a math test. 
# Find the average score.

scores = [78 , 82, 90 , 85]
average = sum(scores) / len(scores)
print("Average is :" , average)


# Q2.  You deposit $5,000 in a savings account with an annual interest rate of 3% for 2 years. 
# How much simple interest will you earn on your investment? 
principal = 5000
rate = 3
time = 2
simple_interest = (principal * rate * time) / 100
print("Simple interest: " , simple_interest)


# Q3. A man can do a work in 20 days and a woman in 15 days. 
# If they work on it together for 5 days, then the fraction of the work that is left is ?
man_work = 20
woman_work = 15
man_work_one_day = 1/20
woman_work_one_day = 1/15

total_one_day_work = man_work_one_day + woman_work_one_day
five_day_work = total_one_day_work * 5

fraction = 1 - five_day_work
print("Fraction of work left: " , fraction)


# Q4. A circular table has a radius of 3 cm. What is the area of the table top?
radius = 3
area = 3.14 * radius * radius
print("Area of circle: " , area)


# Q5. The cost price of a book is $10. 
# You want to make a 15% profit on each book. At what price should you sell the book? 
cost_price = 10
profit = 0.15 * cost_price
selling_price = cost_price + profit
print("Selling Price: " , selling_price)