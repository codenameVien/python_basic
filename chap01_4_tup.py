#튜플

a=(1,)
print(type(a))
print()
print()

c=(11,12,13,14)
d=(100,10000,'Ace', 'Base',"captine")
e=(100,10000,('Ace', 'Base',"captine"))

print(d[1])
print(d[0]+d[1]+d[1])
print(d[-1])
print(e[-1])
print(e[-1][1])

print(d[0:3])
print(d[2:])
print(e[2][1:3])

print(c+d)
print(c*3)

#튜플함수
a=(5,2,3,1,4)
print(a)
print(a.index(3))
print(a.count(2))

print()
print()

#팩킹
t=('foo','bar','baz','qux')

print(t)
print(t[0])
print(t[-1])


#언팩킹 #각 원소에 대입
(x1,x2,x3,x4)=t

print(type(x1), type(x2), type(x3), type(x4))
print(x1,x2,x3,x4)