def CompBatAvg(hits, bats):
  batavg = hits / bats

  return batavg 

count = 0.0
r = input("Do you want to compute batting average? Yes or No")

while r == "Yes":
  lname = input("Enter player's last name")
  hits = float(input("Enter the number of hits"))
  bats = float(input("Enter the number of bats"))
  batavg = CompBatAvg(hits, bats)
  print(lname, " has a batting average of: ", batavg)
  count = count + 1
  r = input("Do you want to compute batting average again? Yes or No")

print("Number of players entered: ", count)