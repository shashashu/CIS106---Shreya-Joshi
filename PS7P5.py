f = open("data1.txt" , "r")

c = 0 
tottui = 0.0

#get first part of the data

lname = str(f.readline().rstrip('\n'))

while lname != "": #detect end of file
  dcode = str(f.readline().rstrip('\n'))
  credits = float(f.readline())

  if dcode == "I":
    costpercredit = 250.00
  else:
    costpercredit = 500.00

  tution = costpercredit * credits
  c = c + 1 
  tottui = tottui + tution

  print("Student: " ,lname)
  print("Credits Taken: " , credits)
  print("Tuition Owed" , tution)
  print(" ")
  
  lname = str(f.readline().rstrip('\n'))

f.close()

print("Number of students " , c)
print("Total Tuition Owed " , tottui)
