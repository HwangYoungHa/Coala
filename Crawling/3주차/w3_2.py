import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EC%95%8C%EB%9D%BC",
                   headers={"User-Agent":"Mozilla/5.0"}) # 데이터 요청시 브라우저에서 요청한 것처럼 만듦

html = BeautifulSoup(raw.text, 'html.parser')

# 0. 컨테이너
# 컨테이너 : ul.type01 > li (제한적 name일 경우 상위의 범위로 나갈것)
# 기사제목 : a._sp_each_title (class 내부 띄어쓰기 : 클래스 이름이 다수개인 경우)
# 언론사 : span._sp_each_source

# 1. 컨테이너 수집
articles = html.select("ul.type01 > li")

# 2. 기사 데이터 수집 + 3. 반복하기
for ar in articles:
    title = ar.select_one("a._sp_each_title").text
    source = ar.select_one("span._sp_each_source").text
    print(title, source)
    print("="*25)

# 단점 : 한 페이지에서만 수집 가능...
