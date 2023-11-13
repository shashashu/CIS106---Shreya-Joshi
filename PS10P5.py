total = 0.0 
tax = 0.0
def compttl(qty,price):
  global total
  total = qty * price
  global tax
  tax = total * 0.07
  return

qty = float(input("Enter the item amount"))
price = float(input("Enter the price of each item"))
compttl(qty,price)
print("your total is: $", format(float(total), '10,.2f'))
print("Your tax cost is:", format(float(tax), '10,.2f'))
