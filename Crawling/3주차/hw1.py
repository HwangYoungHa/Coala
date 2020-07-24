import requests
from bs4 import BeautifulSoup

# container : div.lst_thum_wrap li
# title : div.lst_thum_wrap li a strong
# writer : div.lst_thum_wrap li a span.writer


for page in range(1, 6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(page),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')
    books = html.select("div.lst_thum_wrap li")
    for b in books:
        title = b.select_one("div.lst_thum_wrap li a strong").text
        writer = b.select_one("div.lst_thum_wrap li a span.writer").text
        print(title, ":", writer)
    print("="*50)