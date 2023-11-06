def Compsqrft(L,W,H):
  sqrft = 2 * L * W + 2 * L * H + 2 * W * H

  return sqrft

r = input("Do you want to run this program? Yes or No")

while r == "Yes":
  L = float(input("Enter the length of the room"))
  W = float(input("Enter the width of the room"))
  H = float(input("Enter the height of the room"))
  sqrft = Compsqrft(L,W,H)
  paint = sqrft / 50
  print("The gallons of paint needed to pain entire room:" , paint)
  r = input("Do you ant to run this program again? Yes or No")