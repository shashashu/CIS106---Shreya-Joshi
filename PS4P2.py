item = input("Enter item name")
qty = float(input("Enter quantity amount"))

if item == "A": 
  up = 10.00
else:
  up = 20.00

extprice = qty * up 

print("The item inputed was: ",item)
print("The unit price of the item was: $", up)
print("Your extended price is: $", extprice)