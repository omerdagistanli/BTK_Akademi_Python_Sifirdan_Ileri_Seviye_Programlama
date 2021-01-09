import numpy as np

# (10,15,30,45,60) değerlerine sahip dizi oluştur
dizi = np.array([10,15,30,45,60])

# (5-15) arasındaki sayılarla dizi oluştur
dizi = np.arange(5,16)

# (50-100) arasında 5 er 5 er artarak dizi oluştur
dizi = np.arange(50,105,5)

# 10 elemanlı 0 lardan oluşan dizi
dizi = np.zeros(10)

# 10 elemanlı 1 lerden oluşan dizi
dizi = np.ones(10)

# 0 100 arasında eşit aralıklı 5 sayı
dizi = np.linspace(0,100,5)

# (10-30) arasında rastgele 5 sayı üret
dizi = np.random.randint(10,30,5)

# -1,1 arasında 10 sayı üret
dizi = np.random.randn(10)

# 3x5 boyutunda 10-50 arası matris oluştur
dizi = np.random.randint(10,50,15).reshape(3,5)

# üretilen matrisin satır sütün toplamı
# satir = dizi.sum(axis = 1)
# sütun = dizi.sum(axis = 0)
#
# print(satir)
# print(sütun)

# matrisin max min ve mean deperleri
# max = dizi.max()
# min = dizi.min()
# mean = dizi.mean()
#
# print(max)
# print(min)
# print(mean)

# 10-20 arasındaki sayıları içeren dizinin ilk 3 elemanı
dizi = np.arange(10,20)

print(dizi[:3])