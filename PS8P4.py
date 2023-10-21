def CompPayRate(jobcode):
  payrate = jobcode

  if jobcode == "L":
    payrate = 25
  elif jobcode == "A":
    payrate = 30
  elif jobcode == "J":
    payrate = 50

  return payrate 

ttlgrosspay = 0
r = input("Do you want to compute gross pay? Yes or No")

while r == "Yes":
  lname = input("Enter employee last name")
  jobcode = input("Enter Jobcode")
  hours = float(input("Enter hours worked"))
  payrate = CompPayRate(jobcode)
  if hours > 40:
    grosspay = (hours * payrate) * 1.5
  else:
    grosspay = hours * payrate
    
  ttlgrosspay = ttlgrosspay + grosspay
  print(lname, "gross pay is: ",grosspay)
  r = input("Do you want to compute gross pay? Yes or No")

print("Total of all gross pay: ", ttlgrosspay)

  