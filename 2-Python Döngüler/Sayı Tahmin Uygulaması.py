"""1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalış"""

import random

tahminSayisi = input("1-100 arası bir sayı girin:")

uretilenSayi = random.randrange(1,100)

print(uretilenSayi)

while True:
    if(int(tahminSayisi) == uretilenSayi):
        print("Tebrikler bildiniz!")
        exit()
    if(int(tahminSayisi) > uretilenSayi):
        print("Tahmininiz yüksek düşürün")
    if(int(tahminSayisi) < uretilenSayi):
        print("Tahmininiz düşük, arttırın")
    tahminSayisi = input("Tekrar deneyin:")
