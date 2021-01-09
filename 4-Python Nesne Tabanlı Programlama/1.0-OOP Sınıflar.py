# class

class Person():
    # class attributes (özellik)
    address = "no information"

    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        # methods

# object (instance)

p1 = Person("ali", 20)
p2 = Person("ömer", 25)

print(p2.name,p1.name,"yi döver", p1.year, p2.year, p1.address, p2.address)