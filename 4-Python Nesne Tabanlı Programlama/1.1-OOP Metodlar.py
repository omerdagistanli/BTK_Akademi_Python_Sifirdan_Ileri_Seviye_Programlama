# class OOP

# class Person():
#
#     # class attributes (özellik)
#     address = "no information"
#
#     # constructor (yapıcı metod)
#     def __init__(self, name, year):
#         # object attributes
#         self.name = name
#         self.year = year
#
#     # methods
#     def hello(self):
#         print("Hello, I am", self.name)
#
#     # instance method
#     def calculateAge(self):
#         return 2020 - self.year
#
# # object (instance)
#
# p1 = Person("ali", 20)
# p2 = Person("ömer", 25)
#
# print("You was borned at", p1.calculateAge())
# print("You was borned at", p2.calculateAge())

class circle():
    pi = 3.14

    def __init__(self,yaricap = 1):
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2 * self.yaricap * self.pi

    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)

c1 = circle()     # yarıcap = 1
c2 = circle(5)

print("Çevre:",c1.cevre_hesapla(),"Alan:",c1.alan_hesapla())
print("Çevre:",c2.cevre_hesapla(),"Alan:",c2.alan_hesapla())