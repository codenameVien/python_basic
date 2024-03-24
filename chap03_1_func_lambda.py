#function 함수

#print문으로 호출 
def first_func(w):
    print("Hello ",w)

word = "Goodboy"
first_func(word)


print()


#반환값을 받아서 호출
def return_func(w1):
    value = "Hello " + str(w1)
    return value

x = return_func('Goodboy2')
print(x)


print()


#다중반환
def func_mul(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30

    return y1,y2,y3

x,y,z = func_mul(10) # x값에 10을 넣었을 때 y1,y2,y3에 반환 되는 값
print(x,y,z)


print()


#tuple return & packing
def func_mul2(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30

    return y1,y2,y3

q = func_mul2(10) 
print(type(q), q, list(q))


print()


#list return 
def func_mul2(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30

    return [y1,y2,y3]

p = func_mul2(10) 
print(type(p), p, set(p))


print()


#dictionary return
def func_mul3(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30

    return {'v1': y1, 'v2': y2, 'v3' : y3} #dictionary 형태로 반환

d = func_mul3(10) 
print(type(d), d, d.get('v2'), d.items())

print()
print()

#중요!!
# *args, **kawargs

 # *args(언팩킹) : 여러개의 인자로 함수를 호출할 경우, tuple로 받은 것처럼 인식
def args_func(*args): #매개변수명은 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

args_func('Lee')
args_func('Lee','Park') #여러개의 인자로 함수를 호출할 경우, tuple처럼 인식
args_func('Lee','Park','Kim')  #여러개의 인자로 함수를 호출할 경우, tuple처럼 인식


print()


# **kwargs(언팩킹)) : 키 & 값 (key와 value)형태로 이루어진 걸 dictionary 처럼 할당함
def kwargs_func(**kwargs): #매개변수명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print("-----")

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')

print()

#링크 에제
def introduceEnglishName(**kwargs):
    for key, value in kwargs.items():
        print("{0} is {1}".format(key, value))

introduceEnglishName(MyName="Chris!!")

print()
print()


#전체 혼합 예제
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)
# 10은 args_1에, 20은 args_2에, 
#('Lee', 'Kim', 'Park')은 *args에, 
#{age1:20, age2:30, age3:40} 은 **kwargs에 할당함


print()
print()

#중첩함수
def nested_func(num):
    def func_in_func(num): # 함수 func_in_func 정의부분
        print(num)  # 함수 func_in_func 정의부분
    print("In func")
    func_in_func(num+100)

nested_func(100)
#func_in_func(1000)은 실행 불가 -> 정의되지 않았기 떄문, nested_func에서만 사용가능

print()
print()
print()


#Lamda 람다식
#메모리 절약, 가독성 향상, 코드 간결
#함수는 객체 생성 -> 리소스(메모리)할당
#람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
#남발시 가독성 감소

#일반 함수 표현 #def mul_func(x,y):
#    return x,y : x*y

#Lambda x, y : x*y

#일반적 함수 -> 변수를 할당
def mul_func(x,y):
    return x*y
print(mul_func(10,50)) #그냥 바로 프린트

q=mul_func(10,50) #변수 할당
print(q)

mul_func_var = mul_func #함수에 할당
print(mul_func_var(20,50))


print()


#람다식 -> 람다함수를 할당
lambda_mul_func = lambda x,y : x*y #익명함수에 lambda를 담음    
print(lambda_mul_func(50,50))  


def func_final(x,y,func):
    print('>>>>',x*y*func(100,100))

func_final(10,20, lambda x,y:x*y) #func에 lambda 함수를 할당 (이 줄만 존재해도 실행 가능)
#또는
func_final(10,20, lambda_mul_func) #위에서 lambda 함수를 담은 함수 (위에서 람다를 자기에게 담는 과정 필요)
#또는
func_final(10,20, mul_func_var) #위에서 식을 담은 일반함수 (위에서 한 일반적함수 선언/정의 코드 필요)
## 따라서 한줄로 끝낼수 있는 lambda가 좋다!!! 