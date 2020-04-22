def ground_shipping(weight):

    if (weight <= 2):
      price_per_pound = 1.50

    elif (weight <= 6):
      price_per_pound = 3.00

    elif (weight <= 10):
      price_per_pound = 4.00

    else:
      price_per_pound = 4.75
    return 20 + (price_per_pound * weight);

#test my function with 8.4 pounds
print(ground_shipping(8.4));

#Create a variable for the cost of premium ground shipping
premium_ground_shipping = 125.00

#Create a function for cost of drone
def cost_drone(weight):

    if (weight <= 2):
      price_per_pound = 4.50

    elif (weight <= 6):
      price_per_pound = 9.00

    elif (weight <= 10):
      price_per_pound = 12.00

    else:
      price_per_pound = 14.25
    return (price_per_pound * weight);
#test my function premium with 1.5 pounds
print(cost_drone(1.5))

#best option for a customer function
def best_option(weight):

  ground = ground_shipping(weight);
  premium = premium_ground_shipping;
  drone = cost_drone(weight);

  if ground < drone and ground < premium:

      method = "ground"
      cost = ground
  
  elif drone < ground and drone < premium:
  
      method = "drone"
      cost = drone
  else:

      method= "premium"
      cost = premium

print(
  "The cheapest option available is %.2f"
  " with %s shipping"
    % (cost, method)
)

best_option(4.8)


