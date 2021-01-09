# range

# 0 dan 10 a kadar (0-9)
for item in range(10):
    print(item)

# 20 den 100 e kadar 10 ar 10 ar (20-90)
for item in range(20, 100, 10):
    print(item)

print(list(range(10, 50, 5)))

# enumerate

index = 0
greeting = "hello there"

for letter in greeting:
    print(f"index: {index} letter: {letter}")
    index += 1

# (0, "h"), (1, "e")...
for item in enumerate(greeting):
    print(item)

# zip

# [(1,a,100), (2,b,200), (3,c,300)]
# herhangi bir listenin indeksi eksikse eksik değere göre fazlaysa az olan değere göre indeksler eşitleniyor
list1 = [1,2,3]
list2 = ["a","b","c"]
list3 = [100,200, 300]

print(list(zip(list1,list2,list3)))