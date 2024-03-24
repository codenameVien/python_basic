# 집합(set)

#선언
a=set()
b= set([1,2,3,4])
d= set([1,2,3,'Pen', 'Cap','Plate'])
e={'foo', 'bar', 'baz'}  #키가 없는 딕셔너리 모양 = set
f={42,'foo', (1,2,3), 3.14} \




###형변환
#튜플 변환 (set -> tuple)
t = tuple(b) #b를 튜플로
print('t - ', type(t), t)
print('t - ', t[0], t[1:3]) # tuple로 변환되었으므로 슬라이싱 가능

#리스트 변환 (set -> list)
l = list(b)
l2 = list(e)

print('l - ', type(l), l)
print('l2 - ', l2)


print()
print()



s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#교집합
print('s1 &s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))
print()
#합집합
print('s1|s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2))
print()
#차집합
print('s1-s2 : ', s1 - s2)
print('s1-s2 : ', s1.difference(s2))
print()

#중복원소 확인 (공통 원소를 가지지 않으면 True를, 가지면 False를)
print('s1 & s2 : ', s1.isdisjoint(s2))

#부분집합 확인
print(s2.issubset(s1)) # s2의 '모든' 요소가 s1에 포함되어있는지 (부분집합인지)
print(s1.issuperset(s2)) #s1이 s2를 포함하는지
print()

#데이터 추가 & 제거
s1 = set([1,2,3,4])
s1.add(5)
print(s1)

s1.remove(2)
print(s1)
s1.discard(3) # 없는 거 지우면 에러남
print(s1)
s1.discard(7) # 얘는  집합에 없는 원소를 지우더라도 예외(에러)가 없음
print(s1)

s1.clear() # 싹 다 지우기
print(s1)