qty = float (input("Enter quantity amount"))

if qty >= 1000.00:
  up = 3.00
else:
  up = 5.00

extprice = qty * up
tax = extprice *.07 
total = extprice + tax

print("Quantity Ordered ", qty)
print("Unit price:     $", up)
print("Extended Price: $", extprice)
print("Tax amount:     $", tax)
print("Total order:    $", total)