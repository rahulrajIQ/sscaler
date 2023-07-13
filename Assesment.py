import copy

# Manufacturer class with the attributes and the method.
class Manufacturer:
    def __init__(self, name,location,brands=[]):
        self.name = name
        self.location = location
        self.brands = copy.deepcopy(brands)

    def add_brand(self, brand):
        self.brands.append(brand)
        

    def get_brands(self):
        print(self.brands)
        return self.brands

# Car class with the attributes and the method. The 'mf' is the corresponding manufacturer object.
class Car:
    def __init__(self, brand, model, year, mf):

        self.brand = brand
        self.model = model
        self.year = year
        self.mf= mf

    def get_details(self):
        print(self.brand, self.model, self.year)


# Two manufacturer objects
mf1 = Manufacturer('Tesla','Hawaii')
mf2 = Manufacturer('Ford','Goa')

# Adding brands to both the two manufacturer objects
mf1.add_brand('Tesla-X')
mf2.add_brand('McLaren')

# Two car objects

# belongs to the first manufacturer object
ca1=Car('Tesla-X', 'X-Series',1990, mf1)


# belongs to the second manufacturer object
ca2=Car('McLaren', 'Mac-Series',1991, mf2)

#Getting details of both the cars
ca1.get_details()
ca2.get_details()

# Veryfying with the manufacturers.
ca1.mf.get_brands()
ca2.mf.get_brands()

