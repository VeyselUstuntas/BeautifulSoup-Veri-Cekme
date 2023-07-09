from bs4 import BeautifulSoup as bs
import urllib.request as req
import lxml

adres = "https://www.pttavm.com/arama/elektronik?q=thinkpad"
istek = req.Request(adres,headers={'User-Agent':'Mozilla/5.0'})
icerik = req.urlopen(istek).read()

soup = bs(icerik,"lxml")

for i in soup.find_all("div",class_="product-list-box-container-info"):
    urun_ad = i.find("a").text
    print(urun_ad)
