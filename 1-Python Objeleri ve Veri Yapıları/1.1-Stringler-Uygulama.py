website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan sona Python Programlama rehberiniz (40 saat)"

# 1- "course" karakter dizisinde kaç karakter bulunmaktadır ?
# 2- "website" içinden www karakterlerini al
# 3- "website" içinden com karakterlerini al
# 4- "course" içinden ilk 15 ve son 15 karakterleri al
# 5-  "course" ifadesindeki karakterleri tersten yaz

name, surname, age, job  = "Bora", "Yılmaz", 32, "mühendis"

# 6- yukarda verilen değişkenler ile ekrana aşağıdaki ifadeyi yaz
# "Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis."
# 7- "Hello world" ifadesindeki w harfini W ile değiştirin
# 8- "abc" ifadesinini yan yana 3 defa yazdırın

""" 1 """
print("1.Cevap ->" + str(len(course)))

""" 2 """
print("2.Cevap ->" + website[7:10])

""" 3 """
uzunluk = len(website)
print("3.Cevap ->" + website[uzunluk-3:uzunluk])

""" 4 """
print("4.Cevap ->" + course[0:15] + course[-15:])

""" 5 """
print("5.Cevap ->" + course[::-1])

""" 6 """
print("6.Cevap ->" + "Benim adım {i} {s}, yaşım {y} ve mesleğim {m}".format(i = name, s = surname, y = age, m = job))

""" 7 """
kelime = "Hello world"
kelime = kelime[0:6] + "W" + kelime[7:]
print("7.Cevap ->" + kelime)

""" 8 """
veri = "abc"
print("8.Cevap ->" + 3 * veri)