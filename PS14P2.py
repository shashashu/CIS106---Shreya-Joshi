class car:
  def __init__(self,make,model,stickerp): 
    self.make = make
    self.model = model
    self.stickerp = stickerp

  def discountp(self, discamnt):
    d = float(discamnt) * float(self.stickerp)
    return d 

class sport(car):
  options = {'SportWheels' : 1000.00, 'SportEngine' : 3000.00, 'SportInterior' : 2000.00}

  def add_option(self, include_option):
    pricewithoptions = float(self.stickerp)
    for option, include in zip(self.options, include_option):
      if include == 'Y':
        pricewithoptions += self.options[option]
    self.pricewithoptions = pricewithoptions

car1 = car('Honda', 'Hybrid', 40000.00)
car2 = sport('Porsche', 'Cayman', 104000.00)

include_option1 = ('Y', 'N', 'N')
include_option2 = ('N', 'Y', 'N')
include_option3 = ('N', 'N', 'Y')

print(car1.make)
print(car1.model)
print(car1.stickerp)
print(car1.discountp(.90))
print(car2.make)
print(car2.model)
print(car2.stickerp)

car2.add_option(include_option1)
print(car2.pricewithoptions)

car2.add_option(include_option2)
print(car2.pricewithoptions)

car2.add_option(include_option3)
print(car2.pricewithoptions)