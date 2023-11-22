#PROBLEM 1 
def dl1 (mylist):
  n = int(input("Number of items in your list"))
  for n in range(0,n,1):
    s = int(input("Enter a number"))
    mylist.append(s)
  return mylist
def displaylist(mylist):
  for item in mylist:
    print(item)

mylist = []
mylist = dl1(mylist)
displaylist(mylist)
print(mylist) 
#PROBLEM 2 
mylist.insert(0,99)
print(mylist)
#PROBLM 3 
mylist[0]=100
print(mylist)
#PROBLEM4
mylist2 = ["500","600","700","800","900"]
mylist2.extend(mylist)
print(mylist2)
#PROBLEM5
mylist2.remove("800")
print(mylist2)
#PROBELM6
mylist.remove(3)
print(mylist)
#PROBLEM7
gradeslist = ["A", "B", "C", "A", "A", "C"]
print(gradeslist)
#PROBLEM8
print("Count of A's in grades list", gradeslist.count("A"))
#PROBLEM9
print("Index position of B in grade list: ",gradeslist.index("B"))
#PROBLEM10
if "F" in gradeslist:
  print("Count of F's in grades list", gradeslist.count("F"))
else:
  print("F is not in the list")
#PROBLEM11
list.clear(mylist2)
print(mylist2)
#PROBLEM12
del mylist2
#error pops up and cannot run rest of code but typed in print(print.mylist2) says DNE

#PROBLEM13
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
#PROBLEM14
players.sort()
print(players)
#PROBLEM15
players2 = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print(players2)
#PROBLEM16
players2.sort(reverse=True)
print(players2)