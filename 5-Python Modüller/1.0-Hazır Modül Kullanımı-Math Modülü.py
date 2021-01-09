# import math as islem
#
# value = islem.factorial(6)
#
# print(value)

# Yöntem 2
# bu tanım tüm modüllerin programa inerek gereksiz yer kaplamasını önler


from math import factorial, sqrt, fmod

# kendi metodumuz modülün altındaysa çalışır değilse modül çalışır

def sqrt(x):
    print("x:" + str(x))

deger = sqrt(144)

print(deger)