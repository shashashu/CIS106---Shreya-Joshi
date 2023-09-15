#input phase 
fixedcosts = float(input("Enter the fixed cost of your item"))
pricepunit = float(input("Etner the price per unit"))
costpunit = float(input("Enter the cost per unit"))

#process phase 
breakeven = fixedcosts /( pricepunit-costpunit )

#output phase 
print("The break even point is ", breakeven)