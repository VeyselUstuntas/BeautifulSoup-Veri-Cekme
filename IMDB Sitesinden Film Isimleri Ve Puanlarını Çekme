from bs4 import BeautifulSoup
import requests
import lxml

adres = "https://www.imdb.com/chart/top"
request = requests.get(adres)

soup = BeautifulSoup(request.content,"lxml")


top250 = soup.find("tbody",attrs={"class":"lister-list"}).find_all("tr")

for i in top250:
    adi = i.find("td",attrs={"class":"titleColumn"}).a.text
    #puan= i.find("td",attrs={"class":"ratingColumn imdbRating"}).strong.text
    puan = i.find("td",attrs={"class":"ratingColumn imdbRating"}).strong.get("title")
    tarih = i.find("td",attrs={"class":"titleColumn"}).span.text
    print(f"Filmin adı '{adi}' ve IMBD puanı {puan} ve çıkış yılı {tarih}\n")
