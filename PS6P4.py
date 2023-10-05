counter = 0
sumgpay = 0.00

response = input("DO you want to do this program Yes or No")

while response == "Yes": 
  counter = counter + 1
  lname = input("Enter employee last name")
  payrate = float(input("Enter hourly payrate"))
  hours = float(input("Enter hours worked"))
  if hours > 40:
    gpay = (40 * payrate) + (hours-40)*1.5*payrate
  else:
    gpay = hours * payrate
  sumgpay = sumgpay + gpay 
  print(lname, " your gross pay is $" , gpay)
  response = input("Do you want to use this program again Yes or No")

avgpay = sumgpay/counter
print("Number of employees ",counter)
print("Total sum of gross pay ",sumgpay)
print("The average gross pay is $",avgpay)
