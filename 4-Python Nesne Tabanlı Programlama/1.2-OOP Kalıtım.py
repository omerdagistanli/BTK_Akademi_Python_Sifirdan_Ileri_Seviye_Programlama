 # Inheritance (Kalıtım): Miras alma

 # Person => name, lastname, age, eat(), run()...
 # Student(Person), Teacher(Person)

class Person():
     def __init__(self, fname,lname):
         self.firstname = fname
         self.lastname = lname
         print("Person Created")

     def who_am_i(self):
        print("I am a person")

     def eat(self):
         print("I am eating")

class Student(Person):
    # pass   yer tutucu (kod yazılmayacağı zaman kullanılır)
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student Created")

    def who_am_i(self):                   # kalıtım aldığı sınıftaki metodu ezer (override (geçersiz kılmak))
        print("I am a student")

class Teacher(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)           # Person.__init__(self, fname, lname) cümlesinin alternatifi

p1 = Person("Ömer","Ali")
s1 = Student("Ayşe","Burçak",650)

print(p1.firstname+ " " + p1.lastname)
print(s1.firstname+ " " + s1.lastname + " " + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()

p1.eat()
s1.eat()