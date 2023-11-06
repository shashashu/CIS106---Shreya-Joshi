def CompFrCast(month,sales):
  Prcnt = month 

  if month in ["Jan", "Feb", "Mar"]:
    Prcnt = .10
  elif month in ["Apr","May","June"]:
    Prcnt = .15
  elif month in ["Jul","Aug","Sep"]:
    Prcnt = .2
  elif month in ["Oct","Nov","Dec"]:
    Prcnt = .25

  nextmonth = sales * (1 + Prcnt)

  return nextmonth

r = input("DO you want to do this program Yes or No")

while r == "Yes":
  lname =input("Enter your last name")
  month =input("Enter the current month")
  sales =float(input("Enter the number of sales made"))
  nextmonth = CompFrCast(month,sales)
  print("The sales for next month are predicted to be:" ,nextmonth)
  r = input("Do you want to do this program again? Yes or No")