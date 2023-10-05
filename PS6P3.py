counter = 0 

response = input("Want to calculate the average score of your two exams? Yes or No")

while response == "Yes": 
  counter = counter + 1 
  lname = input("Enter student last name")
  score1 = float(input("Enter exam 1 score"))
  score2 = float(input("Enter exam 2 score"))
  avg = (score1 + score2)/2 
  print (lname, " has an average of " , avg)
  response = input("Do you want to calculate another average? (Yes or No)")

print ("Number of students: " , counter)