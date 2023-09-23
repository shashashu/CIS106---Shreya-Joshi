appname = input("Enter the name of the appliance")
appcost = float(input("Enter the cost of your appliance"))

if appcost <= 1000: 
  warrcost = appcost * .1 
else: 
  warrcost = appcost * .05

total = appcost + warrcost

print("Appliance being bought today:            ",appname)
print("The base cost of your appliance is:       $",appcost)
print("The warrantee cost for your appliance is: $",warrcost)
print("The total cost for your appliance is:     $",total)