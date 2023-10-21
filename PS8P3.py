def CompMPG(miles, gallons):
  mpg = miles / gallons

  return mpg 

count = 0 
r = input("Do you want to compute the mpg to your destination? Yes or No")

while r == "Yes":
  city = input("Enter the city travelled to")
  miles = float(input("Enter the miles travelled"))
  gallons = float(input("Enter the gallons used"))
  mpg = CompMPG(miles, gallons)
  count = count + 1
  print(miles, "miles travelled to drive to ", city)
  print("Estimated amount of miles per gallon ", mpg)
  r = input("Do you want to compute the mpg to another destination? Yes or No")

print("Total number of trips taken: ", count)
  