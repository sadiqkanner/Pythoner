'''
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
e=[]
for i in range(5):
    xx = input("Enter Name")
    e= e+[xx]
    
my_used_car = Car(str(e), 'outback', 2013)
   
   
print(my_used_car.get_descriptive_name())
'''



class Toyes():
    """A simple attempt to represent a toye."""
    def __init__(self, toye_name, toye_price, toye_qty):
        """Initialize attributes to describe a Toye."""
        self.toye_name = toye_name
        self.toye_price = toye_price
        self.toye_qty = toye_qty
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.toye_name) + ' ' + self.toye_price + ' ' + self.toye_qty
        print(long_name.title," LONG ")
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


e=[]
for i in range(5):
    xx = input("Enter Name")
    e= e+[xx]
    
my_used_car = Car(str(e), 'outback', 2013)
   
   
print(my_used_car.get_descriptive_name())