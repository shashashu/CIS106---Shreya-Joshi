
#define the object 
class Employee:
  # leave empty rn 
  def __init__(self,first,last,pay):
    self.first = first 
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'
    # self.rate = 0.00

  def bonus(self,rate):
    b = float(rate)*float(self.pay)
    return b 

class Manager(Employee):
  def termbonus(self,rate):
    tb = float(rate)*float(self.pay)
    return tb
#main - execution
# instantiante the object 
empl1 = Employee('Eddie', 'Brock',60000.00)
empM = Manager('Peter', 'Parker', 80000.00)

#use object 
#object syntax is object.method
print(empl1.email)
print(empl1.first)
print(empl1.last)
print(empl1.pay)
print(empl1.bonus(.10))
print(empl1.bonus(.20))
print(empM.email)
print(empM.first)
print(empM.last)
print(empM.pay)
print(empM.bonus( .40))