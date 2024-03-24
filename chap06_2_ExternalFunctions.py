#외장 함수
#종류 : sys, pickle, shutill, temfile, time, random 등

print()

# 예제 1
import sys
print(sys.argv)

#예제2(강제 종료)
#sys.exit()

print()

#예제3(파이썬 패키지 위치)
print(sys.path)

print()



#pickle : 객체 파일 쓰기
import pickle

#예제4(쓰기)
f= open("test.obj", 'wb') #write / binary
obj={1:'python', 2:'study', 3:'basic'}
pickle.dump(obj, f)
f.close() #열고나서는 반드시 닫아야함

#예제5(읽기)
f = open('test.obj', 'rb') #read binary
data = pickle.load(f)
print(data, type(data))
f.close()

print()



# os : 환경변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관현
#mkdir, rmdir(비어있으면 삭제), rename

# 예제6
import os
print(os.environ)
#print(os.environ["USERNAME"]) #나 왜 안되뇽

print()

# 예제 7(현재경로)
print(os.getcwd())

print()




# time : 시간관련 처리
import time

# 예제 8
print(time.time())

# 예제 9(형태 변환)
print(time.localtime(time.time()))

# 예제10 (간단표현)
print(time.ctime)

# 예제 11 (형식 표현) - 내가 원하는 대로 출력
print(time.strftime('%Y-%m-%d %H:%Y:%S', time.localtime(time.time())))

# 예제12 (시간 간격 발생)
for i in range(5):
    print(i)
    time.sleep(1) #1초동안 멈춰있다가 실행 - 아 얘가 막 타이머 같은 기능에 쓰이겠네 또는 속도 변환?? 그런거

print()




# random : 난수 관련
import random

# 예제13
print(random.random()) # 0 ~ 1 사이의 실수를 랜덤으로 

# 예제14
print(random.randint(1,45)) # 1~45 사이의 정수를 랜덤으로
print(random.randrange(1,45)) # 1~44 사이의 정수를 랜덤으로 

print()


# 예제15(섞기)
d = [1,2,3,4,5]
random.shuffle(d)
print(d)

#예제16(무작위 선택)
c = random.choice(d)
print(c)

print()




# webbrowser : 본인 os의 웹브라우저 실행

import webbrowser

webbrowser.open("http://google.com")
#webbrowser.open_new("http://google.com") 똑같음
