#딕셔너리

# 선언
a = {'name': 'Kim', 'phone':'01033337777', 'birth':'122134'}
b= {0:'Hello python'}
c= {'arr':[1,2,3,45]}
d= {
    'Name': 'Kim',
    'city': 'seoul',
    'Age':22
}
f= dict(
    Name='Kim',
    City='Seoul',
    Age=22
)

print()

print('a - ', a['name']) #if name 존재 X -> 에러 발생
print('a - ', a.get('name1')) # name1 존재 X -> None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('Name'))
print('f - ', f.get('Status'))

print()
print()

#딕셔너리 추가/수정
a['address'] = 'seoul'
print('a -', a)
a['status'] = 'true'
print('a -', a)
a.update(birth='910924')
print('a -', a)
print()
print()



#함수
# dict_keys, dict_values, dict_items : 반복문(_iter_)에서 사용가능

## 키 만 가져오는
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print()
###dict_keys라는 자료형에서 우리가 필요한 리스트만 가져오게 해줌 (형변환)
print('a - ', list(a.keys())) 
print('b - ', list(b.keys()))
print()

##값만 보여주는 dict_values
print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print()
###dict_values에서 필요한 리스트만 가져오게 해줌
print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print()
print()


print('a-',a.pop('name'))
print('a-',a)

print()
print()

print('a-','birth' in a)