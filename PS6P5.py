sumofdisc = 0 
numborders = 0

response = input("Do you want to run this program Yes or No")

while response == "Yes":
  qty = float(input("Enter the quantity purchased"))
  price = float(input("Enter the price of the item"))
  extprice = qty * price
  if extprice > 1000:
    discamnt = extprice * .25
  else:
    discamnt = extprice * .10
  totalorder = extprice - discamnt
  sumofdisc = sumofdisc + discamnt
  numborders = numborders + 1 
  print("Extended price is $" ,extprice)
  print("Discount earned $" , discamnt)
  print("Your order total is" , totalorder)
  response = input("Do you want to run this program again Yes or No")

print("Total discounts given $", sumofdisc)
print("Number of orders ",numborders)
avgdisc = sumofdisc / numborders
print("Average discount per order $" , avgdisc)
  