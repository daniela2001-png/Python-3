hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
total_price = sum(prices)
print("ADD PRICES:\n" + str(total_price))
print('-----------------------------------')
average_price = total_price / len(prices)
print("AVERAGE HAIRCUT PRICE:\n" +'$' +str(average_price))
print('-----------------------------------')
new_prices = [x - 5 for x in prices]
print("LOW PRICES:\n" + str(new_prices))
print('-----------------------------------')
total_revenue = 0
for i in range(0, (len(hairstyles))):
  total_revenue += prices[i] * last_week[i]
  print("TOTAL RENUEVE: " + str(total_revenue))
# Find the average daily revenue:
average_daily_revenue = total_revenue / 7
print('-----------------------------------')
print("LAST RENUEVE: {:}".format(average_daily_revenue))
# haircuts that are under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles[i])) if new_prices[i] < 30]
print('-----------------------------------')
print("HAIRCUTS UNDER 30 DOLLARS:\n" + str(cuts_under_30))
