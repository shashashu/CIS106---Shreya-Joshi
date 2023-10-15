# count from 1 to 10 by 1's 
# start value 
# stop vlaue 
# increment value 

response = input("Do you want to calculate interest (Yes or No)")

while response == "Yes":
  p = float(input("Enter Principle"))
  r= float(input("Enter interest rate"))
  
  totint = 0.0
  
  print("Year", " Beg Bal  ", "  End Bal  ")
  for count in range (1,6, 1):
    i = p * r
    totint = totint + i
    eb = p + i
    print(count,  "  ", p,"   ", eb)
    p = eb
    
  response = input("Do you want to calculate interest again (Yes or No)")

print("total interest earned" , totint)