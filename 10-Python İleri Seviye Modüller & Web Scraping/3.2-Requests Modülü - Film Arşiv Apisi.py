# themovieeb.com => film ve dizi arşivi
# themoviedb nin sunduğu apiyi kullanıcaz
# anahtar kelimeye göre arama
# en popüler film listesi
# vizyondaki fimler

import requests

class theMovieDb():
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "771a21552c55924cb0f8c9a9d93fad22"

    def getPopulars(self):
        response = requests.get(self.api_url+"/movie/popular?api_key="+self.api_key+"&language=en-US&page=1")
        return  response.json()

    def nowPlayin(self):
        response = requests.get(self.api_url+"/movie/now_playing?api_key="+self.api_key+"&language=en-US&page=1")
        return response.json()

    def getSearch(self,keyword):
        response = requests.get(self.api_url+"/search/keyword?api_key="+self.api_key+"&query="+keyword+"&page=1")
        return response.json()

movieApi = theMovieDb()

while True:
    print(" Welcome ".center(40,"*"))
    secim = input("1- Popular Movies \n2- Now Playing\n3- Search Movies\nSeçim: ")
    if secim == "1":
        movies = movieApi.getPopulars()
        for movie in movies["results"]:
            print(movie["title"])
    elif secim == "2":
        nowPlayingMovies = movieApi.nowPlayin()
        for movie in nowPlayingMovies["results"]:
            print(movie["title"])
        if movie["title"] != "Mulan":
            print("\nMulanı hemen izleyin\n")
    elif secim == "3":
        searchWord = input("Kelime: ")
        searchMovie = movieApi.getSearch(searchWord)
        for movie in searchMovie["results"]:
            print(movie["name"])
