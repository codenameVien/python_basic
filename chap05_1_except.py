#예외처리
#1.예외는 반드시 처리
#2.로그는 반드시 남긴다
# Syntaxerror : 문법 오류
# NameError : 참조 없음 (선언되지 않은 변수를 참조하려 했을때)
# ZeroDivisionError : cant divide with zero(0)
# IndexError : List의 인덱스 범위를 벗어났을때)
# KeyError : dict에 없는 키 가져왔을때
# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# ValueError : List/Tuple/Dict안에 없는 값을 참조시
# FileNotFoundError : 없는 파일을 열거나 지우려고 할떄
# TypeError : 자료형에 맞지 않는 연산을 수행할 경우

# Exception 또는 빈칸 : 모든 에러를 의미 , 포괄적 -> 아 그냥 어떤 예외든 잡을래~ 이럴때 쓰나봄

#예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 : 
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

#예제1 
try:
    z= 'Kim' #Choi 이렇게 바꾸면 except문 실행
    x = name.index(z) # z = 0
    print('{} Found it! {} in name'.format(z,x+1)) # x+1한 이유가 x+1번째 순서라고 표시하기 위해서
except ValueError:
    print("Not Found! - Occured ValueError!")
else:
    print('Ok! else.')

print()


#예제2
try:
    z= 'Choi'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z,x+1)) # x+1한 이유가 x+1번째 순서라고 표시하기 위해서
except Exception: #모든 에러를 잡음 (포괄적)
    print("Not Found! - Occured Error!")
else:
    print('Ok! else.')

print()


#예제3
try:
    z= 'Choi' 
    x = name.index(z) 
    print('{} Found it! {} in name'.format(z,x+1)) # x+1한 이유가 x+1번째 순서라고 표시하기 위해서
except ValueError as e:
    print(e) #에러의 내용을 출력!!! (alias)
    print("Not Found! - Occured ValueError!")
else:
    print('Ok! else.')
finally:
    print("Ok! finally!")

print()


#예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생시킴 
try:
    a= 'Park'
    if a =='Kim': # else문과 except문만 실행
        print('OK! Pass')
    else:
        raise ValueError # 무조건 에러를 발생시켜라 (에러 직접 발생시킴 - 우리가 예외를 직접 만들어서 잡음)
except ValueError:
    print('Occured! Exception!')
else:
    print("Ok! else!")