import requests
from bs4 import BeautifulSoup

# challenge : 4위 ~ 100위까지의 제목, 채널명, 재생수, 좋아요수 출력
# 컨테이너(4~100위) : div.cds
# 제목 : dt.title
# 채널명 : dd.chn
# 재생수 : span.hit
# 좋아요수 : span.like

raw = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("div.cds")

for cont in container:
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")
    print(title.text)
    print(chn.text)
    print(hit.text)
    print(like.text)
    print("=" * 25)

