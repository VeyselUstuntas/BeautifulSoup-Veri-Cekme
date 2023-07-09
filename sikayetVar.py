from bs4 import BeautifulSoup as bs
import urllib.request as urlBilgi

adres = "https://www.sikayetvar.com/bmw"
istek = urlBilgi.Request(adres,headers={'User-Agent':'Mozilla/5.0'})

icerik = urlBilgi.urlopen(istek).read()

soup = bs(icerik,"html.parser")

for sikayet in soup.find_all("article",class_="story-card"):
    baslik = sikayet.find("h2").a.text
    icerik = sikayet.find("section").p.text
    print(f"""
        {baslik}
        
        {icerik}
    \n""")
