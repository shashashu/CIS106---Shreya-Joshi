def displayarrays(lname):
  for i in range(0,10):
    print(lname[i])

  
def rdisplay(lname):
  for i in range (9, -1,-1):
    print(lname[i])



lname = ["Parker", "Kim", "Raj", "Ae", "Smith","Mon","Adams", "Rana","Nakamura","Jongin"]

displayarrays(lname)
print("REVERSE")
rdisplay(lname)