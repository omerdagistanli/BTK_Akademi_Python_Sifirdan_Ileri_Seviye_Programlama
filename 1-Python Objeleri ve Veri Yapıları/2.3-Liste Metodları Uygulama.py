names = ["Ali", "Yağmur", "Ömer", "Burçak"]
years = [1998, 2000, 1996,1995]

# 1-    "Cenk" ismini liste sonuna ekle
# 2-    "Sena" değerini liste başına ekle
# 3-    "Yağmur" ismini listeden sil
# 4-    "Ali" isminin indeksi nedir?
# 5-    "Ali" listenin bir elemanı mı ?
# 6-    listeyi terse çevir
# 7-    listeyi alfabetik yap
# 8-    years rakamsal büyüklüğe göre sırala
# 9-    years en büyük ve en küçük ?
# 10-   year kaç tane 1998 var ?

""" 1 """
names.append("Cenk")
print("Cevap1->", names)

""" 2 """
names.insert(0, "Sena")
print("Cevap2->", names)

""" 3 """
names.remove("Yağmur")
print("Cevap3->", names)

""" 4 """
print("Cevap4->", names.index("Ali"))

""" 5 """
if names.count("Ali")>0:
    print("Cevap5-> Evet")

""" 6 """
names.reverse()
print("Cevap6->", names)

""" 7 """
names.sort()
print("Cevap7->", names)
""" 8 """
years.sort()
print("Cevap8->", years)

""" 9 """
yearsMin = min(years)
yearsMax = max(years)
print("Cevap9.1->", yearsMin)
print("Cevap9.2->", yearsMax)

""" 10 """
print("Cevap10->", years.count(1998))
