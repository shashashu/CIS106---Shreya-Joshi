def displayarrays(lname, scores):
  for i in range(0,10):
    print(lname[i], "scored a", scores[i])

  
def rdisplay(lname,scores):
  for i in range (9, -1,-1):
    print(lname[i], "has scored a",scores[i])

def sdisplay(scores):
  for i in range (0,10):
    print(scores[i])



lname = ["Parker", "Kim", "Raj", "Ae", "Smith","Mon","Adams", "Rana","Nakamura","Jongin"]
scores = [100, 92, 93, 82, 72, 78, 89, 94, 100, 99]

displayarrays(lname, scores)
print("REVERSE")
rdisplay(lname,scores)
print("SCORES ONLY")
sdisplay(scores)