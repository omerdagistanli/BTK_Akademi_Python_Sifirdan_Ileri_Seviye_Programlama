website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan sona Python Programlama rehberiniz (40 saat)"

# 1- " Hello world " boşlukları sil
# 2- "www.sadikturan.com" sadikturan hariç herşeyi sil
# 3- "website" içinde kaç tane "a" var ?
# 4- "course" tüm karakterleri küçült
# 5-  "website" www ile başlayıp com ile bitiyor mu ?
# 6- "website" içinde ".com" var mı ?
# # 7- "course" ifadesindeki boşlukları "-" ile değiştir
# 8- "Hello world" world > "there" yap

""" 1 """
kelime = " Hello world "
kelime = kelime.strip()

print("1.cevap ->" + kelime)

""" 2 """
kelime1 = "www.sadikturan.com"
kelime2 = kelime1[4:14]

print("2.cevap ->" + kelime2)

""" 3 """
deger = website.count("a")

print("3.cevap ->" + str(deger))

""" 4 """
kelime3 = course.lower()

print("4.cevap ->" + kelime3)

""" 5 """
basliyomu = website.startswith("www")
bitiyomu = website.endswith("com")

print("5.cevap1 ->" + str(basliyomu))
print("5.cevap2 ->" + str(bitiyomu))

""" 6 """
varmi = website.count(".com")

print("6.cevap ->" + str(varmi))

""" 7 """
course = course.replace(" ", "-")

print("7.cevap ->" + course)

""" 8 """
kelime = kelime.replace("world", "there")

print("8.cevap ->" + kelime)