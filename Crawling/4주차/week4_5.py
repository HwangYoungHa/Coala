import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook() #openpyxl.Workbook 실행
sheet = wb.active #sheet 선택
sheet.append(["제목", "채널명", "재생수", "좋아요수"]) #header 추가

raw = requests.get("https://tv.naver.com/r/")
print(raw)
html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("div.inner")

for cont in container:
    title = cont.select_one("dt.title").text.strip()
    chn = cont.select_one("dd.chn").text.strip()
    hit = cont.select_one("span.hit").text.strip()
    like = cont.select_one("span.like").text.strip()

    hit = hit.replace("재생 수", "")
    like = like.replace("좋아요 수", "")

    sheet.append([title, chn, hit, like])
    # print(title.text.strip())
    # print(chn.text.strip())
    # print(hit.text.strip())
    # print(like.text.strip())

wb.save("navertv.xlsx") #원하는 방식으로 저장