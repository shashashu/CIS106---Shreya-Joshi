lname = input("Enter last name")
grinc = input("Enter Your Gross Income")
dpds = input("Enter number of dependents")

adjinc = float(grinc) - 12000.00 * float(dpds)

if adjinc > 50000.00:
  taxrate = adjinc * .20 
else: 
  taxrate = adjinc * .10

if taxrate < 0: 
  taxrate = 100.00

print("Gross Income:         $", grinc)
print("Number of Dependents:  ", dpds)
print("Adjusted Gross:       $", adjinc)
print("Income Tax:           $", taxrate)