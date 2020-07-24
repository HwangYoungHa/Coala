import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve # url 라이브러리

raw = requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd", headers={"User-Agent": "Mozila/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# container : div.lister-item
# title : h3.lister-item-header a
# director : p.text-muted a:nth-of-type(1)
# actors : p.text-muted a:nth-of-type(2~5)
# poster : div.poster a img

movies = html.select("div.lister-item")

for m in movies:
    title = m.select_one("h3.lister-item-header a")
    print(title.text)
    url = title.attrs["href"]
    each_raw = requests.get("https://www.imdb.com"+url, headers={"User-Agent": "Mozila/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    poster = each_html.select_one("div.poster a img")
    poster_src = poster.attrs["src"]  # 속성 중 src 추출
    print(poster_src)
    urlretrieve(poster_src, "chalposter/" + title.text[:2] + ".png")  # 경로 및 파일 이름 지정
