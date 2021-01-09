# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#
#     return wrapper
#
# @my_decorator
# def sayHello(name):
#     print("hello",name)
#
# sayHello("ali")

from math import pow, factorial
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        
        func(*args,**kwargs)

        finish = time.time()
        print("Fonksiyon "+func.__name__ + " " + str(finish - start) + " saniye sürdü")
    return inner

@calculate_time
def usAlma(a,b):
    print(pow(a,b))

@calculate_time
def faktoriyel(num):
    print(factorial(num))

usAlma(2,3)
faktoriyel(4)
