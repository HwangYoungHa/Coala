import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("hw1_output.xlsx") #기존 파일 로드 후 입력
    sheet = wb.active
    print("불러오기 완료")
except: # try에서 error 발생시의 코드(파일이 존재하지 않을 경우)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["제목", "저자"])
    print("새로운 파일 생성")

# container : div.lst_thum_wrap li
# title : div.lst_thum_wrap li a strong
# writer : div.lst_thum_wrap li a span.writer


for page in range(1, 6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(page),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')
    books = html.select("div.lst_thum_wrap li")
    for b in books:
        title = b.select_one("div.lst_thum_wrap li a strong").text #제목
        writer = b.select_one("div.lst_thum_wrap li a span.writer").text #저자
        sheet.append([title, writer])
        #print(title, ":", writer)

wb.save("hw1_output.xlsx")