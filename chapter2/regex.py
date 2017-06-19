# http://www.regexpal.com/

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])

# 속성에 접근하기
# myImgTag.attrs['src']

# lambda: 태그 객체를 매개변수로 받아야 하고 불리언만 반환할 수 있다
# ex)  속성이 두개인 태그를 찾는다.
# soup.findAll(lambda tag: len(tag.attrs) == 2)
