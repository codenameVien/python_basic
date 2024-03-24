#내장함수(Built-in)

# abs 절대값
print(abs(-3))



# all : iterable 요소 전부 검사(참, 거짓)
print(all([1,2,''])) #and 역할
#>>> False (비어있는게 있기 때문에)

print(any([1,2,''])) #or 역할
#>>> True



# chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))



# enumerate : 인덱스 + Iterable 객체 생성
# 즉 반복가능한.. list, set, dict, tuple 객체에 index를 붙여줌
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i+1, name)



# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는값 추출
def conv_pos(x):
    return abs(x) > 2 # 절대값을 씌웠을 때 2보다 큰 값만 리턴
print(list(filter(conv_pos, [1,-3,2,0,-5,6])))
#>>>[-3,-5,6]

#또는 람다식으로 표현
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))



# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs,[1,-3,2,0,-5,6])))
# >>> [1, 3, 2, 0, 5, 6]

# 또는 람다식으로 표현
print(list(map(lambda x: abs(x), [1,-3,2,0,-5,6])))



# max, min : 최대값, 최솟값
print(max([1,2,3]))
print(max('pythonstudy'))
print(min('pythonstudy')) #여기에 공백(띄어쓰기)이 있으면 걔가 가장 작아서 공백이 출력됨!!



# pow 제곱값
print(pow(2,10)) #2의 10제곱



# range : 반복가능한 객체 (Iterable) 반환
print(range(1,10,2)) #>>> range(1, 10, 2)
print(list(range(1,10,2))) #>>> [1, 3, 5, 7, 9]



# round : 반올림
print(round(3.54))
print(round(6.2453,2))



# sorted : 반복가능한 겍체 (Iterable) 오름차순 정렬 후 반환
print([4,1,2,3])
a = sorted([4,2,3,1])
print(a)
print(sorted(['c','a','b']))



# sum : Iterable의 합 반환
print(sum([1,2,3,4]))
print(sum(range(1,101))) # 1~100 의 합



# zip : Iterable의 요소를 짝끼리 묶어서 반환, 짝이 없는 것들은 반환되지 않음 
print(list(zip([10,20,30],[40,50,60])))
#>>> [(10, 40), (20, 50), (30, 60)]
print(list(zip([10,20,30],[40,50]))) #이 경우 30은 짝이 없기에 반환되지 X
