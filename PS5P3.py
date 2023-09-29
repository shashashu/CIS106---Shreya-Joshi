
prin = float(input("Enter the Principle amount"))
years = int(input("Enter the years to maturity"))

if prin > 100000 and years == 5:
  rate = .06
elif prin >= 50000 and years == 10:
  rate = .05 
elif prin >= 50000 and years == 5: 
  rate = .04 
else: 
  rate = .02

firstyear = prin * rate 

print("Your principle is: " ,prin)
print("Your interest rate is: ", rate)
print("Your interest amount for the first year is: " ,firstyear)
