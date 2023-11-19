def displayplayers(ln, batavg):
  for i in range (0,10,1):
    print(ln[i], "has a batting average of: ", batavg[i])

def searchname(ln, batavg, plname):
  foundsub = -1
  for i in range(0,10,1):
    if ln[i] == plname:
      foundsub = i

  if foundsub != -1:
    print(ln[foundsub], "has a batting average of: ", batavg[foundsub])

f = open("info.txt","r")
lname = f.readline()

ln = []
batavg = []
while lname != "":
  ln.append(str(lname).rstrip("\n"))
  a = float(f.readline())
  batavg.append(a)
  lname = f.readline()
f.close
displayplayers(ln,batavg)

r = input("Do you want to search for a player? Yes or No")
while r == "Yes":
  plname = input("Enter the name you want to search for")
  searchname(ln, batavg, plname)
  r = input("Do you want to search for a player? Yes or No")