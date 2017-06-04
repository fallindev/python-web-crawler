from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

# bsObj.findAll(tagName, tagAttributes)
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
    # get_text 는 모든 태그를 제거하고 텍스트만 남김

# findAll({"h1", "h2", "h3"})
# findAll("span", {"class":{"green", "red"}})

nameList = bsObj.findAll(text="the prince")
print(len(nameList))