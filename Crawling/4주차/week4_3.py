import requests
from bs4 import BeautifulSoup

# csv 형식으로 저장하기
f = open("navertv.csv", "w", encoding='UTF-8')
f.write("제목, 채널명, 재생수, 좋아요\n") #header

raw = requests.get("https://tv.naver.com/r/")
print(raw)
html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("div.inner")

for cont in container:
    title = cont.select_one("dt.title").text.strip()
    chn = cont.select_one("dd.chn").text.strip()
    hit = cont.select_one("span.hit").text.strip()
    like = cont.select_one("span.like").text.strip()

    title = title.replace(",","")
    chn = chn.replace(",", "")
    hit = hit.replace(",", "")
    like = like.replace(",", "")

    hit = hit.replace("재생 수", "") #replace
    like = like[5:] #슬라이싱

    #print(title.text.strip())
    #print(chn.text.strip())
    #print(hit.text.strip())
    ##print(like.text.strip())
    #print("=" * 50)
    f.write(title+','+chn+','+hit+','+like+'\n')

f.close()