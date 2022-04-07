# 참조
# csv 파일 만들기
# https://walknrest.tistory.com/288
# 데이터 csv 파일로 저장
# https://book.coalastudy.com/data_crawling/week4/stage2#:~:text=파이썬으로 csv파일 만들기
# 현재 디렉토리 위치 얻는 방법
# https://codechacha.com/ko/python-examples-get-working-directory/
import os
import csv

path = os.getcwd() + "\\0407"
os.chdir(path)

f = open("hitsong.csv", "w",newline='',encoding="utf-8-sig")

singers = ["박정현", "임창정", "izi", "아이유"]
songs = ["꿈에\n봄", "소주한장", "응급실", "좋은날"]

edit = csv.writer(f)

edit.writerow(['','singers','songs'])

for i in range(len(singers)):
    edit.writerow([i,singers[i],songs[i]])
    
f.close()