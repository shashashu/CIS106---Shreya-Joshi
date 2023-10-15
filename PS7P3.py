f = open("data1.txt", "r")

totalb = 0.0

lname = str(f.readline().rstrip('\n'))

while lname != "":
  sal = float(f.readline())

  if sal >= 100000: 
    bonus = sal * .2
  elif sal >= 50000:
    bonus = sal * .15
  else:
    bonus = sal * .10

  print("Employee:     " ,lname)
  print("Salary:       " ,sal)
  print("Bonus Amount: ", bonus)
  print(" ")
  totalb = bonus + totalb

  lname = str(f.readline().rstrip('\n'))

f.close()

print("Total Amount of Bonuses Given Out: " , totalb)