qty = float(input("Enter the quantity of tickets bought"))

if qty >= 25: 
  ppticket = 50
elif qty >= 10: 
  ppticket = 60 
elif qty >= 5: 
  ppticket = 70
else: 
  ppticket = 75

total = qty * ppticket 

print("The number of tickets you purchased is: " ,qty)
print("THe price per ticket is: ", ppticket)
print("Your total is: $", total)