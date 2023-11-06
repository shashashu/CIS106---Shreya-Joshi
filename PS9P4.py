def CompTrain(milesfromchi):
  ticket = milesfromchi

  if milesfromchi >= 30:
    ticket = 12
  elif milesfromchi >= 20:
    ticket = 10
  elif milesfromchi >= 10:
    ticket = 8
  else:
    ticket = 5

  return ticket

totaltickets = 0 
r = input("Do you want to run this program? Yes or No")

while r == "Yes":
  lname = input("Enter last name")
  milesfromchi = float(input("Enter how many miles from downtown Chicago you are"))
  ticket = CompTrain(milesfromchi)
  print(lname, "The price of your ticket to Chicago is: ",ticket)
  totaltickets = totaltickets + ticket
  r = input("Do you want to run this program again? Yes or No")

print("Total sum price of all tickets: ",totaltickets)