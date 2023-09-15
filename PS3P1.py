#input phase 
exam1 = float(input("Enter Exam 1 score"))
exam2 = float(input("Enter Exam 2 score"))

#process phase 
exam1weight = exam1 * .60
exam2weight = exam2 * .40
totalscore = exam1weight + exam2weight

#output phase 
print("The total score of your two exams are ", totalscore)