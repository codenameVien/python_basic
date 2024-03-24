#여러 출력법 (fstring사용)
x = 50
y=100
text= 308276567
n='Lee'

ex1= 'n=%s. s=%s, sum %d' %(n,text,(x+y))
print(ex1)

ex2='n={n}, s={s}, sum={sum}'.format(n=n, s=text,sum=x+y)
print(ex2)

ex3=f'n={n}, s={text}, sum={x+y}'
print(ex3)


#구분기호
m=100000000
print(f'm: {m:,}')


#정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽
t=20

print(f"t:{t:10}")
print(f"t is at : {t:^10}")
print(f"t is at : {t:<10}")
print(f"t is at : {t:>10}")

print(f"t is at : {t:-^10}")
print(f"t is at : {t:#<10}")

print()

#멀티라인
multi_str = \
'''
String
Multi Line
Test
'''
print(multi_str)

print()


#문자열 함수
str_o1 = "python"
str_o2 = "Seoul Daejeon Busan"

print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o1.endswith("e"))
print("replace: ", str_o1.replace("thon", 'Good'))
print("sorted: ", sorted(str_o1))
print("split: ", str_o2.split('!'))

print()
print()

a=[5,2,3,1,4]

print(a)
a.append(10)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(3), a[3])
a.insert(2,7)
print(a)
a.reverse()
print(a)
a.remove(7)
print(a)
print(a.pop(2))
print(a.count(4))


print()
print()

c=[70,75,80,85]
c[0]=4
print(c)
c[1:2]=['a','b','c']
print(c)
c[1:3]=[]
print(c)
del c[2]
print(c)


