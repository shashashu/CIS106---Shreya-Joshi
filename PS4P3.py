booknum = float(input("Enter number of books bought"))
bookcost = float(input("Enter the price of each book"))

ordertotal = booknum * bookcost

if ordertotal <= 50: 
  shipcost = 25.00
else: 
  shipcost = 0 

fullorderttl = ordertotal + shipcost

print("Your order total is:       $", ordertotal)
print("Your shipping cost is:     $", shipcost)
print("Total cost of whole order: $", fullorderttl)