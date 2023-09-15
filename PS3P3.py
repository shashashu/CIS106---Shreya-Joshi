#input phase 

mealtotal =float(input("Enter the price of your meal"))

#process phase 
fifttip = mealtotal * .15 
totalwtip15 = mealtotal + fifttip
eighttip = mealtotal * .18 
totalwtip18 = mealtotal + eighttip
twenttip = mealtotal * .2
totalwtip20 = mealtotal + twenttip

#output phase 
print("With 15% tip:")
print()
print("Total: " , mealtotal)
print("Tip: ", fifttip)
print("Total with tip: ", totalwtip15)
print()
print("With 18% tip:")
print()
print("Total: ", mealtotal)
print("Tip: ", eighttip)
print("Total with tip:", totalwtip18)
print()
print("With 20% tip")
print()
print("Total: ", mealtotal)
print("Tip: ", twenttip)
print("Total with tip: ", totalwtip20)