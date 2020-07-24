import requests
from bs4 import BeautifulSoup

raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx", headers={"User-Agent": "Mozila/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

#container(main page) : div.main_detail li
movies = html.select("div.main_detail li > a")

for m in movies:
    url = m.attrs["href"] # getting url of each movies
    each_raw = requests.get(url, headers={"User-Agent": "Mozila/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    details = each_html.select("div.detail_summarize div.movie_summary")
    for d in details:
        try:
            title = d.select_one("div.subject_movie strong.tit_movie").text
            score = d.select_one("div.subject_movie a em.emph_grade").text
            genre = d.select_one("dl.list_movie dd.txt_main").text
            director = d.select_one("dl.list_movie dd:nth-of-type(5) a").text
            actors = d.select("dl.list_movie dd:nth-of-type(6) a")
        except:
            title = d.select_one("div.subject_movie strong.tit_movie").text
            score = d.select_one("div.subject_movie a em.emph_grade").text
            genre = d.select_one("dl.list_movie dd.txt_main").text
            director = d.select_one("dl.list_movie dd:nth-of-type(6) a").text
            actors = d.select("dl.list_movie dd:nth-of-type(7) a")

        finally:
            title = title.strip()
            score = score.strip()
            genre = genre.strip()
            director = director.strip()
            print("제목 : ", title)
            print("별점 : ", score)
            print("장르 : ", genre)
            print("감독 : ", director)
            print("주연 :  ", end='')
            for a in actors:
                print(a.text,end='')
            print("\n")
            print("="*50)


#container(detailed) : div.detail_summarize
#title : div.movie_summary div.subject_movie strong.tit_movie
#score :  div.movie_summary div.subject_movie a em.emph_grade
#장르 : dl.list_movie dd.txt_main
#감독 : dl.list_movie dd.type_ellipsis(1번째) a
#배우 : dl.list_movie dd.type_ellipsis(나머지) a