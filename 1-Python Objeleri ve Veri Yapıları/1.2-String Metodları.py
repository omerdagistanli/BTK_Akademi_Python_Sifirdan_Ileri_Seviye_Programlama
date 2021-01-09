message = "Merhaba, benim adım Ömer Dağıstanlı"

# .upper() bütün karakterleri büyük harf yapar
# message = message.upper()

# .lower() bütün karakterleri küçük harf yapar
# message = message.lower()

# .title() her kelimenin baş harfi büyük harf olur
# message = message.title()

# .capitalize() değişken içindeki stringin ilk harfi büyük olur, gerisini küçültür
# message = message.capitalize()

# .strip() string başındaki ve sonundaki boşlukları siler
# message = message.strip()

# .split() boşluklara göre parçalama
# message = message.split()
# print(message[3])             'Ömer' kelimesini vericektir
# message = " ".join(message)   parçalanmış kelimeleri, aralarına 1 boşluk bırakarak tamamlıyacak
# message = message.split(,)    ',' karakterine göre parçalama yapar

# .find() aranan kelimenin ilk harfinin index nosunu döndürür, bulamazsa "-1" döndürür
# .rfind() aramaya sağdan başlar     rightfind()
# index = message.find("Ömer")

# isFound = message.startswith("M")    string ifade "M" ile başlarsa isFound değişkeni True olur
# isFound = message.startswith("M")

# isFound = message.endswith("ı")    string ifade "ı" ile biterse isFound değişkeni True olur
# isFound = message.endswith("ı")

# .replace("Ömer", "Ali") string içinde "Ömer" bulursa onu "Ali" yapar
# message = message.replace("Ömer","Ali")
#                   .replace("ö","o")
#                   .replace("ç","c")........

# .center() string ifadeyi girilen değerin ortasına yazar, sağ ve soldan eşit boşluklar bırakır
# message = message.center(50, "*")     sağ ve soluna yıldılar koyar


print(message)