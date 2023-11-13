def examavg (exam1,exam2,exam3):
  sum = exam1 + exam2 + exam3
  total = 300
  percent = (sum / total) * 100
  avg = (sum/3)
  points = exam1 + exam2 + exam3

  return avg,points

lname = input("Enter student's last name")
exam1 = float(input("Enter the score for exam 1"))
exam2 = float(input("Enter the score for exam 2"))
exam3 = float(input("Enter the score for exam 3"))

avg,points = examavg(exam1,exam2,exam3)
print("Student Last Name:", lname)
print("Your exam average:", avg)
print("Your point total is: ",points)