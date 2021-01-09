import pandas as pd
df = pd.read_csv("imdb.csv")

# 1- Dosya hakkında bilgiler
result = df
result = df.columns
result = df.info

# 2- İlk 5 kayıt
result = df.head()

# 3-ilk 10 kayıt
result = df.head(10)

# 4- son 5 kayıt
result = df.tail()

# 5- son 10 kayıt
result = df.tail(10)

# 6- sadece movie_title kolonu
result = df["Movie_Title"]

# 7- sadece movie_title kolonu içindeki ilk 5
result = df["Movie_Title"].head()

# 8- movie_title ve rating içeren ilk 5
result = df[["Movie_Title","Rating"]].head()

# 9- movie_title ve rating içeren son 7
result = df[["Movie_Title","Rating"]].tail(7)

# 10- movie_title ve rating içeren ikinci 5 li
result = df[["Movie_Title","Rating"]][5:10]

# 11- movie_title, rating ve imdb = 8.0 ve üstü olan 50 kayıt
result = df[df["Rating"] >= 8.0][["Movie_Title","Rating"]].head(50)

# 12- yayın tarihi 2014-2015 arası filmlerin isimleri
result = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2015)][["Movie_Title", "YR_Released"]]

# 13- num_reviews 100.0 dan büyük yada imdb puanı 8-9 arasındaki fimleri listele
result = df[(df["Num_Reviews"] >= 100000) | ((df["Rating"] >= 8) & (df["Rating"] <= 9))][["Movie_Title", "Rating", "Num_Reviews"]]

print(result)