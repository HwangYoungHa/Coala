import requests
from bs4 import BeautifulSoup
import openpyxl

keyword = input("검색어를 입력해 주세요: ") #키워드 입력받음

try: #c++과 동일 문법
    wb = openpyxl.load_workbook("navernew.xlsx") #기존 파일 로드 후 입력
    sheet = wb.active
    print("불러오기 완료")
except: # try에서 error 발생시의 코드(파일이 존재하지 않을 경우)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["제목", "언론사"]) #header(except일 때만 수행)
    print("새로운 파일 생성")

# 네이버 검색 page -> 1페이지 넘어갈 때마다 page가 10씩 증가
# ex) 1페이지 : 1 / 2페이지 : 11 / 3페이지 : 21 ...
page = 1
for page in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query="+keyword+"&start="+str(page), #입력받은 키워드 검색
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

# 해당 페이지에서의 container 데이터 수집
    articles = html.select("ul.type01 > li")

# 해당 페이지에서 수집한 데이터 출력
    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text
        print(title, source)
        sheet.append([title, source])

wb.save("navernews.xlsx")