
qty = float(input("Enter the quantity to purchase"))

if qty > 10000:
  price = 10.00
elif qty >= 5000: 
  price = 20.00
else:
  price = 30.00

extprice = qty * price 
tax = extprice * .07
total = extprice + tax 

print("Your extended price is: ",extprice)
print("Your tax amount is:     ",tax)
print("Your total is:          ", total)