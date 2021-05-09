import urllib.request as req
from bs4 import BeautifulSoup

url = "https://m.stock.naver.com/marketindex/index.nhn"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")
money = soup.select_one("#content > div.ct_wrp > div.ct_box.intnl_major_item > ul > li:nth-child(1) > a > div.price_wrp > span").get_text()

print("현재 환율은 %s입니다\n" % money)
WON = int(input("원화금액을 입력해주세요:"))
money = money.replace(",","")
price = WON / float(money)
print("%0.2f 달러 입니다." % price)