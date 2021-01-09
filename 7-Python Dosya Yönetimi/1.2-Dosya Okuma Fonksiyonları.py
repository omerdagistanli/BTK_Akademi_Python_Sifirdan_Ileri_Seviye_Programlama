# with olduğu için file.close() a gerek yok

with open("deneme.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(0)
    print(file.tell())         # cursor konumu






