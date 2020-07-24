# openpyxl 연습하기

import openpyxl

wb = openpyxl.Workbook()  # 새로운 워크북 생성(엑셀파일)
sheet = wb.active  # 현재 활성화 되어 있는 시트
sheet['A1'] = "Hello World"  # 원하는 셀에 data 입력
sheet.cell(row=3, column=3).value = "Good Bye" #row와 column을 통한 입력

sheet.append(["Python", "Java", "HTML", "Javascript"]) #행별로 data 추가
sheet.append(["Coala", "Study", "Crawling"]) #다음 행에 data 추가

wb.save("test.xlsx")
