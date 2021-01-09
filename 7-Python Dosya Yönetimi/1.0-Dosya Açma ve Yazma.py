# open(dosya_adi,dosya_erişme_modu) kullanım şekli

# "w" yazma modu.Dosyayı konumda oluşturur, daha önceden varsa içeriği siler.
# "a" ekleme modu.Dosya konumda yoksa oluşturur
# "x" (create) oluşturma modu.Dosya varsa hata verir
# "r" okuma modu.Dosya yoksa hata verir
# "r+" okuma ve yazma modu.

file = open("deneme.txt","w",encoding="utf-8")
file.write("Ömer Dağıstanlı")
file.close()
