#for 문


for v1 in range(10): # 0~9 
    print('v1 is :', v1)

print()

for v2 in range (1,11): # 1~10
    print('v2 is :', v2)

print()

for v3 in range(1,11,2): # 1부터 2씩 건너뛰어 10이하 까지 (즉 홀수만 프린트)
    print('v3 is :', v3)

print()

for v4 in range(0,11,2): # 0부터 2씩 건너뒤어 10이하까지 (0과 짝수만)
    print('v4 is :', v4) 

print()
print()



#1~1000의 합
sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1~1000 Sum :', sum1)

##또는
print('1~1000 Sum :', sum(range(1,1001)))

print()
print()

print('1~100) 4의 배수의 합 : ', sum(range(4,1001,4)))


print()
print()


#List안에 있는 값들을 반복해서 출력하기
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Voo']

for n in names:
    print("You are : ", n)
print()

lotto_numbers = [11,16,21,24,25,62]

for n in lotto_numbers:
    print("Current number : ",n)

print()
print()

#문자열에서 각각의 문자를 뽑아 반복 출력
word = "Beautiful"
for s in word :
    print('word :', s)

print()
print()

#dictionary에서 '값' 반복 출력
my_info = {
    "name" : 'Lee',
    "Age" : 33,
    "city": "Seoul"
}

for key in my_info:
    print("key :", my_info.get(key))
##또는
for val in my_info.values():
    print("key : ", val)

print()

#키만 출력
for key in my_info.keys():
    print("key is ", key)

print()
print()

#문자열을 전부 대문자로 바꾸기
fruit = 'PineApplE'

for n in fruit:
    if n.isupper(): # 대문자라면
        print(n) #그냥 출력
    else:
        print(n.upper()) # 해당 문자를 대문자로 변환후 출력

print()
print()


#break
numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]

for num in numbers:
    if num == 4:
        print('Found : 4!')
        break
    else:
        print('Not Found : ', num)

print()
print()

#continue : 아랫구문 skip 역할 -> 다시 처음 for문으로
lt = ["1", 2, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue #자료형이 bool 이라면 skip
    print("current type : ", v, type(v))


print()
print()


#for - else  
numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]

for num in numbers: 
    if num ==24:
        print("Found : 24")
        break
else : 
    print('Not Found : 24') #24가 존재하기 때문에 위의 break 문으로 인하여 실행되지 X

print()

for num in numbers:
    if num ==49:
        print("Found : 49")
        break
else : 
    print('Not Found : 49') #위의 if 문이 만족되지 않이 때문에 실행됨

print()
print()


#구구단 출력
for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i*j), end='')
    print()


#형변환
name2 = 'Aceman'
print('Reversed', reversed(name2)) 
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) #set은 순서 X