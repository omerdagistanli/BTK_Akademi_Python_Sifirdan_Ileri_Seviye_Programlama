# 1- "Bmw, Mercedes, Opel, Mazda" listesi oluştur
# 2- liste kaç elemanlıdır ?
# 3- listenin ilk ve son elemanı ?
# 4- Mazda -> Toyota
# 5- listenin ilk 3 elemanını alın
# 6- listeye audi ekle
# 7- listeyi tersten yazdır

""" 1 """
arac_liste = ["Bmw", "Mercedes", "Opel", "Mazda"]
print("Cevap1->",arac_liste)
""" 2 """
print("Cevap2->", len(arac_liste))

""" 3 """
print("Cevap3.1->", arac_liste[0])
print("Cevap3.2->", arac_liste[3])

""" 4 """
arac_liste[3] = "Toyota"
print("Cevap4->", arac_liste)

""" 5 """
print("Cevap5->", arac_liste[:3])

""" 6 """
arac_liste.append("Audi")
print("Cevap6->", arac_liste)

""" 7 """
#print("Cevap7->", arac_liste[::-1])
arac_liste.reverse()
print("Cevap7->", arac_liste)