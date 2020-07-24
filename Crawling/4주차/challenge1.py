import requests
from bs4 import BeautifulSoup

# 네이버 검색 page -> 1페이지 넘어갈 때마다 page가 10씩 증가
# ex) 1페이지 : 1 / 2페이지 : 11 / 3페이지 : 21 ...

f = open("ch1_output.csv", "w", encoding='UTF-8')
f.write("기사제목, 언론사\n")


page = 1
for page in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=코알라&start="+str(page),
                       headers={"User-Agent":"Mozilla/5.0"}) # 데이터 요청시 브라우저에서 요청한 것처럼 만듦
    html = BeautifulSoup(raw.text, 'html.parser')

# 해당 페이지에서의 container 데이터 수집
    articles = html.select("ul.type01 > li")

# 해당 페이지에서 수집한 데이터 출력
    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text

        title = title.replace(",","")
        source = source.replace(",","")
        f.write(title+","+source+'\n')

f.close()