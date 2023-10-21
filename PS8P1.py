def CompExtPrice(qty, price):
  extprice = qty * price

  if extprice > 10000:
    discamnt = extprice * .10
  else:
    discamnt = 0.0

  newextprice = extprice - discamnt

  return newextprice

ttlextprice = 0.0 
r = input("Do you want to compute extended price?")

while r == "y":
  qty = float(input("Enter quantity: "))
  price = float(input("Enter quantity price"))
  extprice = CompExtPrice(qty, price)
  ttlextprice = ttlextprice + extprice
  print("Extended price is: " , extprice)
  r = input("Do you want to compute extended price?")

print("Total Extended Price is: $" , ttlextprice)