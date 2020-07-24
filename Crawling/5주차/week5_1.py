import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={"User-Agent": "Mozila/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너: dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목: dt.tit > a
    title = m.select_one("dt.tit > a").text
    # 평점: dd.star_t1 a span.num
    score = m.select_one("div.star_t1 a span.num").text
    # 장르: dl.info_txt1 dd a -> 컨테이너 안의 컨테이너
    # 감독: dl.info_txt1 dd a
    # 배우: dl.info_txt1 dd a

    # #select 함수를 이용하는 방법
    # info = m.select("dl.info_txt1 dd")
    # #장르
    # genre = info[0].select("a") # 한 영화에 여러 장르 가능
    # #감독
    # director = info[1].select("a")
    # #배우
    # actor = info[2].select("a")

    # 선택자를 사용하는 방법
    # (dl_lst_dxc dl.info_txt1 dd:nth-of-type(1) -> 해당 클래스가 갖는 1번째 dd)
    # 장르 (여러 장르가 있을 수 있기 때문에 select 사용)
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    # 감독
    director = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    # 배우
    actor = m.select("dl.info_txt1 dd:nth-of-type(3) a")

    print("제목: ",title)
    print("평점: ",score)
    print("장르 : ")
    for g in genre:
        print(g.text)
    print("감독 : ")
    for d in director:
        print(d.text)
    print("배우 : ")
    for a in actor:
        print(a.text)
    print('=' * 50)