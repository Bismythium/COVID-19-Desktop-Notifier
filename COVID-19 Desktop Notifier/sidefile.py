from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier

header = {'User-Agent':'Chrome'}
req = Request("https://www.covid19india.org/",headers=header)
html = urlopen(req)

obj = bs(html,'html.parser')

extract_list =obj.find_all("h5")
print(extract_list)
new_cases = extract_list[0].h4.text.split()
recovered = extract_list[2].h4.text.split()
deceased = extract_list[3].h4.text.split()

notifier = ToastNotifier
message = "New Cases - " +new_cases + "\nRecovered - "+recovered + "\nDeath - " + deceased
notifier.show_toast(title = "COVID-19 UPDATE",msg=message, duration = 5,icon_path="./virus.ico")