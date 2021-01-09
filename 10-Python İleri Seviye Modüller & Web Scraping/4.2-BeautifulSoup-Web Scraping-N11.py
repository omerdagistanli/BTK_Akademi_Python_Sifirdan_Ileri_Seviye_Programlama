from bs4 import BeautifulSoup
import requests

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class":"column"}, limit=5)

for line in list:
     name = line.div.a.h3.text.strip()
     link = line.div.a.get("href")
     oldprice = line.find("div", {"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
     newprice = line.find("div", {"class":"proDetail"}).find_all("a")[1].text.strip().strip("TL")
     print(name.ljust(70), oldprice, newprice,"\n",link)
