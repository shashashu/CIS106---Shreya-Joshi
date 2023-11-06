def CompDoor(make,model,msrp):
  prcentoff = make

  if make == "Honda Accord":
    prcentoff = .10
  elif make == "Toyota Rav4":
    prcentoff = .15
  elif make == "Electric":
    prcentoff = .30
  else:
    prcentoff = .05

  discount = msrp * prcentoff
  newmsrp = msrp - discount
  tax = newmsrp * .07
  total = newmsrp + tax
  sumofall = msrp - discount + tax

  return total

ttlmsrps = 0
r = input("Do you want to do this program? Yes or No")

while r == "Yes":
  make = input("Enter make of the car")
  model = input("Enter model of the car")
  msrp = float(input("Enter the msrp of the car"))
  total = CompDoor(make,model,msrp)
  print("The total of your",make, model, "car is", total)
  r = input("Do you want to run this program again? Yes or No")
  ttlmsrps = ttlmsrps + total
  
print("The sum of all the sale prices of MSRPS is: ",ttlmsrps)