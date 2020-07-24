f = open('test.txt', 'w') # test.txt 파일을 w형식(write)으로 생성
f.write('Hello world!\n')
f.write('Good Bye') # Hello world!와 Good Bye test파일에 입력

f.close() # 열었던 파일을 닫는 기능