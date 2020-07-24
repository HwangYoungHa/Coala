# 영화 페이지의 제목을 클릭 후 상세 페이지의 평점과 리뷰 탐색
import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={"User-Agent": "Mozila/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너: dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목: dt.tit > a # 평점: dd.star_t1 a span.num
    title = m.select_one("dt.tit > a")
    url = title.attrs["href"] #attrs : attribute
    print(title.text)

    each_raw = requests.get("https://movie.naver.com"+url, headers={"User-Agent":"Moziala/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')
    # print("https://movie.naver.com"+url) # 해당 url 출력

    # https://movie.naver.com/movie/bi/mi/basic.nhn?code=193804
    # movie.naver.com/movie 뒤 내용에 따라 들어가는 사이트 변동

    #컨테이너 (세부 사이트) div.score_result > ul > li
    #평점 div.star_score em
    #리뷰 div.score_reple p

    # reviews = each_html.select("div.score_result > ul > li")
    #
    # for r in reviews: # 세부 사이트의 정보 출력
    #     stars = r.select_one("div.star_score em").text
    #     star = stars.strip() # 공백 제거
    #     reples = r.select_one("div.score_reple p").text
    #     reples = reples.strip() # 공백 제거
    #     print(stars, reples)

    # 포스터 선택자 : div.mv_info_area div.poster a img
    poster = each_html.select_one("div.mv_info_area div.poster a img")
    poster_src = poster.attrs["src"] #속성 중 src 추출
    print(poster_src)
    print("-"*50)

