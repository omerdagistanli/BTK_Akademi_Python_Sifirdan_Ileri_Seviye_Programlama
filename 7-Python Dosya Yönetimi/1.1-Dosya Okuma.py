file = open("deneme.txt","r", encoding="utf-8")

# for döngüsü

# for i in file:
#     print(i, end="")
#
# file.close()

# read() fonksiyonu

content = file.read()
print(content)
file.close()

# readline(), readlines()