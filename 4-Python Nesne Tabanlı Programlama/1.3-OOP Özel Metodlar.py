class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu")

    # varsayılan olarak gelen str,len vs metodları sınıf içerisinde kendimiz yazıp içeriğinde değişiklik yapabiliyoruz
    # fakat varsayılan metod işlevini apmaya devam ediyor
    def __str__(self):
        return self.title + " by " + self.director

    def __len__(self):
        return self.duration

    def __del__(self):
        print("SİLMEDİM XD XD")

m = Movie("Film","Yönetmen", 144)

print(str(m))
print(len(m))

#print(m)