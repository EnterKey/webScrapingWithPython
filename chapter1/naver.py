from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObj = BeautifulSoup(html.read(), "html.parser")
# for child in bsObj.find("", {"class":"ah_roll_area PM_CL_realtimeKeyword_rolling"}).ul.children:
#     print(child)

for child in bsObj.findAll("span", {"class":"ah_k"}):
    print(child.get_text())


