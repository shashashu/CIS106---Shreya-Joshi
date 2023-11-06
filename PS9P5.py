def CompValue(county,mrktvalue):
  vprcnt = county 

  if county == "Cook":
    vprcnt = .90
  elif county == "Cupage":
    vprcnt = .8
  elif county == "McHenry":
    vprcnt = .75
  elif county == "Kane":
    vprcnt = .6
  else:
    vprcnt = .7

  realvalue = vprcnt * mrktvalue

  return realvalue

ttlmrketvalue = 0
ttlrealvalue = 0 
r = input("DO you want to run this program? Yes or No")

while r == "Yes":
  county = input("Enter the county you currently reside in")
  mrktvalue = float(input("Enter the current market value of your home"))
  realvalue = CompValue(county,mrktvalue)
  print("This is the real value of your home on the market right now: ",realvalue)
  ttlrealvalue = ttlrealvalue + realvalue
  ttlmrketvalue = ttlmrketvalue + mrktvalue
  r = input("DO you want to run this program again Yes or No")

print("Total sum of all market values: ", ttlmrketvalue)
print("Total sum of actual value on the market: ", ttlrealvalue)