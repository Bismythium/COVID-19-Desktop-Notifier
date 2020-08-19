from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier  #for windows notifications

header ={'User-Agent':'Chrome'}
req = Request("https://www.worldometers.info/coronavirus/country/india",headers = header)
html = urlopen(req)

obj = bs(html,'html.parser')

new_cases = obj.find("li",{"class":"news_l i"}).strong.text.split()[0]
death = list(obj.find("li",{"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

# Notifier
notifier =ToastNotifier()
message = "New Cases - " + new_cases +"\nDeath - "+death
notifier.show_toast(title = "COVID-19 Update",msg = message, duration=5,icon_path="./virus.ico")
