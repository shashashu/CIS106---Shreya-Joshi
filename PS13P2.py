
#define the object 
class Student:
  def __init__(self,first,last,district, credits): 
    self.first = first
    self.last= last
    self.district = district
    self.credits = credits
    # self.tuit = 0.00

  def tuit(self,district):
    if district == "I":
      tuit = float(self.credits) * 250
    else:
      tuit = float(self.credits) * 500
    return tuit

stu_1 = Student('Lyn', 'Jongin', 'I', 18)
stu_2 = Student('Zayn', 'Sango', 'O', 15)

print(stu_1.tuit(stu_1.district))
print(stu_1.first)
print(stu_1.last)
print(stu_1.credits)
print(stu_1.district)
print("")
print(stu_2.tuit(stu_2.district))
print(stu_2.first)
print(stu_2.last)
print(stu_2.credits)
print(stu_2.district)