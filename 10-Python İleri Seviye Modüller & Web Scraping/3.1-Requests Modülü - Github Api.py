import requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "3ddb186412302598cfecd05078323ba3566acffc"

    def getUser(self, username):
        response = requests.get(self.api_url+"/users/"+username)
        return response.json()

    def getRepositories(self,username):
        response = requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()

    def createRepositories(self, name):
        response = requests.post(self.api_url+"/user/repos?access_token="+ self.token, json={
            "name": name,
            "description":"Kod ile oluşturduğum ilk depo",
            "homepage":"https://github.com",
        })
        return response.json()

githubObject = Github()
while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repo\n4- Exit\nSeçiminiz: ")

    if secim == "4":
        break
    else:
        if secim == "1":
            username = input("Username: ")
            result = githubObject.getUser(username)
            print("name:",result["name"],"public repos:", result["public_repos"], "follower:", result["followers"])
        elif secim == "2":
            username = input("username: ")
            result = githubObject.getRepositories(username)
            for repo in result:
                print(repo["name"])
        elif secim == "3":
            name = input("Repo name: ")
            result = githubObject.createRepositories(name)
            print(result)
        else:
            print("Yanlış seçim!")