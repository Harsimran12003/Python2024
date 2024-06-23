quote1 = "Be Exceptional\n"
quote2 = "Search the candle rather than cursing the darkness"

file = open("quotes.txt", "a")

file.write(quote1)
file.write(quote2)
print("Data written...")
file.close()