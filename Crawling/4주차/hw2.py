import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("hw2_output.xlsx")
    sheet = wb.active
    print("load completed")
except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["기사제목", "기사요약"])
    print("new file made")

# 기사제목 / 기사요약
# 컨테이너 : div.wrap_cont
# 제목 : div.wrap_cont a.f_link_b
# 요약 : div.wrap_cont p.f_eb

for page in range(1, 4):
    raw = requests.get("https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EC%BD%94%EC%95%8C%EB%9D%BC&p="+str(page))
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.wrap_cont")

    for ar in articles:
        title = ar.select_one("a.f_link_b").text
        summary = ar.select_one("p.f_eb").text
    #     print(title, ":", summary)
    #     print("\n")
    # print('='*50)
        sheet.append([title, summary])

wb.save("hw2_output.xlsx")