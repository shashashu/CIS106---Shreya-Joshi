#input phase 
ppshare = float(input("Enter price per share"))
curstockprice = float(input("Enter current stock price"))
quantstock = float(input("Enter the quantity of stock"))

#process phase 
valueofstock = (curstockprice-ppshare) * quantstock

#output phase 
print("The value of your stock is ", valueofstock)