def displaynames(ln ,scores):
  for i in range (0,10,1):
    print(ln[i], "has a score of ", scores[i])
    
def hilow (lname, scores):
  hi_var = 0.0
  hiscore = 0
  low_var = 9999
  lowscore = 0

  for i in range (0,10,1): 
    if (scores[i]) > hi_var:
      hi_var = scores[i]
      hiscore = i
    elif scores[i] < low_var:
      low_var = scores[i]
      lowscore = i

  print (lname[hiscore], " has the highest score of: ",scores[hiscore])
  print (lname[lowscore], "has the lowest score of: ",scores[lowscore])

f = open("info.txt","r")

lname = f.readline()

ln = []
scores = []
while lname != "":
  ln.append(str(lname).rstrip("\n"))
  a = float(f.readline())
  scores.append(a)
  lname = f.readline()
f.close
displaynames(ln ,scores)
print("HIGHEST AND LOWEST")
hilow(ln, scores)