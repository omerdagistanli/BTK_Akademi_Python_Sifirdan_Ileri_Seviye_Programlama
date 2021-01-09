# n burda parametre olduğu için değişim olmadı, değişkenin kopyası göndereliyo
def changeName(n):
    n = "Ahmet"

name = "Ömer"
changeName(name)
print(name)

# n dizinin adresini barındırdığı için değişim oldu
def change(n):
    n[0] = "istanbul"

citys = ["ankara", "izmir"]
change(citys)
print(citys)

# fazla sayıda parametre göndermenin kısa yolu   (tuple list)
def add(*params):
    return  sum((params))

print(add(10,20,30,5,45,343,35))

# dictionary list
def displayUser(**args):
    for key, value in args.items():
        print("{} is {}".format(key,value))

displayUser(name = "Ömer", age = 24, city = "Çanakkale")