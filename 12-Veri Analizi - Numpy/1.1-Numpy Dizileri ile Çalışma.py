import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.zeros(10)
# result = np.ones(10)
# result = np.linspace(0,100,5)

# np_array = np.arange(50)
# print(np_array.mean())                # ortalamasını verir
# np_multi = np_array.reshape(5,10)
#
#
# print(np_multi.sum(axis = 1))       # satırların toplamı
# print(np_multi.sum(axis = 0))       # sütunların toplamı

matris1 = np.random.randint(10,100,6)
matris2 = np.random.randint(10,100,6)

mmatris1 = matris1.reshape(2,3)
mmatris2 = matris2.reshape(2,3)

result = np.vstack((mmatris1,mmatris2))         # dikey olarak 2 matrisi birleştirir
result1 = np.hstack((mmatris1,mmatris2))         # yatay olarak 2 matrisi birleştirir

print(result)
print(result1)