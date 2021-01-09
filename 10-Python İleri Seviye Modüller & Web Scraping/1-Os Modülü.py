import os

# os.chdir("C:\\ C dizininde işlem yapmaya hazır")
# os.mkdir("Yeni Klasör Oluşturur")

# listeleme        c dizindeki herşeyi listeler
# result = os.listdir("C:\\")

# bilgi alma
# result = os.stat("dosya_adi")

# silme                                 alt klasörü siler
# os.rmdir("yeni klasör")     os.removedirs("yeni klasör/alt klasör")

# path
# result = os.path.abspath("1-Os Modülü.py")

result = os.name
result = os.getcwd()

print(result)
