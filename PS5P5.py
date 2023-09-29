
lname = input("Enter your last name")
salary = float(input("Enter your salary amount"))
joblevel = int(input("Enter your job level"))

if joblevel >= 10: 
  bonusrate = .25 
elif joblevel >= 5:
  bonusrate = .20
else: 
  bonusrate = .10

bonus = salary * bonusrate

print(lname, "your bonus amount is: " ,bonus)