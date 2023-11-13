def salesrprt (sales):
  if sales > 100000.00:
    per = .10
  elif sales <= 100000.00:
    per = .05
  comm = sales * per
  nxtyr = sales * 1.05
  return comm,nxtyr

name = input("Enter sales person's name")
lname = input("Enter last name")
sales = float(input("Enter sales amount"))
comm , nxtyr = salesrprt(sales)
print("This is your commission amount: ",comm)
print("This is your next years report: ",nxtyr)
