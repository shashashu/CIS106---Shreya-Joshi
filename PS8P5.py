def CompTuitOwed(hours, code):
  if code == "O":
    pph = 550
  elif code == "I":
    pph = 250
    
  tuitowed = hours * pph
  
  return tuitowed 

ttltuit = 0
r = input("Do you want to compute total tuition cost? Yes or No")

while r == "Yes":
  lname = input("Enter student last name")
  hours = float(input("Enter credit hours taken"))
  code = input("Enter the district code the student is from")
  tuitowed = CompTuitOwed(hours, code)
  ttltuit = ttltuit + tuitowed
  print(lname, "'s total tuition cost is: ", tuitowed)
  r = input("Do you want to compute total tuition cost? Yes or No")

print("Total of all tuition owed: ", ttltuit)