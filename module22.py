product_prices = [1200, 500, 7650, 800, 3500, 1700]

def find_max(data):
    max = data[0]
    for idx in range(1 , len(data)):
        if data[idx] > max:
            max = data[idx]
    print("Max is : " , max)


find_max(product_prices)