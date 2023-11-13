def b_average (score1, score2, score3, handi):
  sum = score1 + score2 + score3
  avg = sum / 3
  havavg = (sum + handi) / 3
  return avg, havavg

lname = input("Enter bowler's last name")
score1 = float(input("Enter 1st score"))
score2 = float(input("Enter your 2nd score"))
score3 = float(input("Enter your 3rd score"))
handi = float(input("Enter your handicap"))
avg,havavg = b_average(score1,score2,score3,handi)
print("Bowler: " ,lname)
print("Your score average is: ",format(float(avg),'10,.2f'))
print("Your handicap: ",format(float(havavg),'10,.2f'))