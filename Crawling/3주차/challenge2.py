# https://news.ycombinator.com/
# 순위, 제목 수집 파이썬 코드
# 1 ~ 3페이지
import requests
from bs4 import BeautifulSoup

# container : tr.athing
# rank : tr.athing span.rank
# title : tr.athing a.storylink

for page in range(1, 4):
    raw = requests.get("https://news.ycombinator.com/news?p="+str(page),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("tr.athing")

    for ar in articles:
        rank = ar.select_one("tr.athing span.rank").text
        title = ar.select_one("tr.athing a.storylink").text
        print(rank, title)
    print("="*50)