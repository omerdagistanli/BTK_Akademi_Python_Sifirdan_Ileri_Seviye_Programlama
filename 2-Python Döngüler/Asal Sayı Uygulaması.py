""" Girilen sayı asal mı ?"""

sayi = input("Sayı giriniz:")

for i in range(2,int(sayi),1):
    if(int(sayi) % i != 0):
        print("Girilen sayı asal sayıdır")
        exit()
    else:
        print("Girilen sayı asal değildir")
        exit()