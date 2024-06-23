product_prices = [1200, 500, 7650, 800, 3500, 1700]
salaries = [35000, 61500, 1800, 13500, 21700]
team_points = [12, 8, 4, 10, 2]

# Goal : find maximum out of these three


max = product_prices[0]
for idx in range( 1 , len(product_prices)):
    
    if product_prices[idx] > max:
        max = product_prices[idx]
print("Maximum value: " , max)
        

max = salaries[0]
for idx in range( 1 , len(salaries)):
    if salaries[idx] > max:
        max = salaries[idx]

print("Maximum value: " , max)
        

max = team_points[0]
for idx in range( 1 , len(team_points)):
    if team_points[idx] > max:
        max = team_points[idx]

print("Maximum value: " , max)
        
