def discount(qty,price,discrate):
  total = qty * price
  discamnt = discrate * total
  discprice = total - discamnt

  return discamnt, discprice

qty = float(input("Enter the quantity"))
price = float(input("Enter the price of each unit"))
disrate = float(input("Enter the discount percent"))
discamnt,discprice = discount(qty,price,disrate)

print("This is your quantity" ,qty)
print("The unit price: $" ,price)
print("This is your discounted amount: $", discamnt)
print("THis is your total discounted price: $" ,discprice)