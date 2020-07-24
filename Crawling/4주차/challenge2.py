import requests
from bs4 import BeautifulSoup
import openpyxl

keyword = input("검색어를 입력해 주세요: ") #키워드 입력받음

try: #c++과 동일 문법
    wb = openpyxl.load_workbook("challenge2_output.xlsx") #기존 파일 로드 후 입력
    sheet = wb.active
    print("불러오기 완료")
except: # try에서 error 발생시의 코드(파일이 존재하지 않을 경우)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["검색어", "기사제목", "언론사"])
    print("새로운 파일 생성")

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
        sheet.append([keyword, title, source])

wb.save("challenge2_output.xlsx")