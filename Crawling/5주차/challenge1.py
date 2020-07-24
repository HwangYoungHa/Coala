import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd", headers={"User-Agent": "Mozila/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# container : div.lister-item
# title : h3.lister-item-header a
# director : p.text-muted a:nth-of-type(1)
# actors : p.text-muted a:nth-of-type(2~5)

movies = html.select("div.lister-item")

for m in movies:
    title = m.select_one("h3.lister-item-header a").text
    people = m.select("p.text-muted a")
    director = people[0]
    actors = people[1:]
    print("제목 : ", title)
    print("감독 : ", director.text)
    print("주연 :  ",end='')
    for a in actors:
        print(a.text,",",end='')
    print("\n")
    print("-"*50)