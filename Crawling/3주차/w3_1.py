import requests
from bs4 import BeautifulSoup #bs4 패키지 안에 있는 BeautifulSoup

raw = requests.get("https://tv.naver.com/r/") #페이지의 data를 가져와서 raw에 저장
print(raw) #잘 가져왔을 경우 -> 200 출력 / 아닐 경우 -> 404 출력
# print(raw.text) # html코드 출력
html = BeautifulSoup(raw.text, 'html.parser')
# print(html)

'''parcing : 문자열을 유의미한 단위로 구분하는것
get : html 단순 복사 / BequtifulSoup : 의미 인식 후 복사'''

# 1-3위 컨테이너 : div.inner
# 제목 : dt.title
# 채널명 : dd.chn
# 재생수 : span.hit
# 좋아요수 : span.like

# 컨테이너 수집 -> 영상별 데이터 수집 -> 수집반복(컨테이너)

#1. 컨테이너 수집
container = html.select("div.inner")
#print(container) # list형식으로 저장

#2. 영상 데이터 수집
for cont in container: # container 리스트의 element를 cont로 설정 후 반복
    title = cont.select_one("dt.title") # container[0]에서 title 걸러냄
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")
    # container -> 한 페이지에 여러개 => select 사용
    # title -> container[0] 안에 오직 하나! => select_one 사용

    print(title.text.strip()) # .text : 해당 html문의 태그 지우고 내용만 출력
    print(chn.text.strip()) #.strip() : 공백 없애기
    print(hit.text.strip())
    print(like.text.strip())
    print("=" * 50)

#3 반복하기

